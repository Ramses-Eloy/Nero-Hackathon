# Microsoft: guía de estudio para CTF

## Alcance

Base: workshops 1–5 y [cápsulas Microsoft](../referencias/microsoft.pdf), 18 páginas. Es un mapa de conocimientos para resolver preguntas sobre el entorno entregado. No confirma que cada servicio aparezca en los retos. Las cápsulas cubren 17 temas desde Azure hasta diagnóstico; la práctica debe recorrerlos, no limitarse a leer sus definiciones.

## 1. Azure, identidad y organización

Azure es la plataforma; una suscripción delimita recursos y acceso administrativo; un Resource Group agrupa recursos relacionados. Distinguir cuenta/identidad, directorio/tenant, suscripción, grupo y recurso. Los permisos se aplican a un alcance: que un recurso no sea visible no demuestra que no exista.

Aprender a encontrar nombre e ID, tipo, región, grupo, estado, etiquetas y dependencias. Comprobar que se está en el entorno del equipo, no en una suscripción personal. Para responder un nombre conservar el valor visible exacto; para ID no sustituirlo por un alias.

Practicar: localizar la aplicación, su grupo y su plan; explicar qué relación existe. I1 profundiza aquí; I2 debe saber revisar alcance y configuración.

## 2. App Service y configuración

App Service ejecuta apps web/APIs en una plataforma administrada. El plan es una pieza distinta de la aplicación. Conocer runtime, despliegue, hostname, configuración y registros. No asumir que arrancar correctamente garantiza que todos los endpoints funcionan.

Variables de configuración, conexiones, URL del backend y parámetros de instrumentación influyen en el comportamiento sin cambiar necesariamente el código. Un fallo local vs nube puede revelar diferencias de entorno. No inspeccionar/copiar todos los valores cuando basta el nombre o presencia de una variable.

En App Service los app settings llegan como variables de entorno; modificarlos puede reiniciar la aplicación. Por eso investigar antes de cambiar y comprobar impacto en otras preguntas que usan el mismo entorno. [Configuración oficial](https://learn.microsoft.com/en-us/azure/app-service/configure-common).

Servicios complementarios mencionados en la preparación: App Service Plan, Static Web Apps, Functions, Storage, Azure Monitor, Log Analytics y Application Insights. Identificar función y relación, no crear recursos por defecto. Entra ID/RBAC son identidad/permisos; Kudu es una vía de diagnóstico de App Service cuando esté disponible. VMs, contenedores, AKS, Container Registry, redes, Key Vault u otros servicios se estudian en detalle si el entorno/enunciado los requiere; no están todos confirmados como retos.

## 3. APIs, HTTP y backend

API describe una interfaz de intercambio. Entender endpoint, método, cabeceras, cuerpo, parámetros, código de estado y contrato JSON. Distinguir autenticación/autorización, dato faltante, ruta incorrecta y excepción interna. Un código 500 es un síntoma; investigar mensaje/traza/dependencia para identificar origen.

Estudiar GET/POST/PUT/PATCH/DELETE, estados 2xx/4xx/5xx y la diferencia entre error HTTP y petición que ni llegó a ejecutarse. Una petición de lectura puede observar comportamiento; peticiones que modifican datos requieren entender alcance y efectos.

Si hay .NET: ubicar arranque/rutas, configuración, inyección de dependencias, middleware y manejo de excepciones. Saber leer archivos entregados y distinguir restaurar dependencias, compilar, probar y ejecutar. No asumir que .NET será el único stack. [CLI de .NET](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet).

Preguntas a practicar: dónde se produce el fallo, qué configuración utiliza, qué dependencia respondió mal y qué evidencia diferencia dos causas posibles. El nombre de una excepción no demuestra por sí solo la causa raíz.

## 4. Frontend e integración

Frontend es la interfaz del usuario; backend procesa lógica/datos. Seguir navegador → petición HTTP → API → dependencia → respuesta. Usar Network y Console para localizar URL, método, estado, cuerpo permitido y error. Evitar confundir un fallo visual con una API caída.

CORS regula llamadas desde navegador entre orígenes. Origin incluye esquema, host y puerto. Una petición que funciona con un cliente HTTP puede fallar en navegador por política de origen; eso no significa que la política sea la única causa. Identificar petición real y preflight cuando exista, origen esperado y configuración aplicada. [Tutorial API/CORS](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-rest-api).

No resolverlo cambiando a un origen wildcard de forma automática. Si el reto exige corregir, hacer el cambio pertinente y repetir la comprobación que fallaba. Comprobar URL de API, variables del frontend, formato de respuesta y configuración de despliegue antes de tocar diseño.

## 5. DevOps, Git y pipelines

DevOps conecta desarrollo y operaciones; Git conserva versiones. Poder identificar rama, commit, diff, archivo cambiado y versión desplegada. Un repo correcto no demuestra que el entorno esté ejecutando esa versión. No confundir GitHub, Azure DevOps y sus sistemas de pipelines.

En un pipeline distinguir trigger, agente, etapa/job, tarea, artefacto y despliegue. Buscar la primera falla relevante y su contexto, no solo la última línea roja. Separar error de build/test, permisos, variable/conexión faltante y despliegue. Los pipelines automatizan integración/entrega; no garantizan comportamiento funcional. [Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines?view=azure-devops).

Practicar lectura de YAML y logs: qué se ejecutó, en qué orden, qué entrada usó, qué código de salida devolvió y qué artefacto produjo. No volver a ejecutar un pipeline que modifica el entorno sin comprobar la tarea y su autorización.

## 6. Terraform e IaC

IaC expresa infraestructura en archivos. Terraform incluye proveedor, recursos, variables, outputs y estado. Estudiar init/validate/plan/apply y distinguir configuración declarada de estado real. No subir tfstate, planes ni secretos.

Un plan muestra cambios propuestos; no los aplica. Leer creación, actualización o eliminación y verificar workspace/variables/proveedor antes de ejecutar una modificación. Un plan puede consultar/refrescar datos y necesita acceso apropiado; no confundirlo con un comando puramente textual. [Referencia de plan](https://developer.hashicorp.com/terraform/cli/commands/plan).

Para preguntas: ubicar recurso, atributo, variable o referencia causal. Si un valor depende del entorno, inspeccionarlo; no adivinarlo a partir de un ejemplo del taller.

## 7. Observabilidad, logs y Application Insights

Las cápsulas distinguen observabilidad y señales para entender estado y fallos. Métrica cuantifica, log registra y traza sigue recorrido. Conectar solicitud, excepción y dependencia; registrar intervalo y operación, no solo una captura sin contexto.

Diagnóstico de App Service distingue registros de aplicación y despliegue; otras opciones dependen de sistema operativo/configuración. Elegir la fuente pertinente al síntoma. [Logs de App Service](https://learn.microsoft.com/en-us/azure/app-service/troubleshoot-diagnostic-logs).

Application Insights/Log Analytics pueden mostrar nombres distintos: requests/AppRequests, dependencies/AppDependencies, exceptions/AppExceptions y traces/AppTraces. No copiar una consulta entre esquemas sin adaptar campos; traces contiene logs de aplicación, mientras solicitudes/dependencias representan spans. [Modelo de telemetría](https://learn.microsoft.com/en-us/azure/azure-monitor/app/data-model-complete).

## 8. KQL

Leer esquema primero. Dominar selección de tabla, where, project, order by, take, summarize y agregaciones; después correlación/join cuando se necesite. Nombres de tablas/columnas y operadores requieren sintaxis exacta. `take` muestra una muestra, no un conteo total. Registrar ventana, filtros y unidades; una ventana incorrecta cambia una respuesta aunque la consulta sea válida. [Introducción KQL](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/get-started-queries).

Ver ejemplos adaptables en [scripts-consultas.md](scripts-consultas.md). Practicar obtener conteo, error predominante, solicitud lenta y su dependencia. No inventar un resultado si no hay datos o permiso.

## 9. Health checks y pensamiento diagnóstico

Un health check comprueba una condición definida; no prueba toda la aplicación. Distinguir respuesta del endpoint de salud y recorrido funcional que pregunta el reto. Comprobar configuración, runtime, disponibilidad y dependencias.

Método: describir síntoma → delimitar alcance → elegir hipótesis → reunir evidencia → comprobar → corregir si corresponde → repetir prueba. Cambiar una cosa justificable, preservar evidencia inicial y registrar efecto. No reiniciar/redeployar todo para ocultar un fallo antes de entenderlo.

## Comprobación de aprendizaje

I1 e I2 deben poder obtener evidencia del entorno y explicársela al otro, leer un script antes de ejecutarlo, diagnosticar HTTP/CORS/configuración, seguir un pipeline/plan y adaptar una consulta KQL. Los ejercicios son de laboratorio, no preguntas reales ni predicciones de flags. Ampliar esta guía cuando se entregue el stack y los retos.
