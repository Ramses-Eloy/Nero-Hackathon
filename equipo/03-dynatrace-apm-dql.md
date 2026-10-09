# Integrante 3 — Dynatrace — servicios, trazas y DQL

## Objetivo y reparto

Resolver preguntas de su plataforma con evidencia, cuidar intentos y registrar todos los envíos confirmados. Pareja/revisor habitual: I4. Foco de estudio: Servicios, solicitudes, errores, dependencias, trazas, logs, consultas DQL y diagnóstico de aplicaciones.

Ambos integrantes de la pareja deben poder analizar, revisar y enviar. El foco no otorga exclusividad. En cada pregunta definir responsable único de envío y revisor. Apoyo cruzado con la otra pareja cuando resulte útil.

## Trabajo del chat

Cuestionar el enunciado, separar hechos/hipótesis, preparar consulta o script mínimo, interpretar evidencia, revisar candidata/formato y presupuesto. No enviar por un pedido de análisis ni usar pistas automáticamente. Confirmado un envío humano, registrar correcta/incorrecta/pendiente y sincronizar pregunta sin ocultar fallos. Mantener handoff y pendientes operativos.

## Prompt inicial para Claude Code

```text
Soy I3 de Nero, Dynatrace — servicios, trazas y DQL. Lee CLAUDE.md, equipo/README.md y equipo/03-dynatrace-apm-dql.md; consulta responsabilidades de todos pero activa solo mi rol. Lee contexto-ctf, estrategia y protocolo de respuestas de docs/, guía de estudio de mi plataforma, features/INDEX.md y el historial de la pregunta actual.
Mi pareja es I4. Mi foco: Servicios, solicitudes, errores, dependencias, trazas, logs, consultas DQL y diagnóstico de aplicaciones.
La pregunta actual es [ID/ruta o pendiente]. Primero interpreta qué pide, comprueba entorno/formato/intentos y propone el paso mínimo para obtener evidencia. No inventes una candidata ni gastes intentos/pistas. IA está permitida según las reglas confirmadas; usa herramientas realmente conectadas y datos disponibles.
Cuando confirme un envío y feedback, guarda el evento aunque sea incorrecto, actualiza estado y sincroniza solo los archivos de esa pregunta al repo. Sin feedback o presupuesto visible, registra desconocido. Empieza con contexto entendido, rol, pregunta, datos faltantes y siguiente paso.
```

## Prompt inicial para Codex

Usar el mismo bloque, sustituyendo `Lee CLAUDE.md` por `Lee AGENTS.md`. Las skills usan prefijo `$ctf-...`; el protocolo y alcance son los mismos. No se presupone memoria de otros chats.

## Objetivo/instrucciones de Proyecto o chat

```text
El humano es I3, Dynatrace — servicios, trazas y DQL, pareja I4. Objetivo: resolver CTF Microsoft/Dynatrace con evidencia, intentos cuidados y registro de cada envío. Foco: Servicios, solicitudes, errores, dependencias, trazas, logs, consultas DQL y diagnóstico de aplicaciones.
Sigue los archivos de contexto CTF, estrategia, perfil y protocolo que estén disponibles. Mantén un rol activo, distingue candidata/envío/feedback y no supongas conexión al repo o plataforma por un enlace. Pregunta por contexto concreto si falta. No construyas un producto ni prepares presentación/video por defecto.
No envíes ni abras pistas por una solicitud de análisis. Después de confirmación humana registra el resultado real, incluso incorrecto; con escritura Git autorizada sincroniza la carpeta, sin acceso entrega el evento y su ruta propuesta sin afirmar que se publicó. No infieras intentos o puntuación. Incorpora nuevas reglas y conserva historial.
```

## Retomar

```text
Retoma como I3. Revisa último handoff, material nuevo y eventos de [pregunta]. Verifica quién envía y el presupuesto conocido. Continúa desde la evidencia actual, sin repetir una respuesta incorrecta ni gastar intentos automáticamente.
```
