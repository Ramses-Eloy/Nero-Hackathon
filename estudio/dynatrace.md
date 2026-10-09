# Dynatrace: guía de estudio para CTF

## Alcance y acceso de práctica

Base: workshop 6, [guía del estudiante](../referencias/dynatrace-guia.pdf), 14 páginas, y [conceptos de observabilidad](../referencias/dynatrace-conceptos.pdf), 4 páginas. El temario describe capacidades; no garantiza que estén todas activadas en competencia.

La guía recorre Playground → University → Essentials con una misma cuenta. Essentials tiene nueve lecciones y unas 4 h 30 min orientativas; practicar necesita tiempo adicional. Playground contiene ejemplos, no respuestas de competencia. Confirmar el entorno del equipo al recibirlo y no trasladar valores del laboratorio.

I3 se enfoca inicialmente en servicios/trazas/logs/DQL; I4 en infraestructura/relaciones/experiencia y capacidades complementarias. Ambos deben poder revisar preguntas del otro. El usuario confirmó uso de IA permitido: disponibilidad de datos, conexiones y capacidades se comprueba en el entorno real.

## 1. Señales y contexto

Métricas: CPU, latencia, errores y otras cantidades. Logs: eventos y mensajes. Trazas: recorrido de transacciones por servicios/dependencias. Elegir señal según la pregunta: una gráfica agregada no responde necesariamente qué ocurrió en una transacción individual.

Registrar ambiente, entidad/ID, intervalo y unidad. Diferenciar host, proceso, servicio, endpoint, solicitud y sesión de usuario. Un nombre visible puede no ser único; si se pide ID, recuperar ID. El glosario ayuda a identificar términos del producto. [Glosario oficial](https://docs.dynatrace.com/docs/discover-dynatrace/get-started/glossary).

## 2. Navegación y búsqueda de evidencia

Reconocer las aplicaciones y vistas realmente habilitadas: servicios, infraestructura, problemas, exploración de datos, dashboards/notebooks y experiencia. Los nombres/menús pueden variar; estudiar capacidad, filtros y relaciones antes de memorizar posiciones.

Cambiar primero a la ventana correcta. Comprobar zona horaria y filtros heredados. Si faltan datos, revisar alcance, permisos e ingestión antes de concluir que no hubo eventos. No modificar instrumentación para preguntas de identificación si basta otra fuente disponible.

Practicar: localizar entidad desde una pregunta y seguir relaciones hasta el componente pertinente. Guardar ruta conceptual y evidencia con timestamp/intervalo.

## 3. Servicios, solicitudes y trazas

APM ayuda a entender aplicaciones y APIs. Inspeccionar respuesta, errores, volumen y dependencias en el intervalo pedido. Un servicio afectado no es automáticamente el origen del fallo: seguir la transacción y contrastar con registros o configuración.

Para una solicitud lenta, estudiar dónde se consume tiempo y qué llamadas dependen de ella. Diferenciar duración total, tiempo propio, llamada externa y agregación sobre varias solicitudes. Si se pide la más lenta, verificar alcance y criterio; una muestra no garantiza el máximo global.

Ejercicios: seguir una transacción a otra API/base de datos; distinguir capa que muestra el error de la que lo produce; explicar qué evidencia permite decidir entre dos componentes.

## 4. Infraestructura y Kubernetes

La observabilidad end-to-end del PDF conecta usuario, aplicación, infraestructura, red y base de datos. Reconocer hosts, procesos, contenedores y relaciones con servicios. Cuando haya Kubernetes, ubicar clúster/namespace/workload/pod y comprender qué representa cada nivel.

CPU alta, reinicios o memoria elevada son observaciones; correlacionarlas temporalmente con tráfico/errores antes de atribuir causa. No confundir una instancia con todo el servicio ni asumir que cada pod contiene el mismo intervalo de datos.

Smartscape/relaciones permiten entender dependencias según las capacidades disponibles. Practicar encontrar quién depende de quién y qué alcance tiene un problema; un mapa orienta la investigación, no sustituye la comprobación del dato pedido.

## 5. Logs y DQL

DQL es el lenguaje de Dynatrace para explorar datos del ecosistema Grail; no es KQL. Entender origen de datos, registros, campos, filtros, proyección, ordenación, límite y agregación. Primero inspeccionar campos reales y tipos; después construir la consulta mínima. [Referencia DQL](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/dql-reference).

En Notebooks/Dashboards, registrar consulta y rango temporal. No asumir que un campo existe en todo dataset o que todas las trazas/logs están ingeridas. Consulta válida con cero resultados puede indicar ventana, filtro, acceso o fuente equivocados.

`fetch` selecciona fuente; `filter` restringe; `sort` ordena; `limit` limita filas; `summarize` agrega. Estudiar comandos en referencias y practicar primero sobre datos simples. [Fuentes](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/data-source-commands), [filtros](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/filtering-commands), [agregación](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands).

Ver [scripts-consultas.md](scripts-consultas.md). No copiar operadores KQL esperando igual sintaxis ni contar una muestra como totalidad.

## 6. Problemas y diagnóstico

La correlación automática puede señalar componentes y causas, pero el equipo debe comprobar alcance, tiempo y evidencia que responde a la pregunta. No confundir alerta, problema, impacto y causa raíz. Si el reto da un problema concreto, abrir su contexto antes de investigar indiscriminadamente otros.

Recorrido: síntoma → entidad → intervalo → transacción/relación → evidencia complementaria → hipótesis → comprobación. Si la plataforma permite corrección, cambiar lo requerido y volver a verificar; si pide identificación, entregar el dato sin alterar el entorno.

## 7. Experiencia de usuario y negocio

RUM observa experiencia de usuarios reales. Distinguir página/acción, sesión, error frontend y backend. Synthetic, si está presente, comprueba recorridos simulados: no es una sesión real. El PDF relaciona experiencia con dependencias de aplicación e infraestructura.

Business Events conecta eventos operativos con resultados de negocio. Si se pide conteo/impacto, precisar evento, intervalo, entidad y posibles duplicados; no convertir tráfico técnico automáticamente en compras/usuarios sin definir relación.

Ejercicio: correlacionar una acción afectada con petición/dependencia y explicar qué se sabe del impacto, sin inventar una métrica económica.

## 8. LiveDebugger y AppSec

El PDF introduce inspección en vivo, seguridad de aplicaciones y eventos de negocio. Saber para qué sirven y qué evidencia generan. Disponibilidad, instrumentación y permisos reales se comprueban; no tomar una simplificación del PDF como garantía universal de que no habrá configuración adicional.

LiveDebugger puede ayudar a inspeccionar el comportamiento donde esté habilitado. AppSec orienta sobre vulnerabilidades/amenazas de aplicación según capacidades. Diferenciar hallazgo de seguridad de error funcional; no usar herramientas de ataque ni explorar sistemas ajenos al alcance del reto.

## Comprobación de aprendizaje

I3 e I4 deben localizar entidad/ventana, seguir transacción/relaciones, consultar logs con DQL y explicar evidencia al compañero. Practicar diagnósticos que incluyan hipótesis alternativas y unidades. Las respuestas del CTF se obtendrán en su entorno, nunca por valores memorizados del Playground.
