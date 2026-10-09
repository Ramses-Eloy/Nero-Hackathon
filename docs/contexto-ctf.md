# Contexto vigente — CTF

**Rapidez obligatoria:** en chat, solo respuesta exacta o pregunta indispensable con contexto mínimo. Sin explicación ni narración; evidencia y explicación van al MD de la pregunta. [Modelos y escalado por dificultad](modelos-rapidez.md).

## Confirmado por el usuario, 8 de octubre de 2026

- La hackathon utiliza Capture the Flag: una plataforma habilita varios retos con preguntas sobre Microsoft y Dynatrace.
- Hay que investigar, y cuando el reto lo requiera corregir, usando los entornos entregados. Scripts, backend, frontend, DevOps y observabilidad forman parte de la preparación.
- Las preguntas no están cronometradas individualmente según la información recibida; algunas permiten uno, dos o tres intentos. Registrar el límite real de cada una, sin generalizar.
- Existen pistas y usarlas resta puntos. Se busca resolver primero sin pistas.
- Cualquier integrante puede responder; los puntos se suman al banco del equipo.
- Compiten con otros 51 equipos. El usuario indica que responder rápido importa; la fórmula de puntuación/desempate todavía no está disponible.
- Reparto: integrantes 1–2 Microsoft, 3–4 Dynatrace. El integrante 4 ahora resuelve retos, no tiene rol de presentación.
- El usuario confirma que se pueden utilizar Claude, Codex y otras IA durante toda la competencia, sin las restricciones de IA que se habían interpretado previamente. No repetir aquella prohibición en el flujo actual. Disponibilidad de conexiones y credenciales es una cuestión técnica aparte.
- Cada envío, correcto o incorrecto, se confirma al chat y se registra/sincroniza en el repo. No se presume acceso automático a la plataforma.

## Objetivo operativo

Maximizar puntos del equipo mediante investigación paralela, respuestas sustentadas, verificación proporcionada al riesgo del intento y coordinación de envíos. No convertir el CTF en un proyecto de producto ni crear entregables de presentación por defecto.

## Qué falta

Consultar [reglas-pendientes.md](reglas-pendientes.md). No inventar penalización de respuesta incorrecta, fórmula por velocidad, puntos por pregunta, bloqueo de retos, reset de entornos o cierre global. Que no haya cronómetro por pregunta no implica duración ilimitada del evento.

## Qué hace el asistente coordinador

Mantiene contexto de su integrante y pregunta actual, cuestiona ambigüedades, ayuda a localizar evidencia y propone la comprobación mínima que permite decidir. Puede preparar scripts/consultas y correcciones acotadas al reto cuando estén autorizadas. No refactoriza ni despliega por iniciativa propia.

Presenta una respuesta candidata separada de su fundamento, unidad/formato y límites. Antes de un envío con intentos limitados comprueba que no exista otro responsable enviando. No usa pistas ni consume intentos por un simple pedido de análisis. Si el humano pide expresamente enviar, exige conocer la pregunta exacta y su presupuesto de intentos, y registra el resultado observado.

Después de la confirmación del humano, conserva el intento y actualiza el estado aunque el resultado sea incorrecto. Sin feedback concluyente el resultado es pendiente; sin confirmación de consumo no resta intentos por inferencia. Los chats comparten archivos y commits, no memoria automática ni locks de Git.

## Contexto nuevo

Leer features/INDEX.md al retomar y cuando el equipo anuncie nuevas reglas/evidencias. Registrar origen, fecha y qué cambia. Si la aclaración modifica un supuesto, actualizar guías, perfiles y preguntas afectadas; no mantener dos reglas incompatibles.
