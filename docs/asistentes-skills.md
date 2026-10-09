# Asistentes, skills e integraciones para CTF

## Clasificación automática y revisión obligatoria

El humano entrega la pregunta y evidencia; no necesita escribir FACIL, SCRIPT, DIAGNOSTICO ni DIFICIL. El coordinador elige el modo y las skills automáticamente. Las palabras siguen disponibles como indicaciones opcionales, no como requisito del workflow.

Todas las preguntas, incluidas FACIL, pasan antes de entregar una candidata por: interpretar el enunciado → analizar el contexto pertinente → comprobar evidencia, alcance y resultado → revisar correspondencia con lo pedido y formato explícito. La revisión contrasta la candidata con la fuente, cálculo o comportamiento observado; no consiste en afirmar «revisado» sin comprobación. Si falta evidencia indispensable, preguntar lo mínimo en lugar de adivinar.

El coordinador puede hacer todo el ciclo como agente principal; no es obligatorio crear otro subagente para cada pregunta fácil. Si delega, exige al trabajador candidata, evidencia/comprobación y dudas materiales, y revisa esos resultados antes de responder. La revisión independiente se añade cuando el riesgo o la ambigüedad la justifiquen. Ningún modo omite análisis o revisión por rapidez, pero no se activan todas las skills ni se investigan fuentes irrelevantes.

El chat conserva salida mínima: solo respuesta exacta o pregunta indispensable. Evidencia y explicación útil van al MD de la pregunta. Esto no autoriza envíos ni pistas ni convierte una candidata en un intento confirmado.


**Rapidez obligatoria:** en chat, solo respuesta exacta o pregunta indispensable con contexto mínimo. Sin explicación ni narración; evidencia y explicación van al MD de la pregunta. [Modelos y escalado por dificultad](modelos-rapidez.md).

Claude usa CLAUDE.md y .claude/skills/. Codex usa AGENTS.md y .agents/skills/. El contenido de las siete skills es equivalente, con nombres CTF para evitar activar el antiguo flujo de producto. La metadata básica permite descubrirlas; no se han ejecutado aquí contra un entorno de competencia.

| Skill | Resultado |
|---|---|
| ctf-cuestionar | Interpretación y ambigüedades relevantes |
| ctf-diagnosticar | Hipótesis comprobables y diagnóstico |
| ctf-consultar | Consulta/script pertinente y lectura de resultado |
| ctf-contrastar | Revisión independiente y contraejemplos |
| ctf-revisar-respuesta | Candidata/formato/presupuesto antes de enviar |
| ctf-aprender-error | Aprendizaje de feedback sin desperdiciar reintentos |
| ctf-incorporar-contexto | Nuevas reglas y material reconciliados |

Claude: `/ctf-cuestionar ...`; Codex: `$ctf-cuestionar ...`. Un prompt claro también sirve. No instalar catálogos de diseño, presentaciones o desarrollo por defecto. Las skills no son herramientas de conexión ni permisos; el análisis no concede autorización para gastar intentos/pistas.

## Herramientas según la pregunta

- Azure portal/CLI: recursos, configuración, permisos y diagnóstico. Azure DevOps/Git/terminal: pipeline, repo y scripts entregados.
- Log Analytics/Application Insights: consultas KQL y correlación de solicitudes, excepciones y dependencias. Navegador DevTools y peticiones HTTP: frontend/backend cuando corresponda.
- Dynatrace UI/Notebooks/Dashboards/DQL: servicios, trazas, infraestructura, experiencia y datos disponibles. MCP/API puede complementar si se configura y el entorno proporciona acceso.
- Microsoft Learn MCP: documentación pública; .mcp.example.json es ejemplo, no conexión activada. Documentación oficial Dynatrace y Terraform como referencia.
- GitHub/Git: sincronizar conocimiento y eventos confirmados por pregunta. Repositorio no proporciona un lock de envíos ni comparte memorias automáticamente.

El usuario confirmó que IA está permitida. No conservar la prohibición anterior. Confirmar únicamente disponibilidad técnica concreta; tokens, suscripción, permisos y datos de conexión aún no se proporcionaron. No publicar credenciales ni asumir una instalación en otro compañero.

Fuentes: [Claude skills](https://code.claude.com/docs/en/skills), [Claude memory](https://code.claude.com/docs/en/memory), [Codex skills](https://developers.openai.com/codex/skills), [AGENTS.md](https://developers.openai.com/codex/guides/agents-md), [Learn MCP](https://learn.microsoft.com/en-us/training/support/mcp), [Dynatrace MCP](https://docs.dynatrace.com/docs/dynatrace-intelligence/dynatrace-mcp).

## Comandos rápidos

[Palabras del coordinador](comandos-coordinador.md): FACIL, SCRIPT (SCRIP), DIAGNOSTICO y DIFICIL. Activan flujos de análisis/skills; modelos, subagentes y worktrees se usan según disponibilidad y ahorro de tiempo. No autorizan envíos ni pistas. Nuevas skills de GitHub quedan pendientes de recibir e incorporar.
