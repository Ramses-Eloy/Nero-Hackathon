# Nero — Hackathon Copa CTF

**Rapidez obligatoria:** en chat, solo respuesta exacta o pregunta indispensable con contexto mínimo. Sin explicación ni narración; evidencia y explicación van al MD de la pregunta. [Modelos y escalado por dificultad](docs/modelos-rapidez.md).

Preparación y coordinación de un equipo de cuatro para resolver preguntas y retos en los entornos Microsoft y Dynatrace proporcionados por la competencia. El objetivo es acumular puntos del equipo con respuestas fundamentadas, cuidando intentos limitados y pistas con penalización.

La estrategia vigente reemplaza el desarrollo de un producto, presentación y video. Sus archivos fueron retirados de la versión activa; el historial Git permite recuperar el trabajo anterior. No hay retos reales registrados todavía.

## Empezar

Para crear proyectos o chats con una explicación completa, usar [contexto Microsoft (I1–I2)](proyectos/contexto-microsoft.md) o [contexto Dynatrace (I3–I4)](proyectos/contexto-dynatrace.md). Cada documento incluye el mapa del repo, flujo de features y respuestas, responsabilidades y prompt inicial.

1. Leer [contexto y reglas conocidas](docs/contexto-ctf.md), [estrategia 2+2](docs/estrategia-ctf.md) y [datos pendientes](docs/reglas-pendientes.md).
2. Estudiar [Microsoft](estudio/microsoft.md), [Dynatrace](estudio/dynatrace.md), [scripts y consultas](estudio/scripts-consultas.md) y practicar [ejercicios](estudio/ejercicios.md).
3. Abrir el chat con [perfil y prompt del integrante](equipo/README.md). Claude usa [CLAUDE.md](CLAUDE.md); Codex usa [AGENTS.md](AGENTS.md). Ambos siguen el mismo protocolo.
4. Registrar cada pregunta en [retos/](retos/README.md). Analizar y revisar antes de enviar; después confirmar al chat el envío y el resultado real, incluso si fue incorrecto.
5. El asistente guarda el intento y sincroniza los archivos de esa pregunta a GitHub según [el protocolo](docs/protocolo-respuestas.md). No existe un observador automático de la plataforma.

## Reparto confirmado

| Integrante | Pareja | Foco de estudio inicial |
|---|---|---|
| 1 | Microsoft | Azure, App Service, configuración y diagnóstico; coordinación global ligera |
| 2 | Microsoft | APIs, frontend/backend, scripts, Git/DevOps, Terraform y KQL |
| 3 | Dynatrace | Servicios, trazas, logs, DQL y diagnóstico de aplicaciones |
| 4 | Dynatrace | Infraestructura/Kubernetes, relaciones, experiencia de usuario, AppSec y eventos de negocio |

Los focos orientan la preparación; ambos miembros de cada pareja deben poder resolver y revisar preguntas de su plataforma. Cambiar de pareja para desbloquear trabajo cuando sea útil. Cualquier integrante puede enviar una respuesta, pero cada pregunta tiene un único responsable de envío mientras esté activa.

## Contexto vivo y registro

[features/](features/README.md) recibe material nuevo, capturas y aclaraciones. El estado por pregunta vive en retos/, con evidencia, análisis e historial de intentos. Una propuesta del chat no es un envío; un envío no es una respuesta correcta hasta que la plataforma o el humano lo confirme.

Las reglas CTF y el permiso de usar IA fueron confirmados por el usuario el 8 de octubre de 2026. Puntuación exacta, desempates, costo de pistas y límites concretos se incorporarán cuando lleguen. Repositorio: [Ramses-Eloy/Nero-Hackathon](https://github.com/Ramses-Eloy/Nero-Hackathon).

## Herramientas y skills

Las skills son de cuestionamiento, diagnóstico, consultas, revisión y aprendizaje de errores. No desarrollan un producto por defecto. [Catálogo e integraciones](docs/asistentes-skills.md). El helper [registrar_intento.py](scripts/registrar_intento.py) valida y conserva eventos locales; no responde en la plataforma ni hace push por sí solo.

## Fuentes

Los tres PDF originales permanecen en referencias/. [Fuentes, alcance y workshops](referencias/fuentes.md). Las guías distinguen temario público, explicaciones de estudio y reglas confirmadas por el equipo.
