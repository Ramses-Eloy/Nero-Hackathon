# 2209 — Fallos técnicos de miembros Diamond

Candidata: `17`. No enviada.

Consulta ejecutada en la copia del notebook, intervalo Last 3 days. Resultado: 17 transacciones distintas y 29 apariciones de códigos 50xx. Se cuentan IDs distintos para evitar duplicación por varios códigos en un mismo log. Se verificó la unión: `fields: {tier}` produce `tier`, no `lookup.tier`. El campo user_id y transaction_id se contrastó con cinco logs visibles.

```dql
fetch logs
| filter log.type == "payment"
| search "[PaymentServiceThread]"
| filter contains(content, "status=\"FAIL\"")
| fieldsAdd user_id = parse(content, "DATA '<user id=\"' LD:value '\"'"), transaction_id = parse(content, "DATA ' id=\"' LD:value '\"'"), error_code = parseAll(content, "'<error code=\"' LONG:code '\"'")
| lookup [load "/lookups/payment-service-user-lookup"], sourceField: user_id, lookupField: id, fields: {tier}
| filter tier == "diamond"
| expand error_code
| filter startsWith(toString(error_code), "50")
| summarize {transactions = countDistinctExact(transaction_id), error_occurrences = count()}
```

Evidencia: [resultado](evidencias/resultado.png).

## Intento 01 y contraste

El humano envió exactamente `17`; captura confirma rechazo y 2 intentos restantes. Comprobación alternativa sin expandir errores: 13 logs execution, 1 precheck y 3 validation; 17 IDs distintos. El conteo expandido anterior da 29 apariciones 50xx, pero estas no son 29 transacciones. No proponer 29 como certeza: falta evidencia del criterio esperado. No se consumieron pistas ni se realizaron envíos desde el asistente.

```dql
fetch logs
| filter log.type == "payment"
| search "[PaymentServiceThread]"
| filter contains(content, "status=\"FAIL\"") and contains(content, "<error code=\"50")
| fieldsAdd user_id = parse(content, "DATA '<user id=\"' LD:value '\"'"), transaction_id = parse(content, "DATA ' id=\"' LD:value '\"'"), stage = parse(content, "DATA 'stage=\"' LD:value '\"'"), error_code = parseAll(content, "'<error code=\"' LONG:code '\"'")
| lookup [load "/lookups/payment-service-user-lookup"], sourceField: user_id, lookupField: id, fields: {tier}
| filter tier == "diamond"
| summarize {transactions = countDistinctExact(transaction_id), logs = count()}, by: {stage}
```

Confirmación humana: `29` aceptado. El criterio del reto cuenta filas después de expandir errores, 29 apariciones, frente a 17 IDs únicos. Aplicación limitada a 2210 que referencia este conjunto.
