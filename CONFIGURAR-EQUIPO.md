# Preparación de los cuatro equipos de trabajo para mañana

Checklist para I1–I2 (Microsoft) e I3–I4 (Dynatrace), preparado el 8 de octubre de 2026, America/Bogota. «Mañana» corresponde al 9 de octubre; no confirma una fecha oficial del evento. El kit está publicado, pero el acceso y las herramientas de cada computadora deben comprobarse localmente.

## 1. Todos: cuentas, acceso y checkout propio

- [ ] Cuenta personal de GitHub; aceptar invitación de colaborador si hace falta. El propietario verifica que los cuatro tengan escritura en Nero-Hackathon.
- [ ] Iniciar sesión en Claude y Codex con las cuentas/planes que usarán; comprobar acceso a los modelos disponibles y capacidad suficiente para la jornada.
- [ ] Instalar Git y comprobar `git --version`. Tener navegador, editor y terminal operativos.
- [ ] Python 3.9 o superior si esa máquina ejecutará el helper de registro; comprobar `python --version`.
- [ ] Cada integrante tiene un checkout local propio. No trabajar todos sobre una carpeta sincronizada por OneDrive ni compartir un mismo checkout entre máquinas.
- [ ] Acordar un canal humano para claims, cambios de responsable y bloqueos. Un coordinador por integrante; Claude es principal y Codex puede servir de apoyo. Solo uno escribe el historial de una pregunta en un momento dado.

Si todavía no tienes el repo, desde la carpeta donde quieras guardarlo:

```powershell
git clone https://github.com/Ramses-Eloy/Nero-Hackathon.git
cd Nero-Hackathon
git remote -v
git status --short
```

Si ya lo tienes, abrir esa carpeta, revisar `git status --short` y después usar `git pull --ff-only` cuando no haya trabajo pendiente incompatible. Si falla, resolver/integrar; no borrar cambios ni force-push.

Configurar la identidad Git con tu nombre y tu correo verificado o noreply de GitHub. No copiar la identidad de otro compañero. La autenticación Git es aparte del login de Claude/Codex.

No hace falta GitHub MCP para trabajar con este repo si el terminal y Git ya tienen acceso. No publicar tokens ni usar la cuenta Azure personal para crear recursos por anticipado.

## 2. Qué archivos le corresponden a cada integrante

| Integrante | Contexto completo | Perfil individual | Estudio |
|---|---|---|---|
| I1 | proyectos/contexto-microsoft.md | equipo/01-microsoft-azure.md | estudio/microsoft.md |
| I2 | proyectos/contexto-microsoft.md | equipo/02-microsoft-apps-devops.md | estudio/microsoft.md |
| I3 | proyectos/contexto-dynatrace.md | equipo/03-dynatrace-apm-dql.md | estudio/dynatrace.md |
| I4 | proyectos/contexto-dynatrace.md | equipo/04-dynatrace-infra-experiencia.md | estudio/dynatrace.md |

El repo contiene todo: no mover, renombrar ni duplicar CLAUDE.md/AGENTS.md. Ambos contextos explican también el reparto global. Cada chat activa solo su perfil. Los nombres I1–I4 se sustituyen por la persona acordada; no cambiar de identidad sin avisar.

Archivos comunes a los cuatro: GUIA-EQUIPO.md, docs/contexto-ctf.md, docs/protocolo-respuestas.md, docs/comandos-coordinador.md, docs/modelos-rapidez.md, docs/asistentes-skills.md, features/INDEX.md y el historial de la pregunta. Las guías extensas/PDF se consultan según la tarea, no se releen completos en cada mensaje.

## 3. Configurar Claude Code con repo local

1. Instalar/abrir Claude Code mediante su cliente disponible y completar el login. Si usas CLI, verificar `claude --version`; instalar según el [quickstart oficial](https://code.claude.com/docs/en/quickstart) si no existe. No es obligatorio instalar la CLI cuando ya trabajas desde un cliente compatible.
2. Seleccionar/abrir la raíz de Nero-Hackathon. Iniciar desde esa carpeta, no desde proyectos/ o una carpeta vacía.
3. Mantener CLAUDE.md en la raíz. Es la instrucción de proyecto; el prompt inicial pide además leer contexto, perfil, índice y protocolo. [Memoria de proyecto](https://code.claude.com/docs/en/memory).
4. Mantener .claude/skills/ en el checkout. Ahí están las siete skills. Pedir que compruebe cuáles descubre/carga; no copiar las de Codex a esta ruta. [Skills de Claude](https://code.claude.com/docs/en/skills).
5. Seleccionar el modelo disponible: Haiku para preguntas acotadas; Sonnet para diagnóstico/scripts. Si prefieres mantener un coordinador técnico con Sonnet, puede resolver las fáciles sin otro agente. El prompt no cambia su propio motor.
6. Usar el prompt de arranque de la sección 6 con tu integrante. Confirmar acceso real mediante la prueba de la sección 9.
7. Comprobar delegación nativa con una prueba pequeña y explícita. No hay perfiles personalizados de subagentes instalados en este kit. Los agentes nativos disponibles pueden recibir subtareas concretas; selección de modelo/permisos depende del cliente. [Subagentes de Claude](https://code.claude.com/docs/en/sub-agents).

No modificar permisos globales ni desactivar controles para hacer que una prueba funcione. Si la lectura/escritura del repo o el acceso Git requiere autorización del cliente, configurarlo para este workspace con el alcance necesario.

## 4. Configurar Codex con repo local

1. Abrir Codex y completar el login. Añadir/seleccionar como proyecto local la carpeta Nero-Hackathon de esa computadora. Para CLI, iniciar desde esa carpeta; comprobar `codex --version` si ya usas CLI.
2. Mantener AGENTS.md en la raíz. Codex lo usa como guía de proyecto; pedir que lea el contexto y perfil correspondientes. No sustituirlo por CLAUDE.md. [Instrucciones AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
3. Mantener .agents/skills/ en el checkout y comprobar las siete skills disponibles. No necesitan instalarse globalmente para todas las computadoras ni copiarse a .claude/. [Skills](https://learn.chatgpt.com/docs/build-skills).
4. Seleccionar GPT-6 Luna con esfuerzo Low/Light para preguntas acotadas cuando esté disponible. Usar GPT-6.1 Sol para trabajo técnico complejo; Astra para un bloqueo difícil. Revisar disponibilidad en docs/modelos-rapidez.md. No cambiar el motor mediante una palabra clave.
5. Iniciar tu chat con el prompt de la sección 6. Comprobar lectura, escritura y Git con una prueba acotada.
6. Pedir una delegación corta si quieres comprobar subagentes. No hay archivos de agentes personalizados de Codex en el kit; usar capacidad nativa disponible. Las instrucciones del repo permiten delegar cuando aporte rapidez; no requieren agentes para todas las preguntas. [Subagentes](https://learn.chatgpt.com/docs/agent-configuration/subagents).

Si Claude y Codex están abiertos en el mismo checkout, asignar una pregunta o archivos distintos, o dejar uno como lector. No permitir dos coordinadores editando y publicando el mismo historial simultáneamente. Los worktrees se usan si hacen falta cambios de código paralelos, no para toda lectura o consulta.

## 5. Claude web/Proyecto o chat cloud sin checkout

Crear un proyecto personal por integrante, por ejemplo Nero-I1-Microsoft. El contexto del equipo es compartido, pero cada chat identifica al integrante. Un Proyecto web no obtiene habilidades de terminal/escritura por adjuntar MD. [Proyectos Claude](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects).

Adjuntar como conocimiento:

1. El contexto completo de tu pareja, de la tabla de sección 2.
2. Tu perfil individual.
3. CLAUDE.md para Claude; AGENTS.md para Codex cuando sea un entorno que use adjuntos en lugar de checkout.
4. docs/protocolo-respuestas.md y docs/asistentes-skills.md.
5. La guía de estudio de tu plataforma y estudio/scripts-consultas.md.
6. features/INDEX.md y material nuevo pertinente cuando exista.
7. Para Microsoft: referencias/microsoft.pdf. Para Dynatrace: referencias/dynatrace-guia.pdf y referencias/dynatrace-conceptos.pdf.

Opcional: GUIA-EQUIPO.md para uso humano, ejercicios/progreso, fuentes y otras guías cuando hagan falta. Los comandos/modelos ya están explicados en el contexto completo; adjuntar sus MD si se actualizan después. Los archivos de cada pregunta se incorporan al tomarla, no hay preguntas reales precargadas.

Pegar el prompt de arranque en las instrucciones del proyecto y comenzar un chat identificando integrante/pregunta. Si no cabe todo en instrucciones, dejar el prompt allí y los MD como conocimiento. En un chat sin acceso al repo, los nombres de rutas por sí solos no permiten leer archivos: adjuntarlos.

Las skills de .claude/skills/ o .agents/skills/ no quedan instaladas por subir un ZIP de conocimiento. Puede seguir sus procedimientos disponibles en docs/asistentes-skills.md; para usar una skill concreta sin acceso al repo, proporcionar su SKILL.md identificado por nombre. No asumir slash commands ni subagentes nativos de Claude Code en Claude web.

Después de cambios del equipo, actualizar adjuntos o recuperar la versión nueva con una conexión realmente disponible. Si no tiene escritura Git, el chat entrega registro/contenido para que el coordinador conectado lo guarde; no afirmar publicación. Para velocidad y persistencia, preferir Claude Code/Codex local como coordinador operativo y el Proyecto web como apoyo.

## 6. Prompt de arranque listo para copiar

Sustituir integrante, contexto, perfil y guía usando la tabla de sección 2. En Claude usar CLAUDE.md; en Codex usar AGENTS.md. Si no existe checkout, hablar de adjuntos disponibles.

```text
Soy [I1/I2/I3/I4] de Nero. Tú eres mi coordinador de resolución CTF.
Lee [CLAUDE.md o AGENTS.md], [contexto de mi pareja], [mi perfil],
docs/protocolo-respuestas.md, docs/comandos-coordinador.md,
docs/asistentes-skills.md, features/INDEX.md y [guía de mi plataforma].
Usa únicamente archivos/herramientas que realmente tengas disponibles.

Clasifica automáticamente las preguntas; no necesito escribir FACIL,
SCRIPT, DIAGNOSTICO o DIFICIL. Siempre interpreta, analiza, comprueba
evidencia y revisa la candidata antes de entregarla, incluso si es fácil.
Delega subtareas a subagentes cuando ahorre tiempo y el cliente lo permita;
selecciona sus modelos solo si la herramienta lo permite. Un único escritor
conserva el historial de la pregunta. No crees worktrees por rutina.

En chat, solo respuesta exacta o pregunta indispensable con contexto mínimo.
Guarda evidencia y explicación útil en el MD de la pregunta. No pierdas tiempo
con mayúsculas/minúsculas ni puntuación de estilo; cumple requisitos explícitos
de números, decimales, punto/coma, unidades o estructura. No alteres sintaxis
de valores, IDs, URLs, comandos o consultas.

IA está permitida. No envíes respuestas ni abras pistas por pedir análisis.
Cuando confirme un envío, registra respuesta/feedback real aunque sea incorrecto,
mantén desconocidos y sincroniza los archivos relacionados si tienes acceso.
No inventes intentos, puntos, ejecución, agentes creados ni publicación.

Incorpora material nuevo de features/, mantén incidencias/deuda/handoff.
Todavía no te doy una pregunta real. Si puedes leer el contexto, responde
solo “Listo”; si falta un archivo imprescindible, pide únicamente ese archivo.
```

«Listo» no sustituye la prueba técnica de sección 9. La lectura de archivos no acredita acceso al entorno de competencia, todavía pendiente.

## 7. Pareja Microsoft: preparación de herramientas

- [ ] I1 e I2 abren estudio/microsoft.md y el PDF Microsoft; identifican Azure, App Service, APIs, configuración, DevOps, Terraform y KQL.
- [ ] Navegador con DevTools, editor y terminal disponibles. Poder abrir JSON, logs, YAML, .tf y scripts sin ejecutarlos a ciegas.
- [ ] Comprobar acceso al portal/formación del workshop con la cuenta correspondiente. Al recibir el entorno del equipo, verificar tenant/suscripción/Resource Group y permisos; no crear una suscripción de pago para adelantarse.
- [ ] Si ya usarán Azure CLI, comprobar `az --version`; login y selección de suscripción se hacen con las instrucciones del entorno entregado. CLI no es requisito para preguntas resolubles en portal.
- [ ] Si el stack entregado lo exige: .NET/Node/Terraform/Docker. No instalar los cuatro por rutina; el stack no está confirmado. I2 concentra compilación/ejecución local en la máquina más potente.
- [ ] Poder distinguir requests de AppRequests y campos de sus esquemas; practicar una consulta sin confundir muestra y total.
- [ ] Si usarán Microsoft Learn MCP, configurarlo en el cliente según su soporte y probar una consulta documental. .mcp.example.json es un ejemplo, no conexión activa ni acceso Azure. Puede usarse documentación web mientras tanto.
- [ ] I1 e I2 pueden enviar al chat una captura legible con recurso, ventana y resultado pertinente, sin credenciales.

No hace falta montar una aplicación ni desplegar una base común antes de resolver: cada integrante puede trabajar desde que se entregue el entorno.

## 8. Pareja Dynatrace: preparación de herramientas

- [ ] I3 e I4 leen estudio/dynatrace.md y los dos PDF Dynatrace.
- [ ] Seguir la guía del estudiante para cuenta/Playground, University y Essentials; comprobar login y práctica con la misma cuenta cuando corresponda.
- [ ] Navegador actualizado y acceso al laboratorio. Poder localizar entidad, intervalo/zona, servicio, logs/traza y relaciones.
- [ ] Practicar DQL con campos reales del laboratorio; no copiar operadores KQL ni trasladar valores del Playground al CTF.
- [ ] I3 practica servicios/trazas/logs; I4 infraestructura/relaciones/experiencia. Ambos revisan el trabajo de su pareja.
- [ ] No instalar OneAgent, LiveDebugger u otros componentes en sus PCs por rutina: hacerlo solo si las instrucciones del entorno lo requieren.
- [ ] MCP/API es opcional. Se prueba cuando haya acceso real, URL/permisos correspondientes y necesidad; sin eso usar UI y evidencia copiada al chat.
- [ ] Al recibir el tenant de competencia, cambiar a ese entorno y comprobar acceso. El Playground sigue siendo práctica.

## 9. Prueba corta que deben hacer los cuatro hoy

1. Pedir lectura comprobable: «Indica solo mi integrante, pareja, perfil leído y número de skills descubiertas». Esperado: integrante correcto y siete skills si el cliente las descubre. Si no, corregir ruta/contexto; no aceptar una lista inventada como instalación comprobada.
2. Pregunta de laboratorio sin palabra clave: «De 12 solicitudes, 3 fallaron. Responde el porcentaje con dos decimales y punto, sin %». Esperado: `25.00`. Para coma: `25,00`. No consumir intentos en plataforma.
3. Pedir guardar un ensayo claramente marcado LAB en `simulaciones/preparacion/I[n]/nota.md`, no en retos/. Debe describir evidencia y comprobación mínimas, sin tratarlo como envío real. Si es chat web sin escritura, comprobar que entrega contenido/ruta y declara la limitación.
4. Con acceso Git, pedir un commit/push solo de su archivo de laboratorio y verificar que aparece en GitHub. Esa prueba confirma autenticación/escritura; `git push --dry-run` por sí solo no comprueba toda la publicación real. Conservar el ensayo identificado como práctica.
5. Si usarán subagentes, pedir una revisión delegada solo de esa nota, sin escritura ni envío. Comprobar actividad real en el cliente; una frase «delegado» no demuestra un agente creado. Si no está disponible, dejar al coordinador completar el ciclo.
6. Pedir un handoff de práctica que conserve rol, evidencia y próximo paso. Retomar en otro chat con contexto/archivos accesibles; verificar que no lo registra como pregunta real.

El repo incluye tests del helper: `python -m unittest discover -s tests -v`. Ejecutarlos una vez si esa máquina usará el script, no antes de cada respuesta. Los registros de prueba van fuera de las preguntas reales.

## 10. Cierre de preparación y arranque mañana

- [ ] Los cuatro confirman su integrante y pareja.
- [ ] Repo actualizado y autenticación Git comprobada; un archivo LAB por integrante está publicado o hay un responsable conectado para persistencia.
- [ ] Claude/Codex abre el checkout correcto, o el Proyecto web tiene contexto/perfil/adjuntos vigentes.
- [ ] Modelos realmente disponibles identificados; skills y delegación comprobadas o limitaciones anotadas.
- [ ] Prueba de formato y análisis/revisión completada; el chat mantiene salida mínima.
- [ ] Canal humano y regla de responsable único acordados.
- [ ] Entorno de práctica accesible; accesos del CTF que todavía no llegaron siguen pendientes, sin inventarlos.

Mañana: obtener cambios del repo, confirmar accesos/reglas entregados, subirlos a features/, actualizar índice y contexto, tomar preguntas por claim y empezar. No ejecutar MiroFish junto a la competencia por defecto ni aplicar su presupuesto de agentes/RPM al CTF real: son flujos distintos.

Ninguno de estos pasos configura automáticamente las otras computadoras. Cada integrante debe completar su checklist y registrar cualquier bloqueo real antes de la jornada.
