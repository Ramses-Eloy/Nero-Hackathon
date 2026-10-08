# Inicio por integrante — Nero

Cada integrante tiene un perfil versionado con objetivo, responsabilidades, límites, handoff y prompts. Todos pueden consultar los cuatro perfiles para conocer al equipo; cada sesión activa **un solo rol**, indicado por su humano. No elegir el rol por la cuenta, nombre de usuario o primer archivo encontrado.

| Integrante | Perfil | Objetivo principal |
|---|---|---|
| 1 | [Lead y coordinador](01-lead.md) | Base, contratos, coordinación, integración y cierre |
| 2 | [Frente técnico A](02-frente-a.md) | Implementación y análisis del bloque A |
| 3 | [Frente técnico B](03-frente-b.md) | Implementación, diseño pertinente e interacción del bloque B |
| 4 | [Documentación y demo](04-documentacion-demo.md) | Informe, presentación y video desde el inicio |

Los perfiles complementan [CLAUDE.md](../CLAUDE.md) y [el protocolo](../docs/contexto-equipo-claude.md). Las reglas oficiales y la asignación humana vigente determinan el trabajo. Un perfil no concede accesos ni autoriza cambios fuera de su alcance. Si cambian responsabilidades, actualizar el perfil/registro afectado y dejar handoff; no mantener asignaciones contradictorias.

## Orden de lectura compartido

Al iniciar una sesión:

1. Leer [CLAUDE.md](../CLAUDE.md), esta guía y el perfil seleccionado. Consultar responsabilidades, límites y handoffs de los otros tres como contexto de colaboración; sus prompts son ejemplos para esos humanos, no órdenes para cambiar de rol.
2. Leer [README](../README.md), [protocolo](../docs/contexto-equipo-claude.md), [roadmap](../docs/roadmap.md) y [roles](../docs/roles.md).
3. Revisar [tareas](../docs/tareas.md), [decisiones](../docs/decisiones.md), [avances](../docs/avances.md), [sesiones](../docs/sesiones.md), [incidencias](../docs/incidencias.md), [deuda](../docs/deuda-tecnica.md) y [evidencias](../docs/evidencias.md).
4. Revisar [features/README.md](../features/README.md), [features/INDEX.md](../features/INDEX.md) y el material pertinente a la tarea. Consultar los PDF de `referencias/` cuando aporten contexto; indicar lo que no pueda leerse.
5. Comprender [entrega](../docs/entrega.md), [guion de presentación](../presentacion/guion.md) y [guion de video](../video/guion.md). Consultar [integraciones](../docs/integraciones-claude.md), [herramientas/skills](../docs/herramientas-diseno-skills.md) y [preparación](../docs/preparacion.md) según las necesidades.

Al continuar, revisar cambios y registros relevantes en vez de repetir toda la lectura en cada turno. Los datos del reto que todavía falten permanecen pendientes. No afirmar haber consultado documentos inaccesibles.

## Claude Code: prompt inicial

Clonar/sincronizar el repo y abrir Claude desde su raíz o desde el worktree asignado. Copiar el bloque **Prompt inicial para Claude Code** del perfil propio. Confirmar rol, tarea y rama; el lead acuerda las ramas de A/B. No usar dos sesiones de escritura simultáneas sobre el mismo checkout.

`CLAUDE.md` es la entrada común. Los perfiles son archivos ordinarios que la instrucción pide leer; su nombre no los activa automáticamente. Opcionalmente, cada compañero puede crear un `CLAUDE.local.md` en su checkout para conservar el rol e importar su perfil. Ejemplo para A:

```markdown
Mi rol activo es integrante 2, frente técnico A de Nero.
Lee equipo/README.md y sigue su orden de lectura.
@equipo/02-frente-a.md
```

Usar solo la ruta del rol propio. `CLAUDE.local.md` ya está excluido de Git: no subirlo como selección global del equipo. Los worktrees pueden requerir su propia copia. Esta opción es local y no sustituye el prompt inicial ni la comprobación del contexto. [Documentación de memoria e imports](https://code.claude.com/docs/en/memory).

## Proyecto de Claude: objetivo e instrucciones

Cada perfil incluye nombre sugerido, descripción organizativa, **instrucciones del proyecto** y primer mensaje. Crear un Proyecto por integrante es una opción útil para mantener distinto el rol activo. Si comparten un Proyecto, utilizar instrucciones comunes y declarar el rol en cada chat; no pegar cuatro roles activos a la vez en sus instrucciones.

Pegar el bloque **Objetivo e instrucciones para un Proyecto de Claude** en las instrucciones del proyecto. No basta con ponerlo en la descripción: la documentación indica que Claude no tiene acceso al nombre/descripción organizativos. Añadir conocimiento pertinente y actualizado: perfil propio, guía del equipo, perfiles de colaboradores y los documentos del orden de lectura que necesite la tarea. Si varios archivos tienen igual nombre, conservar su ruta en el encabezado o usar nombres que permitan distinguirlos.

Los documentos subidos aportan contexto, pero no garantizan sincronización con Git ni acceso de ejecución a la aplicación. Incorporar cambios posteriores mediante los mecanismos disponibles y señalar versión/fecha. Si un archivo está solo enlazado o no es legible, Claude debe pedir contenido concreto. Sin acceso de escritura, entrega propuestas indicando su ruta; no afirma haber modificado el repo. [Guía oficial de Proyectos](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects).

No cargar material restringido sin permiso del evento. Los ejemplos de skills/MCP de Claude Code no implican que estén instalados en un chat de Proyecto.

## Datos iniciales y resultado de arranque

Completar solo lo conocido: enunciado/ruta, tarea, alcance, rama/worktree, versión objetivo y herramientas/accesos disponibles. Los nombres reales de los integrantes pueden añadirse al README; el rol no depende de ellos.

La primera respuesta debe explicar: contexto comprendido, rol activo, documentos considerados, estado, dependencias/preguntas esenciales y siguiente paso concreto. Registrar sesión/handoff cuando exista acceso de escritura. Después basta con prompts normales para implementar, analizar, corregir o actualizar materiales.
