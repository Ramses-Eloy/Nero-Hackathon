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
