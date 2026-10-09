# 2225 — Network 08/09

Candidata: `aws-us-east-1`. No enviada; captura humana inicial: 0/3 intentos.

Entorno daa00609, copia de notebook 61fdf6c2-61b1-4890-8b73-cf88a5a51300, intervalo Last 3 days, vendor Gigamon. IP interna definida por type=private de /lookups/gigamon-ip-enriched-table. Aplicaciones exactamente bittorrent, edonkey, kazaa, gnutella y ares. Ambos extremos se expanden para atribuir cada flujo a sus dispositivos internos. Conversión toLong necesaria para bytes.

Resultado por ubicación: aws-us-east-1 86240 bytes, 2 atribuciones a 2 dispositivos; office_sao_paolo 6202 bytes, 19 atribuciones a 1 dispositivo.

Comprobación por dispositivo: 10.10.10.22 y 10.10.10.23 en aws-us-east-1 tienen cada uno 43120 bytes (1919 src + 41201 dst); 192.168.1.2 en office_sao_paolo tiene 6202 bytes (3567 src + 2635 dst). Los dos extremos privados del mismo flujo reciben atribución; incluso contando ese flujo una sola vez, aws-us-east-1 sigue primero con 43120 frente a 6202. Los nombres enviados/recibidos de la comprobación corresponden a direcciones del flujo, no a orientación individual del extremo. La suma total es independiente de esa orientación.

Consulta principal:
```dql
fetch logs
| filter vendor == "Gigamon"
| filter in(app_name, "bittorrent", "edonkey", "kazaa", "gnutella", "ares")
| fieldsAdd bytes = toLong(src_bytes) + toLong(dst_bytes), endpoint = array(src_ip, dst_ip)
| expand endpoint
| lookup [load "/lookups/gigamon-ip-enriched-table"], sourceField:endpoint, lookupField:ip, fields:{type, location}
| filter type == "private"
| summarize total_bytes = sum(bytes), registros = count(), dispositivos = countDistinctExact(endpoint), by:{location}
| sort total_bytes desc
```

Comprobación:
```dql
fetch logs
| filter vendor == "Gigamon"
| filter in(app_name, "bittorrent", "edonkey", "kazaa", "gnutella", "ares")
| fieldsAdd endpoint = array(src_ip, dst_ip)
| expand endpoint
| lookup [load "/lookups/gigamon-ip-enriched-table"], sourceField:endpoint, lookupField:ip, fields:{type, location}
| filter type == "private"
| summarize enviados = sum(toLong(src_bytes)), recibidos = sum(toLong(dst_bytes)), registros = count(), by:{location, endpoint}
| fieldsAdd total = enviados + recibidos
| sort total desc
```

Formato: ubicación exacta de la tabla. Sin abrir pistas ni enviar bandera.
