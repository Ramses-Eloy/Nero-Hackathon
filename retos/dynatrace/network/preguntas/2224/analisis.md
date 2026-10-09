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
