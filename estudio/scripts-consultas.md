# Scripts y consultas: ejemplos de estudio

Ejemplos ilustrativos, no ejecutados contra competencia y sin resultados/flags reales. Adaptar recursos, esquema, runtime y ventana. Antes de ejecutar scripts entregados, leer entradas, permisos, efectos, dependencias y manejo de errores. Un comando de diagnóstico y una modificación del entorno no tienen el mismo impacto.

## Azure CLI: alcance primero

```powershell
az account show --query "{tenant:tenantId,subscription:id,name:name}" -o json
az group list --query "[].{name:name,location:location}" -o table
az webapp list --query "[].{name:name,group:resourceGroup,state:state}" -o table
```

Estos comandos dependen de autenticación/permisos y no verifican la pregunta por sí solos. No seleccionar otra suscripción automáticamente. Para configuración, evitar sacar todos los secretos:

```powershell
az webapp config appsettings list --resource-group GRUPO --name APP --query "[].name" -o json
```

[Cuenta Azure](https://learn.microsoft.com/en-us/cli/azure/account?view=azure-cli-latest), [app settings](https://learn.microsoft.com/en-us/azure/app-service/configure-common).

## HTTP desde Windows/PowerShell

```powershell
curl.exe --silent --show-error --max-time 10 --output NUL --write-out "%{http_code}" "https://HOST-AUTORIZADO/RUTA"
```

Sustituir host/ruta; ejemplo para observar estado sin guardar cuerpo. No adjuntar tokens al código compartido. Una petición fuera del navegador no reproduce toda la política CORS. Revisar método, Origin y preflight en DevTools cuando corresponda. Scripts que envían formularios o modifican datos requieren alcance conocido.

## .NET y Terraform

Leer proyecto/runtime antes de escoger dotnet restore/build/test/run; registrar el comando real y su salida. No ejecutar código entregado sin inspeccionarlo. Node/Python/PowerShell se utilizan si el entorno los trae, no como stack asumido.

Terraform: leer archivos/variables/proveedor/workspace antes de init, validate y plan. Apply/destroy no son diagnósticos de lectura. Un plan puede consultar el entorno; no subir estado, planes o valores secretos. [CLI .NET](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet), [plan](https://developer.hashicorp.com/terraform/cli/commands/plan).

## KQL: identificar esquema

Ejemplo sobre tablas Log Analytics; adaptar si el scope muestra requests/exceptions/dependencies en lugar de AppRequests/AppExceptions/AppDependencies.

```kusto
AppRequests
| where TimeGenerated >= ago(30m)
| project TimeGenerated, Name, ResultCode, Success, DurationMs, OperationId
| order by TimeGenerated desc
| take 20
```

Es una muestra. Para contar sobre la ventana completa, quitar el límite antes de agregar:

```kusto
AppRequests
| where TimeGenerated >= ago(30m)
| where Success == false
| summarize fallos=count() by Name, ResultCode
| order by fallos desc
```

Para correlacionar, recuperar OperationId de una solicitud y filtrar excepciones/dependencias con ese valor, validando los campos disponibles. Si el enunciado da una ventana absoluta usarla; `ago(30m)` cambia al pasar el tiempo. Las duraciones/campos del esquema alternativo pueden usar tipos diferentes: verificar conversión/unidad antes de contestar.

[KQL](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/get-started-queries), [modelo Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/data-model-complete).

## DQL: muestra, filtro y conteo

Fijar rango temporal pertinente en el entorno e inspeccionar campos:

```dql
fetch logs
| sort timestamp desc
| limit 20
```

Ejemplo si content existe:

```dql
fetch logs
| filter contains(content, "error")
| fields timestamp, content
| sort timestamp desc
| limit 20
```

La búsqueda de una cadena no equivale a todos los eventos de error. Para contar registros de la fuente/ventana consultada:

```dql
fetch logs
| summarize cantidad = count()
```

No afirmar totalidad si hay límites de escaneo, datos no ingeridos o acceso parcial. Para agrupar por severidad/entidad validar nombre/tipo del campo; no inventar `service` u otro campo por analogía con KQL. [DQL fuentes](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/data-source-commands), [filtros](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/filtering-commands), [agregación](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands).

## Leer scripts recibidos en el CTF

Identificar: objetivo, parámetros, variables, archivos que lee/escribe, endpoints, autenticación, dependencias, loops, manejo de error y efectos remotos. Distinguir ejecución fallida de resultado válido sin datos. No solucionar un script que consulta un scope incorrecto dando permisos mayores por defecto. Guardar script original, diagnóstico, cambio acotado y comprobación si el reto pide corregirlo.
