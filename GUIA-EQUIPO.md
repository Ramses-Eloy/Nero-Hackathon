# Cómo trabajar en Nero: guía para los cuatro

Esta guía es para nosotros, los participantes. Explica el uso diario del kit sin tener que leer todas las instrucciones de los asistentes. Competimos resolviendo preguntas CTF sobre los entornos Microsoft y Dynatrace que nos entreguen.

## 1. Cómo nos dividimos

| Persona | Pareja | Foco inicial |
|---|---|---|
| I1 | Microsoft | Azure, configuración y diagnóstico; ayuda a coordinar bloqueos |
| I2 | Microsoft | Aplicaciones, scripts, DevOps, Terraform y KQL |
| I3 | Dynatrace | Servicios, trazas, logs y DQL |
| I4 | Dynatrace | Infraestructura, relaciones y experiencia de usuario |

Todos resolvemos. Los focos ayudan a repartir, pero podemos apoyarnos entre parejas. Cada pareja puede investigar dos preguntas distintas a la vez y revisar las respuestas del otro cuando haga falta.

**Para cada pregunta, solo una persona queda encargada de enviar la respuesta.** Acordarlo por nuestro canal de comunicación antes de enviar. Los puntos van al equipo; Git no impide que dos compañeros respondan simultáneamente.

## 2. Antes de empezar

1. Obtener la versión actual del repo. Si ya lo tienes clonado, revisar tus cambios antes de actualizar; no sobrescribir trabajo pendiente.
2. Abrir Claude Code o Codex en la raíz del repo. Si usamos un proyecto/chat sin acceso directo al repo, adjuntar el documento de nuestra pareja y los archivos relevantes actualizados.
3. Elegir el contexto: [Microsoft, I1–I2](proyectos/contexto-microsoft.md) o [Dynatrace, I3–I4](proyectos/contexto-dynatrace.md).
4. Copiar el prompt del final de ese documento y sustituir el integrante y la pregunta actual. Los [perfiles individuales](equipo/README.md) también tienen prompts.
5. Seleccionar el modelo disponible que corresponda. Para preguntas sencillas, Haiku 5.5 o GPT-6 Luna Low; para scripts/diagnóstico, Sonnet 5.5 o GPT-6.1 Sol. Los modelos más potentes quedan para preguntas difíciles. Ver [selección de modelos](docs/modelos-rapidez.md).

No hace falta instalar todo ni conectar todas las herramientas antes de estudiar. Usaremos las que estén disponibles y necesite el reto. Un enlace al repo no da acceso de escritura al chat; un prompt tampoco cambia por sí solo su modelo.

## 3. Qué escribir al coordinador

El chat principal es nuestro coordinador. Le damos la pregunta, captura, logs o archivos pertinentes. **No necesitamos escribir palabras clave:** el coordinador clasifica automáticamente. Si queremos orientar el modo, podemos usar estas palabras opcionales:

| Palabra | Cuándo usarla |
|---|---|
| FACIL | Identificar un dato, extraer un valor o responder una pregunta clara |
| SCRIPT o SCRIP | Preparar una consulta, comando o script necesario |
| DIAGNOSTICO | Encontrar por qué falla algo |
| DIFICIL | Resolver algo complejo o contrastar evidencia contradictoria |

Acepta minúsculas y palabras con o sin tilde. Si solo escribimos la palabra, usa la pregunta activa. Si no usamos ninguna, el coordinador elige el flujo más sencillo adecuado.

```text
FACIL [ID]: ¿Qué nombre aparece en esta captura? [captura]
SCRIPT [ID]: necesito una consulta para contar los errores del intervalo indicado.
DIAGNOSTICO [ID]: la API devuelve 500. Estos son los logs: [...]
DIFICIL [ID]: estas dos fuentes muestran valores distintos para lo que pide el reto.
```

**También las preguntas fáciles se analizan, comprueban y revisan antes de responder.** Ese ciclo puede hacerlo el coordinador sin crear otro agente.

**El chat debe contestar solo la respuesta exacta, el código necesario o una pregunta imprescindible.** La explicación y evidencia se guardan en el MD de la pregunta. Si queremos explicación en chat, la pedimos expresamente.

No tenemos que activar cada skill manualmente ni crear un agente por skill. El coordinador usa solo las necesarias y delega a subagentes cuando ahorre tiempo y el cliente lo permita. Para analizar preguntas normalmente no hacen falta worktrees; se reservan para cambios de código simultáneos. Los subagentes no envían respuestas ni gastan pistas.

## 4. El recorrido de una pregunta

**Tomar → investigar → comprobar → responder → confirmar al chat → registrar y sincronizar → continuar.** Podemos volver a investigar en cualquier momento; no hay horarios rígidos para cada paso.

1. Elegir una pregunta y anunciar: «Tomo [ID], envío I[n], revisor I[n]». Confirmar que nadie más la esté enviando.
2. Dar al coordinador el enunciado exacto, el formato pedido y la evidencia disponible. Incluir intervalo, recurso o intentos si se muestran y son relevantes.
3. Pedir que cree o actualice su carpeta en `retos/microsoft/` o `retos/dynatrace/`. Una pregunta tiene ficha, análisis, evidencias e historial de envíos.
4. Investigar con el flujo apropiado. Revisar especialmente el formato y la evidencia si solo queda un intento. Una respuesta rápida sin fundamento puede gastar una oportunidad.
5. Enviar desde la plataforma con la persona acordada. Si queremos que un asistente conectado lo haga, pedirlo explícitamente para esa pregunta; la palabra rápida por sí sola no autoriza el envío.
6. Confirmar al chat lo que realmente enviamos y qué mostró la plataforma. Hacerlo también cuando salga incorrecta o quede pendiente.
7. El coordinador guarda el evento, actualiza la ficha y sincroniza los archivos relacionados. Nosotros podemos tomar la siguiente pregunta sin esperar una explicación extensa.

Intentamos primero sin pistas. Si decidimos usar una, indicarlo explícitamente y registrar su costo observado. Después de un error, revisar feedback y presupuesto antes de reintentar; no repetir valores a ciegas.

## Formato: cuándo importa

No perder tiempo revisando mayúsculas, minúsculas o puntuación de estilo. Si la pregunta indica cómo responder, sí hay que seguirlo exactamente. Por ejemplo: «con dos decimales y punto» → `12.50`; «con dos decimales y coma» → `12,50`; «solo números» → `12`, sin escribir «doce» ni añadir una explicación. Estos valores son ejemplos de formato, no respuestas de competencia.

Esto no permite cambiar puntos dentro de un número, ID, URL o código: pueden cambiar su significado. Al confirmar el envío, copiar exactamente lo que se envió, aunque el estilo sea flexible.

## 5. Cómo confirmar una respuesta

Podemos usar este mensaje corto cuando los demás datos ya estén en el chat:

```text
CONFIRMO ENVÍO [dominio/reto/pregunta]
Soy I[n]. Envié exactamente: [...]
La plataforma mostró: [correcta / incorrecta / pendiente / error de plataforma].
Feedback/captura: [...]
Intentos restantes visibles: [...] / no se sabe.
Consumió intento: sí / no / no se sabe.
Pistas usadas/costo y cambio de puntos: [...] / no se sabe.
Registra y sincroniza.
```

Si un dato no está visible, decir «no se sabe». No tenemos que inventarlo ni detener todo para completar cada campo. El chat conserva los desconocidos; pregunta únicamente si afectan el siguiente paso.

El resultado real se guarda aunque sea incorrecto. Si llega feedback después, confirmar la actualización del mismo envío: no es un nuevo intento. «Parece correcta» no equivale a confirmar un envío.

Después de comprobar la publicación, el coordinador puede contestar «Registrado». Si dice «Push pendiente», el registro aún no está sincronizado: conservarlo y resolver el bloqueo. Sin acceso al repo, el chat entrega el contenido/ruta para que alguien con acceso lo guarde. No hay un observador automático de la plataforma.

## 6. Cómo subir material a features/

`features/` es nuestra bandeja de documentos, capturas, aclaraciones, scripts entregados y material por analizar. Aquí no significa funcionalidades de una aplicación.

1. Subir el archivo con un nombre identificable dentro de `features/`. Podemos crear subcarpetas Microsoft, Dynatrace o general según necesitemos.
2. Avisar al coordinador dónde quedó, de dónde viene y para qué pregunta puede servir.
3. Pedir que actualice `features/INDEX.md`, analice el material, incorpore lo útil a las guías o preguntas y sincronice esos archivos.
4. Avisar a los compañeros si cambia una regla o afecta sus preguntas. Cada chat debe recibir el archivo o actualizar el repo: no se entera automáticamente.

```text
Subí [ruta real en features/]. Viene de [origen], recibido [fecha].
Revisa qué cambia para [dominio/preguntas], actualiza el índice,
incorpora las conclusiones y sincroniza.
```

Si usamos un chat sin repo, adjuntar el archivo y pedir el análisis; después alguien conectado guarda el material y sus conclusiones. Una captura de respuesta enviada corresponde al historial de la pregunta en `retos/`; no dejar el resultado únicamente en `features/`.

No subir claves, tokens, cookies ni capturas con credenciales. Las skills de GitHub que recibamos más adelante también se revisarán e incorporarán con su referencia y utilidad; todavía no están instaladas por el mero hecho de mencionarlas.

## 7. Qué se guarda y dónde

| Qué queremos guardar o consultar | Dónde |
|---|---|
| Explicación completa para iniciar nuestro chat | `proyectos/` |
| Nuestro perfil y prompt | `equipo/` |
| Guías, consultas y ejercicios de práctica | `estudio/` |
| PDF originales y fuentes | `referencias/` |
| Material nuevo por analizar | `features/` y su `INDEX.md` |
| Enunciado, responsable y estado de una pregunta | `retos/<dominio>/<reto-id>/preguntas/<pregunta-id>/README.md` |
| Evidencia, consultas y explicación de la candidata | `analisis.md` y `evidencias/` de esa pregunta |
| Respuesta enviada y feedback real | `intentos/` de esa pregunta |
| Contexto para retomar otro chat | `docs/sesiones.md` |
| Errores de herramientas o entorno | `docs/incidencias.md` |
| Limitaciones o arreglos pendientes | `docs/deuda-operativa.md` |

No necesitamos ejecutar manualmente el script de registro para cada respuesta si el coordinador tiene acceso y lo hace. Ese helper guarda eventos locales; la sincronización Git es una acción separada que el coordinador debe completar y comprobar.

## 8. Cambiar de chat o pasar una pregunta

Antes de cambiar, pedir: «Guarda el handoff de [pregunta]». Debe dejar qué se comprobó, quién envía, presupuesto conocido, último envío, publicación pendiente y próximo paso.

En el nuevo chat usar el contexto de nuestra pareja y decir:

```text
Retoma como I[n] la pregunta [ID/ruta]. Lee el handoff,
el material nuevo y el historial; continúa desde la evidencia actual.
Solo respuesta exacta o pregunta imprescindible.
```

Si la pasamos a un compañero, anunciar el cambio de responsable de envío antes de que responda. No asumir que el otro chat recuerda nuestra conversación.

## 9. Lo que debemos tener presente durante la competencia

Rapidez, respuesta corta y evidencia suficiente. No repetir análisis ya registrado; no usar pistas automáticamente; no ocultar errores; no confundir una propuesta con una respuesta enviada. Los límites, puntos y reglas exactas se toman de la plataforma y las aclaraciones de la organización cuando lleguen.

Para detalles de coordinación consultar [comandos](docs/comandos-coordinador.md) y [protocolo de respuestas](docs/protocolo-respuestas.md). Esta guía es de uso humano; las instrucciones completas de los asistentes siguen en `CLAUDE.md`, `AGENTS.md` y los contextos de proyecto.
