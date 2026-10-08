# Roadmap del equipo para Hackathon Copa 2026

Guía de preparación y ejecución para cuatro integrantes, basada en los seis workshops, la agenda oficial, los tres PDF de preparación y antecedentes de otras ediciones. El objetivo es resolver los requisitos del reto, comprobar los resultados y mantener evidencia compartida para elaborar documentos, presentación y video. No incluye ideas de proyectos ni una solución anticipada.

Claude Code es el desarrollador principal de la solución. Los cuatro integrantes dirigen, analizan, verifican y comunican su trabajo. La preparación se realiza durante las horas necesarias para comprender el entorno y trabajar juntos; no se divide en plazos ni en una estrategia rígida de prioridades. Las fases son frentes flexibles que pueden solaparse o retomarse. El enunciado, los permisos y los criterios de evaluación del evento prevalecen sobre esta propuesta.

## Contexto y alcance confirmado

- La edición 2026 se centra en DevOps, APIs y observabilidad.
- La agenda de Santiago, del 8 y 9 de octubre, combina formación el primer día y competencia el segundo. Publica siete horas de desarrollo, de 9:45 a 16:45. La pestaña de Panamá, del 30 y 31 de octubre, estaba pendiente de publicación al revisar la página; no se extrapola su horario.
- Las charlas de Santiago cubren Dynatrace, infraestructura y Kubernetes, servicios, trazas, logs y DQL; el ciclo .NET, APIs, frontend, Git, Azure DevOps, Terraform y Azure; habilidades personales; seguridad de aplicaciones, experiencia de usuario y observabilidad de negocio; diagnóstico y resolución de problemas.
- Los workshops incluyen Azure, aplicaciones modernas, Git y Terraform, observabilidad con Application Insights y KQL, troubleshooting y Dynatrace. Se incluyó el workshop 4 que no estaba entre los enlaces iniciales.
- En el workshop 2 la organización anuncia accesos y créditos para las actividades. La cuenta personal y el entorno de práctica no deben confundirse con los accesos del reto.
- El workshop de Dynatrace explica que el reto utilizará un entorno específico, con restricciones al acceso de agentes externos y sin el asistente conversacional. Esto no establece una prohibición general de toda IA en todos los retos: hay que confirmar el alcance de las reglas.
- El tipo exacto de evaluación, puntos, penalizaciones, dependencias, formato de entrega y uso permitido de materiales o IA se confirma con las instrucciones del evento.

Fuentes: [agenda](https://hackathoncopa.com/agenda), [workshops](https://hackathoncopa.com/workshops), [accesos y créditos, workshop 2](https://www.youtube.com/watch?v=fy6m-dhzGhM&t=4762s), [restricciones de Dynatrace, workshop 6](https://www.youtube.com/watch?v=WV9QXQs9-Ts&t=4096s).

## Plataformas, cuentas y herramientas

| Elemento | Acceso o instalación | Uso en preparación |
|---|---|---|
| Microsoft Azure | Identidad Microsoft y acceso a una suscripción con permisos suficientes. Para práctica propia necesitan una suscripción; para el evento se anuncian accesos proporcionados. | Principal: recursos, aplicaciones, configuración y diagnóstico. |
| Microsoft Learn | Perfil gratuito para guardar progreso; documentación pública disponible sin iniciar sesión. | Referencia y formación. Un logro de formación no equivale a aprobar AZ-900. |
| GitHub | Cuenta y acceso al repositorio del equipo. Actions utiliza la misma cuenta. | Colaboración y versionado, si el equipo elige esta plataforma. |
| Azure DevOps | Acceso a una organización y proyecto cuando lo utilicen. | Preparar nociones de repositorios y pipelines: está explícitamente en la agenda. Su uso obligatorio depende del reto. |
| Dynatrace Playground y University | Una misma cuenta para ambos. Elegir Playground según la guía del estudiante. | Práctica y capacitación. |
| Dynatrace Essentials | Curso gratuito dentro de University, nueve lecciones y unas 4 h 30 min. | Formación inicial; la práctica requiere tiempo adicional. No es otra cuenta. |
| Git, Azure CLI y Terraform | Herramientas locales. El flujo local de Terraform mostrado no requiere una cuenta de HashiCorp Cloud. | Operaciones reproducibles. |
| Editor y SDK | Elegir un editor. Instalar .NET SDK si reproducen la demostración .NET o el reto lo requiere. | Ejecutar, modificar y comprobar código. |
| Node.js y otras herramientas | Instalar cuando lo necesite el frontend o una integración elegida. | Según el entorno; no instalar todas las alternativas. |

App Service, App Service Plan, Static Web Apps, Functions, Storage Account, Azure Monitor, Application Insights y Log Analytics son servicios o recursos de Azure. Entra ID y RBAC gestionan identidad y permisos; Kudu ayuda a inspeccionar App Service. No se abre una cuenta independiente por cada nombre.

KQL y DQL son lenguajes distintos: KQL se utiliza para consultar telemetría en Azure y DQL en Dynatrace. OpenTelemetry es instrumentación. OneAgent, Grail, OpenPipeline, Smartscape, dashboards, notebooks, Problems, Davis AI, LiveDebugger, AppSec y Business Events pertenecen al ecosistema Dynatrace; conocer un nombre no garantiza que la función esté habilitada en el entorno del reto.

Otros servicios y productos mencionados, como VMs, contenedores, AKS, Container Registry, redes de Azure, Docker Hub, Bitbucket, Vercel, Render, Databricks, Fabric o Foundry, sirven como ejemplos o alternativas. Solo profundizar o crear accesos cuando el reto o el laboratorio elegido lo necesite. GitHub Copilot tampoco es un requisito por usar Claude Code.

Fuentes: [workshops](https://hackathoncopa.com/workshops), [guía Dynatrace](../referencias/dynatrace-guia.pdf), [conceptos Dynatrace](../referencias/dynatrace-conceptos.pdf).

## Frentes de preparación y pruebas de salida

| Frente | Práctica útil | Prueba de salida | Registro compartido |
|---|---|---|---|
| Accesos y entorno | Comprobar herramientas, versiones, identidad, suscripción y permisos. | Cada integrante puede abrir y ejecutar el entorno que le corresponde. | Requisitos y bloqueos de acceso, sin credenciales. |
| Git y colaboración | Clonar, trabajar en ramas, integrar cambios y resolver un conflicto sencillo. | Otra persona obtiene y ejecuta los mismos cambios. | Instrucciones de ejecución y enlaces a commits. |
| Azure y aplicaciones | Comprender Resource Groups, App Service, APIs, HTTP y comunicación frontend-backend; reproducir el despliegue del taller. | Una petición se puede seguir en local y en la nube e identificar la capa que falla. | Componentes, configuración y comprobaciones. |
| DevOps y Terraform | Seguir un pipeline; practicar init, validate, plan y apply en un entorno autorizado. | Explicar un plan antes de ejecutarlo y diagnosticar permisos, configuración o cuotas. | Archivos de infraestructura, procedimiento y decisiones. |
| Observabilidad Azure | Localizar solicitudes, excepciones y dependencias; practicar filtros, ordenación y conteos con KQL. | Encontrar evidencia suficiente para justificar una conclusión. | Consulta, intervalo temporal, entorno e interpretación. |
| Diagnóstico | Practicar fallas controladas de configuración, CORS, HTTP 500 o health checks en un laboratorio. | Reproducir el fallo, corregir su causa y repetir la comprobación original. | Síntoma, hipótesis, evidencia, cambio y validación. |
| Formación Dynatrace | Avanzar en Essentials y practicar en Playground en paralelo. | Explicar los conceptos y encontrarlos en la interfaz sin seguir el video. | Progreso personal, dudas y ejercicios. |
| Investigación Dynatrace | Navegar servicios e infraestructura, seguir trazas y consultar datos con DQL. | Investigar un problema sin depender del asistente conversacional. | Consultas, relaciones, capturas y conclusiones. |
| Simulacro conjunto | Resolver ejercicios de los talleres con reloj, tareas compartidas y verificación cruzada. | Entregar resultados que otro integrante pueda comprobar. | Tiempos observados, bloqueos y mejoras. |
| Comunicación de resultados | Elaborar informe, guion de presentación y guion de video con evidencia ya validada. | Los tres materiales describen la misma versión y delimitan lo pendiente. | Entrega, guiones y evidencias seleccionadas. |

Las cápsulas de Microsoft ofrecen una progresión conceptual desde Azure y aplicaciones hasta IaC, observabilidad y diagnóstico. Se puede usar para resolver lagunas, sin obligar al equipo a estudiar en el mismo orden. El documento de Dynatrace añade el recorrido completo desde usuario hasta aplicación, infraestructura y dependencias, y la relación con impacto de negocio.

El equipo puede dedicar varias horas a comprender y desarrollar cada frente. Las comprobaciones sirven para entender los resultados y dirigir a Claude, no para imponer un calendario. Essentials mantiene la duración orientativa publicada de unas 4 h 30 min, además de práctica.

Fuentes: [cápsulas Microsoft](../referencias/microsoft.pdf), [guía Dynatrace](../referencias/dynatrace-guia.pdf), [conceptos Dynatrace](../referencias/dynatrace-conceptos.pdf).

## Organización del lead y los otros tres integrantes

El integrante 1 es el usuario: lead y coordinador durante todo el trabajo. Primero prepara con Claude la base común y sus integraciones. Cuando la base está lista, los integrantes 2 y 3 dirigen en paralelo dos frentes técnicos, utilizando a Claude como desarrollador principal. El integrante 4 comprende el reto y prepara documentación, presentación y video desde el inicio. Las tareas pueden solaparse; la base y el contexto compartido permiten que las sesiones continúen de forma coherente.

| Rol | Mientras el lead prepara la base | Después de entregar la base | Cierre |
|---|---|---|---|
| 1. Lead y coordinador: tú | Interpretar el enunciado; preparar con Claude repo, entorno, CLAUDE.md, configuración y contratos; comprobar integraciones. | Mantener contexto y decisiones compartidas, resolver bloqueos y revisar integración. | Revisar requisitos, versión final y entrega. |
| 2. Dirección técnica y análisis A | Comprender requisitos, entorno e integraciones de Claude. | Encargar a Claude el primer bloque técnico; inspeccionar cambios, comportamiento, errores y trazas; verificar resultados. | Revisar el otro frente y aportar evidencias. |
| 3. Dirección técnica y análisis B | Comprender interfaces, diseño y comprobaciones. | Encargar a Claude el segundo bloque técnico; usar skills de diseño, análisis y pruebas; comprobar integración y experiencia. | Revisar el recorrido conjunto y aportar tomas demostrativas. |
| 4. Documentación y comunicación | Comprender el reto, la arquitectura y los criterios; abrir el informe y guiones; registrar decisiones y preguntas. | Mantener el relato técnico, ordenar avances y evidencias, preparar diapositivas y recopilar grabaciones de lo que funciona. | Finalizar documento, presentación y video; comprobar que describen la versión entregada. |

API y frontend son una distribución posible, no componentes obligatorios. Si el reto es de infraestructura o investigación, adaptar los dos frentes. Claude realiza la implementación principal; los integrantes 2 y 3 aportan contexto, analizan, revisan y validan. Si utilizan varias sesiones de Claude, trabajar en ramas o worktrees separados y acordar la propiedad de archivos para evitar cambios simultáneos incompatibles.

### Entrega de la base del lead

La base está lista cuando el repo es accesible, Claude puede leer el contexto del proyecto, el entorno relevante se puede ejecutar o inspeccionar, las interfaces y configuración están definidas y las integraciones necesarias están comprobadas. Si el entorno lo proporciona la organización, inspeccionarlo y documentarlo; no recrearlo innecesariamente. No hace falta terminar la aplicación antes de delegar.

Los integrantes 2 y 3 confirman que pueden continuar desde esa base. El integrante 4 recibe una explicación breve del recorrido y de lo pendiente. La entrega incluye README, commit o versión, criterios de aceptación y tareas siguientes.

### Análisis, diseño y skills de Claude

El kit incorpora ocho skills de proyecto para Claude: incorporar-contexto, analizar, disenar, implementar, verificar, gestionar-incidencias, revisar-deuda y documentar. Son instrucciones compartidas redactadas para este flujo, no plugins oficiales ni una instalación global. CLAUDE.md conserva las reglas comunes; las skills se invocan para tareas concretas. Registrar hallazgos y comprobaciones en el repo. Azure cuenta además con un plugin que reúne MCP, agentes y skills según la integración documentada. El acceso externo a Dynatrace continúa sujeto a las restricciones del reto.

### Coordinación y evidencia

El lead conserva la coordinación. Los integrantes 2 y 3 pueden revisar cambios entre sí. El integrante 4 organiza los materiales y puede pedir a Claude borradores basados en evidencias; los responsables técnicos comprueban las afirmaciones. Mantener un registro compartido del contexto y de los archivos que modifica cada sesión.

La distribución detallada está en [roles y tareas](roles.md). La imagen del flujo está en [roadmap del equipo](../roadmap-flujo-claude.png).

## Método para resolver los retos

1. Leer el enunciado y la evaluación antes de actuar: resultado solicitado, formato, permisos, restricciones, dependencias y comprobación esperada.
2. Inspeccionar el estado inicial y reproducir el problema cuando exista. Registrar qué funciona y qué falla.
3. Definir frentes con responsable, sesión o rama de Claude y verificador. Comunicar dependencias y criterios de aceptación.
4. Formular una hipótesis a partir de evidencia. Hacer un cambio acotado y repetir la comprobación.
5. Verificar entre compañeros. Un comando ejecutado o un pipeline exitoso no demuestra por sí solo que el requisito se cumpla.
6. Registrar y entregar conforme se completa cada resultado. Confirmar recepción o aceptación cuando exista ese mecanismo.

Los criterios de evaluación determinan qué debe comprobarse y entregarse. No asumir puntos parciales ni formato CTF en 2026. El trabajo se organiza alrededor de comprensión compartida, integraciones funcionales e implementación verificable, sin un cálculo de prioridades por minuto.

Ante un bloqueo, compartir objetivo, error, contexto, pasos realizados y evidencia con otro integrante, Claude o el mentor adecuado. No se fija un tiempo obligatorio para cambiar de tarea. La siguiente acción debe responder a una hipótesis comprobable.

Mantener resultados verificables durante el desarrollo. Reservar margen de cierre para comprobar la entrega y evitar cambios amplios al final. La distribución exacta depende del reto, no de una agenda rígida inventada por el equipo.

## Repositorio y documentación continua

Este kit contiene documentos vacíos y referencias; no contiene una implementación ni presupone el enunciado. Se puede subir al repositorio que el equipo elija, respetando las reglas sobre material previo.

| Archivo | Función |
|---|---|
| README.md | Entrada al trabajo: objetivo, ejecución, estructura y enlaces. |
| docs/roadmap.md | Guía consolidada de preparación y ejecución. |
| CLAUDE.md | Contexto breve y reglas para Claude como desarrollador principal. |
| .claude/skills/ | Skills compartidas de análisis, diseño, implementación, verificación y documentación. |
| .mcp.example.json | Ejemplo de conexión sin secretos; no activa servidores por sí solo. |
| docs/integraciones-claude.md | Integraciones, requisitos y comprobaciones para Claude. |
| docs/preparacion.md | Matriz de habilidades de los cuatro integrantes. |
| docs/tareas.md | Tareas, requisitos, responsables, verificadores, dependencias y estado. |
| docs/avances.md | Registro breve de hitos y bloqueos con enlaces a cambios y evidencias. |
| docs/decisiones.md | Decisiones relevantes y sus motivos. |
| docs/evidencias.md | Índice de comprobaciones y su relación con requisitos. |
| docs/entrega.md | Informe final y comprobación de entregables. |
| presentacion/guion.md | Orden de exposición basado en resultados. |
| video/guion.md | Recorrido grabado, escenas y evidencias. |
| referencias/ | Los tres PDF originales, sin modificaciones. |

Separar estados de trabajo de dominio personal. Las tareas pueden estar pendientes, en curso, bloqueadas, por verificar, verificadas o entregadas. Para preparación, registrar si cada persona ha estudiado, practicado y demostrado una habilidad. Entregado no significa aceptado: anotar el resultado del evaluador por separado cuando exista.

Actualizar al cerrar un avance importante, encontrar un bloqueo o tomar una decisión. Evitar narrar cada comando. Enlaces a commits, consultas y evidencias permiten reconstruir el trabajo. Para reducir conflictos, usar entradas cortas y acordar quién actualiza la tabla compartida si varios trabajan al mismo tiempo.

Las evidencias deben identificar requisito, entorno, fecha o intervalo temporal, pasos y conclusión. Registrar nombres y finalidad de variables, sin valores secretos. Excluir credenciales, archivos de estado de Terraform y datos restringidos del repositorio compartido.

## Documentos, presentación y video

Prepararlos durante el desarrollo, usando como fuente las tareas verificadas y el índice de evidencias. Guardar una captura o grabación breve cuando una operación funciona, siempre que esté permitida y sea adecuada para compartir. El informe explica; las diapositivas seleccionan; el video demuestra. Los tres deben corresponder a la misma versión del trabajo.

Recorrido sugerido: requisito, solución o corrección, comprobación, resultado y limitaciones. Documentar también qué aportó cada integrante. Definir el formato, duración y canales finales con las instrucciones oficiales. Una grabación de respaldo no sustituye una validación en vivo o una entrega exigida por la organización.

No hace falta cerrar las diapositivas antes de tener resultados. Sí conviene definir el guion y reunir evidencias desde temprano, dejando el montaje y la edición para cuando el recorrido esté comprobado.

## Claude Code como desarrollador principal

Claude debe tener acceso al repo, a las herramientas locales y al contexto técnico. Git, SDK, herramientas de pruebas y Terraform se pueden ejecutar desde terminal; no necesitan MCP. Las conexiones externas complementan ese acceso: GitHub o Azure DevOps para colaboración y pipelines, Azure CLI y Azure MCP para recursos, Microsoft Learn MCP para documentación y Playwright MCP para navegación y comprobaciones de interfaz cuando exista frontend.

La guía [integraciones con Claude](integraciones-claude.md) explica requisitos y pruebas de conexión. CLAUDE.md y las skills comparten la forma de trabajo entre sesiones; no sustituyen la configuración de permisos ni la autenticación. Registrar cada encargo con objetivo, contexto, archivos o recursos implicados, criterio de aceptación y evidencia requerida. Claude implementa; el equipo valida y comunica.

No conectar agentes al Dynatrace del reto por cuenta propia; seguir los accesos y restricciones comunicados. La guía estudiantil es de registro y capacitación, no una autorización para integración externa.

Referencias técnicas: [MCP en Claude Code](https://code.claude.com/docs/en/mcp), [skills](https://code.claude.com/docs/en/skills), [CLAUDE.md](https://code.claude.com/docs/en/memory), [GitHub MCP](https://github.com/github/github-mcp-server), [Azure MCP](https://github.com/microsoft/mcp/blob/main/servers/Azure.Mcp.Server/README.md), [Azure DevOps MCP](https://learn.microsoft.com/en-us/azure/devops/mcp-server/mcp-server-overview?view=azure-devops), [Microsoft Learn MCP](https://learn.microsoft.com/en-us/training/support/mcp), [Playwright MCP](https://github.com/microsoft/playwright-mcp), [Dynatrace MCP](https://docs.dynatrace.com/docs/dynatrace-intelligence/dynatrace-mcp).

## Lecciones de ediciones pasadas y foros

En 2024 Copa se enfocó en Linux. En 2025 un organizador describe dos retos simultáneos, uno con SageMaker Canvas y otro con Databricks, y un sistema de calificación CTF. El antecedente favorece ensayar distribución y validación; no predice las tecnologías, la puntuación o los retos de 2026. Un integrante del equipo ganador de 2025 describe el trabajo conjunto y uso de las herramientas de esa edición.

Los testimonios de Reddit son experiencias particulares, no evidencia de una estrategia universal. Se aprovechan lecciones sobre coordinación, código reproducible, bloqueos y entrega, sin trasladar consejos de presentación o prototipos incompletos a una evaluación técnica que pudiera exigir resultados exactos.

Fuentes: [Copa 2024](https://ciudaddelsaber.org/noticias/hackathon-copa-airlines-2024-1), [organización Copa 2025](https://es.linkedin.com/posts/hugoaquino_hackathoncopa-ciudaddelsaber-aws-activity-7382840993420853248-40FC), [equipo ganador Copa 2025](https://www.linkedin.com/posts/wilfredo-cano_hackathoncopa2025-aws-databricks-activity-7380707660301754368-PyqY), [fallos de coordinación y entrega en Reddit](https://www.reddit.com/r/hackathon/comments/1rbq3qx/my_first_ever_online_hackathon_experience_was_an/), [gestión del tiempo en Reddit](https://www.reddit.com/r/csMajors/comments/17irlcq/any_tips_for_hackathon/).

## Criterio de preparación y de cierre

Preparación: comprender el entorno y poder dirigir, diagnosticar y comprobar el trabajo de Claude. Cierre de una tarea: cumplir el requisito, comprobarlo con otra persona, registrar la evidencia y completar la entrega requerida.

## Contexto vivo, errores y deuda durante todo el recorrido

El [protocolo completo](contexto-equipo-claude.md) convierte esta trayectoria en instrucciones para cada sesión de Claude. `features/` recibe pruebas, documentos, diseños y material por analizar a medida que se desarrolla. Claude revisa su [índice](../features/INDEX.md) al comenzar/retomar, al recibir material anunciado y antes de integrar o entregar; incorpora lo relevante a tareas, decisiones y comprobaciones. No se incluye un observador automático.

Errores y deuda se mantienen visibles en [incidencias](incidencias.md) y [deuda técnica](deuda-tecnica.md). Un error observado se reproduce e investiga, se corrige y se comprueba. Un atajo se documenta con impacto y criterio de resolución. Solo después de resolver y verificar se marca el check y se tacha el título; lo aplazado sigue abierto. Antes de entregar se revisan pendientes que afecten al reto, demo o documentación.

La [imagen con flechas](../roadmap-flujo-claude.png) muestra el handoff de la base hacia los frentes A/B, la documentación paralela desde el inicio y el retorno de errores y material nuevo al desarrollo. El [catálogo de herramientas y skills](herramientas-diseno-skills.md) permite elegir apoyos por fase sin imponer otro stack.
