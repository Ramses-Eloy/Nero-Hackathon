# Modelos para responder rápido en el CTF

Recomendación del equipo basada en documentación oficial consultada el 8 de octubre de 2026. No es un benchmark del entorno de competencia ni una garantía de latencia. Elegir los modelos realmente disponibles en cada cuenta/cliente. No se cambiaron configuraciones personales ni se conectó una API.

## Selección práctica para ambas parejas

| Situación | Claude | GPT en Codex/Work | Criterio |
|---|---|---|---|
| Valor visible, extracción de logs/captura, concepto acotado, formato o consulta sencilla | Haiku 5.5 | GPT-6 Luna con esfuerzo Low/Light | Primera opción por rapidez en tareas claras |
| Script, consulta compleja, diagnóstico con varias fuentes o corrección del reto | Sonnet 5.5 | GPT-6.1 Sol con esfuerzo Low/Light; Medium si lo exige el problema | Evitar vueltas improductivas del modelo pequeño |
| Bloqueo real, evidencia contradictoria o revisión de alto riesgo que los anteriores no resuelven | Opus 5.5 | GPT-6 Astra | Escalar solo la pregunta difícil; volver luego al modelo rápido |

Para Claude como asistente principal: Haiku para preguntas sencillas; Sonnet para diagnóstico/scripts. Para Codex: Luna Low como primera opción en preguntas acotadas, Sol para trabajo técnico complejo. No pedir respuesta a todos los modelos en cada pregunta ni elegir automáticamente el más potente. La recomendación de Low en Sol para este CTF prioriza rapidez; subir esfuerzo si no produce evidencia suficiente.

Anthropic clasifica Haiku 5.5 como el más rápido a velocidad estándar y Sonnet 5.5 como equilibrio de velocidad/capacidad. Su anuncio aclara que Opus en Fast Mode puede ser más rápido: no existe un ganador absoluto independiente del modo. [Comparación oficial](https://platform.claude.com/docs/en/models/overview), [anuncio Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5).

OpenAI sitúa Luna en tareas enfocadas y extracción, y recomienda Luna Low para problemas acotados; Sol se orienta a trabajo técnico complejo. Esta asignación CTF es una recomendación basada en esas capacidades. [Selección oficial](https://developers.openai.com/api/docs/guides/model-selection), [GPT-6 Luna](https://developers.openai.com/api/docs/models/gpt-6-luna).

## Configuración y acceso

Seleccionar el modelo en el selector real del cliente; un prompt no cambia el motor. En Codex usar GPT-6 Luna y esfuerzo Low/Light cuando estén disponibles. Los niveles API y los del cliente no son idénticos: no copiar `none` de la API suponiendo que existe en la interfaz. En Claude elegir el nivel de esfuerzo más bajo adecuado que el cliente/modelo permita; no afirmar que se desactivó thinking si no se comprobó.

GPT-6 Luna y GPT-6.1 Sol están documentados para Work/Codex; no suponer que aparecen en ChatGPT Chat convencional. Disponibilidad depende del plan, cliente y despliegue. Si faltan, seleccionar la opción rápida realmente disponible y verificar la calidad con una práctica corta. [Disponibilidad oficial](https://learn.chatgpt.com/docs/models).

Fast/Ultrafast y modos rápidos de Claude pueden ayudar cuando estén disponibles, pero sus condiciones y consumo se verifican en el cliente. No activarlos ni comprar acceso por una instrucción de estilo. Los nombres/versiones se revisarán cuando cambie el catálogo, sin bloquear la competencia para investigar novedades.

## Rapidez de extremo a extremo

Reducir texto de salida, lecturas redundantes, herramientas y consultas innecesarias. Mantener el contexto pertinente a la pregunta; no adjuntar todos los PDF en cada mensaje. Evitar sesiones cloud con preparación lenta para una pregunta que se puede resolver con el entorno ya abierto. No confundir tiempo hasta el primer token con tiempo hasta una respuesta correcta.

En preparación, probar unas pocas preguntas de laboratorio representativas con el contexto real y registrar tiempo hasta respuesta útil y errores. No inventar segundos o tasas de acierto. Para un único intento, la comprobación mínima necesaria puede ahorrar más tiempo que una respuesta rápida equivocada. La explicación se conserva en el MD y el chat devuelve solo la respuesta exacta o la pregunta indispensable.

## Comandos rápidos

[Palabras del coordinador](comandos-coordinador.md): FACIL, SCRIPT (SCRIP), DIAGNOSTICO y DIFICIL. Activan flujos de análisis/skills; modelos, subagentes y worktrees se usan según disponibilidad y ahorro de tiempo. No autorizan envíos ni pistas. Nuevas skills de GitHub quedan pendientes de recibir e incorporar.
