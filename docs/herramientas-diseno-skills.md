# Herramientas de diseño, skills y apoyo por fase

Catálogo aplicable al flujo de cuatro integrantes con Claude como desarrollador principal, revisado el 8 de octubre de 2026. Es una selección para cubrir las fases del proyecto; no es una lista de herramientas obligatorias ni una afirmación de que estén instaladas. Las plataformas vinculadas al evento y sus accesos se explican en [integraciones-claude.md](integraciones-claude.md) y [preparacion.md](preparacion.md). No se ha escogido aún el stack del reto.

## 1. Qué es cada mecanismo

`CLAUDE.md` aporta contexto persistente del repo. Una skill contiene instrucciones para una tarea. Un plugin puede agrupar skills, agentes y otras capacidades. MCP conecta herramientas o servicios; su disponibilidad técnica no concede permiso sobre sus datos. Un CLI ejecuta comandos locales con los permisos de esa máquina.

Las skills de proyecto se guardan en `.claude/skills/<nombre>/SKILL.md`; este kit las configura para invocación manual con `disable-model-invocation: true`. Cada compañero necesita el repo actualizado y una sesión que las reconozca. La instalación personal de un plugin no se comparte por subir documentos. Referencias: [skills de Claude](https://code.claude.com/docs/en/skills), [memoria y CLAUDE.md](https://code.claude.com/docs/en/memory).

## 2. Ocho skills propias incluidas

Estas son instrucciones creadas para vuestro equipo, no plugins oficiales de Anthropic. No dependen de una conexión MCP concreta; su capacidad efectiva depende de lo disponible en la sesión.

| Invocación | Cuándo usar | Resultado esperado |
|---|---|---|
| `/incorporar-contexto [rutas]` | Al subir archivos a features/ o retomar | Índice actualizado, síntesis, contradicciones y tareas afectadas |
| `/analizar [objetivo]` | Requisito, arquitectura o comportamiento por investigar | Observaciones, hipótesis y comprobaciones con evidencia |
| `/disenar [alcance]` | Flujo, interfaz o contrato antes de implementar | Diseño pertinente al reto, estados y criterios de validación |
| `/implementar [tarea]` | Cambio autorizado con criterio conocido | Implementación acotada, registros y comprobación real |
| `/verificar [alcance]` | Cambio, corrección o versión integrada | Pruebas, resultados, evidencia y limitaciones |
| `/gestionar-incidencias [error]` | Fallo observado | Reproducción, diagnóstico, corrección autorizada y prueba de cierre |
| `/revisar-deuda [área]` | Al retomar un componente o antes de entregar | Deuda visible, resolución dentro del alcance y cierre comprobado |
| `/documentar [versión]` | Durante desarrollo y preparación de entrega | Informe/guiones coherentes con lo comprobado |

El lead usa contexto, análisis, diseño e implementación para preparar la base. A/B combinan implementación, análisis, verificación e incidencias. El integrante 4 usa documentación y material/evidencias; pide comprobaciones a los técnicos. Todos revisan deuda relevante. Una tarea sencilla puede hacerse con un prompt normal sin invocar todo el catálogo.

## 3. Skills publicadas por Anthropic

El [repositorio de skills](https://github.com/anthropics/skills) ofrece ejemplos reutilizables. Revisar instrucciones, dependencias y licencia de cada carpeta antes de incorporarlas; las de documentos tienen condiciones propias. No copiar todo el repositorio por defecto.

| Skill | Aplicación al proyecto | Uso con Claude |
|---|---|---|
| [frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) | Interfaz funcional y diseño visual si el reto tiene UI | Pedir flujo, estados y adaptación al stack real; comprobar funcionamiento, no solo apariencia |
| [webapp-testing](https://github.com/anthropics/skills/blob/main/skills/webapp-testing/SKILL.md) | Pruebas de aplicaciones web locales | Utiliza Playwright; revisar dependencias y guardar resultados/capturas |
| [doc-coauthoring](https://github.com/anthropics/skills/blob/main/skills/doc-coauthoring/SKILL.md) | Informe técnico y narrativa compartida | Iterar estructura, redacción y comprensión del lector a partir de fuentes |
| [canvas-design](https://github.com/anthropics/skills/tree/main/skills/canvas-design) | Piezas gráficas estáticas | Útil para una portada o lámina, si se dispone de dependencias |
| [theme-factory](https://github.com/anthropics/skills/tree/main/skills/theme-factory) | Consistencia visual de materiales | Acordar un tema y aplicarlo sin sustituir contenido técnico |
| [web-artifacts-builder](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder) | Artefactos web de apoyo | Opcional si hace falta un artefacto complejo; no exige cambiar vuestro stack |
| [docx](https://github.com/anthropics/skills/tree/main/skills/docx), [pdf](https://github.com/anthropics/skills/tree/main/skills/pdf), [pptx](https://github.com/anthropics/skills/tree/main/skills/pptx), [xlsx](https://github.com/anthropics/skills/tree/main/skills/xlsx) | Informe, consulta de fuentes, diapositivas o datos tabulares | Generar/revisar los formatos realmente requeridos y abrirlos para inspección |

Ruta publicada para explorar estos ejemplos en Claude Code:

```text
/plugin marketplace add anthropics/skills
/plugin install example-skills@anthropic-agent-skills
/plugin install document-skills@anthropic-agent-skills
```

Son instrucciones de preparación, no comandos ejecutados en esta máquina. Revisar el contenido antes de instalar y elegir el paquete necesario. Los nombres de invocación de skills de plugins pueden llevar namespace; consultar los comandos que Claude muestre después de instalar. [Instrucciones del repositorio](https://github.com/anthropics/skills).

## 4. Plugins para desarrollo y revisión

El [directorio de plugins](https://github.com/anthropics/claude-plugins-official) distingue plugins de Anthropic y aportaciones externas. Estar en el marketplace no convierte cualquier integración externa en una creación de Anthropic. Comprobar editor, instrucciones y disponibilidad desde `/plugin`.

- [feature-dev](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/feature-dev/README.md): flujo estructurado de exploración, arquitectura y revisión. Puede resultar útil para un bloque grande; incluye agentes y momentos de aprobación. No es necesario activarlo para cada ajuste ni imponer sus siete fases al calendario del equipo.
- [pr-review-toolkit](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/pr-review-toolkit/README.md): revisiones especializadas de cambios. Aplicarlo antes de integrar cuando el alcance lo justifique; convertir hallazgos válidos en tareas/incidencias/deuda y verificarlos.

Ejemplo de instalación publicado para el directorio:

```text
/plugin install feature-dev@claude-plugins-official
/plugin install pr-review-toolkit@claude-plugins-official
```

No se han instalado ni probado aquí. Si el nombre no aparece en vuestra versión, buscarlo desde el catálogo y seguir su README vigente. Las skills propias del kit cubren el flujo básico sin depender de estos plugins.

## 5. Diseño y diagramas

| Herramienta | Fase y responsable | Cuenta/acceso | Relación con Claude |
|---|---|---|---|
| [Figma / FigJam](https://www.figma.com/) | Flujos, pantallas y colaboración; B con lead, apoyo del integrante 4 | Cuenta y permiso sobre el archivo para colaboración; comprobar el plan y capacidades disponibles | El [MCP de Figma](https://developers.figma.com/docs/figma-mcp-server/) aporta contexto de diseño. [Code to canvas](https://developers.figma.com/docs/figma-mcp-server/code-to-canvas/) documenta captura de UI desde Claude Code con servidor remoto; no asumir que cualquier conexión permite toda operación |
| [Excalidraw](https://excalidraw.com/) | Bocetos de arquitectura, relaciones y explicación rápida | Comprobar modalidad usada; no hace falta introducirlo si basta un diagrama del repo | Claude puede ayudar con estructura/texto; para editar archivos usar formato/herramientas disponibles. No se presupone MCP instalado. [Documentación](https://docs.excalidraw.com/) |
| [Mermaid](https://mermaid.js.org/intro/) | Diagramas de flujo/arquitectura versionados junto al Markdown | Uso local basado en texto; no requiere cuenta propia | Claude escribe y revisa el diagrama; renderizar para comprobar flechas y legibilidad |

Decidir si hace falta un archivo de diseño separado. Para una UI, acordar navegación y estados vacío/carga/error/éxito, tipografía, contraste y tamaños. Guardar una referencia en features/diseno/; Claude implementa y el equipo compara contra el comportamiento y el diseño acordados. Para un reto sin UI, priorizar diagramas y contratos necesarios para explicar el sistema.

## 6. Verificación visual y funcional

- [Playwright](https://playwright.dev/): automatizar recorridos web y capturas desde tests o herramientas compatibles. La skill webapp-testing es una vía; otra conexión no equivale automáticamente a la misma configuración. Registrar URL, versión, datos de prueba y resultado.
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/): auditorías de páginas desde Chrome DevTools o CLI. Guardar el informe y usarlo para investigar; una puntuación no sustituye la revisión manual de interacción/accesibilidad.
- DevTools del navegador: revisar red y errores de la app cuando corresponda. Guardar solo logs depurados y contexto necesario; no publicar tokens de peticiones.

Combinar recorrido principal, escenarios de error y revisión humana. Si la app no es web, escoger pruebas propias del stack; no instalar Playwright o Lighthouse solo por aparecer aquí.

## 7. Documentos, presentación y video

El integrante 4 trabaja desde el inicio con evidencia de A/B/lead. Puede usar las skills de documentos para generar formatos y el editor que ya maneje el equipo para revisar. Guardar guiones y fuentes en el repo, aunque los archivos finales se produzcan en otra herramienta.

- Documento: Markdown como fuente compartida; DOCX/PDF si los exige la entrega. Revisar tablas, enlaces y legibilidad después de exportar.
- Presentación: guion versionado en `presentacion/guion.md`; generar PPTX si corresponde y revisar el archivo en el editor elegido. Una exportación correcta no garantiza que cada diapositiva se vea bien.
- [OBS Studio](https://obsproject.com/kb/quick-start-guide): grabar pantalla y audio. Probar una toma corta antes de la demo. Claude ayuda con guion y preparación; no asumir grabación automática desde una skill.
- [FFmpeg](https://ffmpeg.org/documentation.html): edición/conversión por CLI cuando esté instalado; Claude puede preparar comandos para archivos autorizados. Revisar duración, resolución, audio y contenido final, conservando la grabación original.

No hace falta adquirir otra herramienta para presentación/video si el equipo ya tiene un editor adecuado. Confirmar formatos, duración y forma de entrega con reglas vigentes.

## 8. Integraciones técnicas y documentación

Las conexiones a Azure, Azure DevOps, GitHub, Terraform, Microsoft Learn y Dynatrace se desarrollan en [integraciones-claude.md](integraciones-claude.md). Elegir las pertinentes al reto. Las cuentas del evento, créditos, roles y acceso a organizaciones pueden depender de la asignación del organizador; no asumir que una cuenta personal concede acceso.

[Context7](https://github.com/upstash/context7) es una opción adicional de documentación para librerías cuando ayude al stack elegido. No reemplaza las especificaciones del evento ni concede acceso a sus entornos.

Para Dynatrace, confirmar expresamente reglas de agentes externos y uso de datos del reto antes de habilitar una conexión. Mantener el análisis manual permitido si una integración no está autorizada. No confundir lectura de documentación pública con consulta de datos privados de una aplicación.

## 9. Preparación eficiente sin cargarlo todo

El núcleo es repo + CLAUDE.md + features/ + registros + comandos del stack. Después comprobar las integraciones necesarias para la base, elegir diseño/diagramas si aportan valor y activar herramientas de prueba cuando exista algo que probar. El integrante 4 prepara guiones desde el inicio y utiliza herramientas de exportación/grabación cuando haya resultados demostrables.

Registrar herramienta/plugin, versión o revisión, responsable, acceso, prueba realizada y alternativa en `docs/preparacion.md`. Una herramienta queda preparada cuando se comprueba una operación concreta, no cuando se instala. Mantener los registros de errores/deuda actualizados a lo largo de todas las fases.
