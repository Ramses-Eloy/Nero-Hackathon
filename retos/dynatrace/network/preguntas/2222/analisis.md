# 2222 — Aplicaciones personales

Candidata: `7`, no enviada. Intervalo Last 3 days. IP 172.16.133.66 tiene 25 logs, todos como src_ip, y ocho app_name: amazon-aws, scorecardresearch, facebook, bing, gmail, linkedin, twitter, https. Se interpreta uso personal como aplicaciones fuera de amazon-aws conforme al contexto del notebook (trabajo esperado en AWS). Al excluir amazon-aws quedan 19 logs y siete nombres, tanto countDistinct como countDistinctExact. HTTPS y scorecardresearch se mantienen: son categorías de aplicación observadas; no se deduplican contra Gmail o LinkedIn. Límite: clasificación por exclusión de AWS, no una etiqueta explícita de personal. Los detalles HTTP muestran incluso tráfico AWS a cdn.printfriendly.com con referer skinnytaste, por lo que uso real y app_name no son equivalentes; la candidata sigue el criterio de nombres del ejercicio.

```dql
fetch logs
| filter vendor == "Gigamon"
| filter src_ip == "172.16.133.66" or dst_ip == "172.16.133.66"
| filter app_name != "amazon-aws"
| summarize {personal_apps = countDistinct(app_name), exact_apps = countDistinctExact(app_name), logs = count()}
```

El humano confirmó expresamente que 7 fue aceptado.
