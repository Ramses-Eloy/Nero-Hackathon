# Analisis 2224

Fecha: 2026-10-09, America/Panama. Fuente: captura del usuario, consultas en daa00609 y lookup del template.
Notebook: https://daa00609.apps.dynatrace.com/ui/apps/dynatrace.notebooks/notebook/38b8cf3e-4319-41bc-b207-8b1bea907134#74fea15f-0541-43e1-a972-02eed9241940
Ventana: Last 3 days. Dataset Gigamon de 7425 registros validado en 2218.

```dql
fetch logs
| filter vendor == "Gigamon"
| fieldsAdd cipher = toLong(ssl_cipher_suite_id), octets = splitString(dst_ip, ".")
| filter startsWith(dst_ip, "10.") or startsWith(dst_ip, "192.168.") or (startsWith(dst_ip, "172.") and toLong(octets[1]) >= 16 and toLong(octets[1]) <= 31)
| lookup [load "/lookups/tls-cipher-suites-table" | fieldsAdd cipher = toLong(NumericID)], sourceField: cipher, lookupField: cipher, prefix: "tls."
| filter toLong(tls.KeySize) < 256
| summarize {logs = count(), ports = collectDistinct(dst_port), suites = collectDistinct(tls.Description)}, by: {dst_ip}
| sort dst_ip asc
```

Resultado: tres registros agregados, cada destino tiene un log y puerto 443.

| Destino privado | Cipher ID | KeySize | Suite |
|---|---:|---:|---|
| 10.0.0.2 | 47 | 128 | TLS_RSA_WITH_AES_128_CBC_SHA |
| 10.221.19.100 | 49199 | 128 | TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 |
| 10.228.182.201 | 4 | 128 | TLS_RSA_WITH_RC4_128_MD5 |

Contraste: consulta sin filtro privado ni limite devolvio 134 combinaciones de destino y suite; los tres primeros destinos privados coinciden con la tabla, con claves 128. 172.16.131.10 usa cipher 53, clave 256, excluido por el umbral estricto. La consulta final filtra los tres bloques RFC1918 y devuelve solo estos tres destinos. Se consideran servidores por dst_ip, puerto 443 y suite negociada; no confundir IP origen cliente con servidor. No usar HashFunction SHA256 como tamano de clave.

Diagnostico de consultas: fetch sobre ruta lookup no es valido; load si. Funcion ipInSubnet no disponible, sustituida por filtro explicito de bloques privados. Estos errores no consumen intentos CTF.

Candidata revisada: `10.0.0.2,10.221.19.100,10.228.182.201`, IPs separadas por comas sin espacios segun aclaracion humana de 2221. Sin envio ni pistas.

## Rechazo y comprobacion posterior

Usuario informa `me marca incorrecta`; respuesta exacta enviada y presupuesto actualizado no visibles. Preservado en intentos/001.json; no inferir consumo ni repetir envio.

Consulta de todos los destinos privados con cipher presente, sin filtro KeySize, devuelve exactamente cuatro combinaciones: las tres anteriores con 128 bits y 172.16.131.10 con cipher 53, TLS_RSA_WITH_AES_256_CBC_SHA, KeySize 256 y puerto 8080. No hay destinos privados con KeySize desconocido en este conjunto. No se observa suite privada omitida por el filtro de nulos.

Consulta adicional de origen privado y KeySize <256 devuelve numerosas IP con puertos origen altos y destino 443; estas filas son clientes, no prueban servidores adicionales. No se cambia la candidata a IPs cliente.

Contraste independiente sobre JSON original, misma ventana Last 3 days:

```dql
fetch logs
| filter vendor == "Gigamon"
| parse content, "JSON:raw"
| fieldsAdd cipher = toLong(raw[ssl_cipher_suite_id]), server = raw[dst_ip], octets = splitString(raw[dst_ip], ".")
| filter startsWith(server, "10.") or startsWith(server, "192.168.") or (startsWith(server, "172.") and toLong(octets[1]) >= 16 and toLong(octets[1]) <= 31)
| lookup [load "/lookups/tls-cipher-suites-table" | fieldsAdd cipher = toLong(NumericID)], sourceField: cipher, lookupField: cipher, prefix: "tls."
| filter toLong(tls.KeySize) < 256
| summarize {logs = count(), ports = collectDistinct(raw[dst_port]), keys = collectDistinct(tls.KeySize), ciphers = collectDistinct(cipher)}, by: {server}
| sort server asc
```

Resultado: las mismas tres IP, un log por servidor, puerto 443, clave 128, ciphers 47, 49199 y 4 respectivamente. No hay evidencia nueva para otra lista. Causa del rechazo sigue pendiente: primero contrastar respuesta exacta enviada y presupuesto actualizado. No probar permutaciones del orden o variantes con intentos limitados.

## Confirmacion exacta y trafico inverso

Captura de Submissions confirma envio exacto sin espacios: `10.0.0.2,10.221.19.100,10.228.182.201`, resultado `incorrect`, October 9th, 11:20:37 AM (zona no visible). Usuario confirma dos intentos restantes. Descartada diferencia entre candidata y texto enviado, incluido separador.

Consulta sobre origen RFC1918, cipher del lookup <256 y puerto origen <=1024, agregada con count y collectDistinct(src_ip): logs=0, sources=null. No se encontraron servidores adicionales en este criterio de trafico inverso. No prueba todos los posibles puertos de servidor, pero las fuentes privadas vistas previamente usaban puertos cliente altos y destino443.

Resultado tecnico sigue sustentado por lookup y JSON. Un orden especifico del validador o una clave incorrecta de plataforma siguen siendo hipotesis sin confirmar. Necesaria aclaracion de organizacion sobre orden o flag esperada; no proponer otro intento por permutacion.

## Segunda confirmacion y reejecucion solicitada

Pista 01/02 aportada despues por captura del usuario: filtrar registros con ssl_cipher_suite_id y agregar con summarize los servidores dst_ip y cifrado. Coste mostrado 30 puntos; descuento real no visible. Confirma el campo destino y criterio ya utilizados, sin aportar nuevos servidores ni modificar umbral. Queda sin explicar rechazo de la lista calculada. No abrir segunda pista ni enviar de nuevo automaticamente.

Usuario proporciona segunda captura: envio con espacios `10.0.0.2, 10.221.19.100, 10.228.182.201`, October 9th, 11:28:57 AM, resultado incorrect. La captura contiene tambien el primer envio: son dos intentos separados. Queda uno por limite inicial de tres. La respuesta sigue sin aceptacion; no recomendar usar el ultimo intento con los mismos datos.

Se reejecuto la consulta del JSON original con IP destino privada, lookup de cipher, key_bits <256 y agrupacion por IP/cipher/key/suite, mostrando puertos. Resultado repetido: 10.0.0.2, cipher47,128 bits; 10.221.19.100,cipher49199,128 bits; 10.228.182.201,cipher4,128 bits. Un registro y puerto443 por IP. Consulta visible en el notebook de trabajo.
