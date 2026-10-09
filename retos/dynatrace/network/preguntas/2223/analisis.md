# 2223 — Bytes de tráfico personal

Candidata: `123692`, no enviada. Continúa el alcance de 2222: IP 172.16.133.66, aplicaciones distintas de amazon-aws. Ventana Last 3 days. 19 logs, siete apps, ningún src_bytes/dst_bytes faltante tras conversión a long. Enviados 57922, recibidos 65770, total 123692 bytes. Se interpreta tráfico generado como volumen bidireccional; si se pidieran bytes enviados exclusivamente serían 57922. Comprobación independiente por sumas por aplicación: bing 3124 + facebook 33418 + gmail 8842 + https 8778 + linkedin 14438 + scorecardresearch 40888 + twitter 14204 =123692. Incluyendo AWS total204700 (AWS81008), excluido por continuidad con pregunta anterior.

```dql
fetch logs
| filter vendor == "Gigamon"
| filter src_ip == "172.16.133.66" or dst_ip == "172.16.133.66"
| filter app_name != "amazon-aws"
| fieldsAdd sent = toLong(src_bytes), received = toLong(dst_bytes)
| summarize {logs = count(), apps = countDistinct(app_name), missing_bytes = countIf(isNull(sent) or isNull(received)), sent_bytes = sum(sent), received_bytes = sum(received), total_bytes = sum(sent + received)}
```

## Revisión tras rechazo

123692 rechazado, dos intentos restantes. La captura pide bytes de tráfico de la IP; no limita a aplicaciones personales. La candidata anterior añadió la exclusión de AWS desde 2222. Se corrige ese alcance: 25 logs, cero valores faltantes, enviados 82894 + recibidos 121806 =204700. Contraste: 123692 personal +81008 AWS =204700. Nueva candidata `204700`, no enviada ni aceptada aún.

```dql
fetch logs
| filter vendor == "Gigamon"
| filter src_ip == "172.16.133.66" or dst_ip == "172.16.133.66"
| fieldsAdd sent = toLong(src_bytes), received = toLong(dst_bytes)
| summarize {logs = count(), missing_bytes = countIf(isNull(sent) or isNull(received)), sent_bytes = sum(sent), received_bytes = sum(received), total_bytes = sum(sent + received)}
```

## Segundo rechazo
El humano confirma rechazo de 204700. Se conservan ambos envíos. El presupuesto restante no fue mostrado en esta confirmación. Ambos volúmenes bidireccionales fueron rechazados. Los bytes enviados ya comprobados son 57922 excluyendo AWS y 82894 incluyendo AWS. Falta confirmar si 7 fue aceptado en 2222 para resolver el alcance de aplicaciones personales antes de una nueva candidata; no realizar envíos automáticos.

## Alcance confirmado y nueva candidata
El humano confirmó aceptación de 7 en 2222. Se mantiene el conjunto de aplicaciones personales fuera de AWS. Nueva candidata: 57922, bytes enviados (src_bytes), comprobados por la consulta registrada y por suma por aplicación: 2302+5694+7130+5682+3648+29114+4352=57922. Interpretación de generó como bytes enviados, dado el rechazo del total bidireccional personal. No enviada ni aceptada todavía.

## Cierre por agotamiento
Captura confirma 57922 rechazado, 3/3 intentos, cero restantes. Se conservan los tres envíos incorrectos: 123692, 204700, 57922. La respuesta correcta queda desconocida. No inferir aceptación de otro valor ni investigar nuevas candidatas al pasar a la siguiente por instrucción humana. Lección: las interpretaciones de alcance y dirección no quedaron confirmadas por el validador; el resultado de 2222 no bastaba para resolver esa ambigüedad.
