# Integraciones de Claude Code para el equipo

Claude Code es el desarrollador principal. La preparación gira alrededor de un contexto compartido y conexiones comprobadas. La siguiente tabla es un mapa de funciones, no un calendario de instalación ni una obligación de conectar todo.

| Integración | Función en el desarrollo | Requisitos | Comprobación |
|---|---|---|---|
| Repo local y terminal | Leer y editar código; ejecutar Git, SDK, build, pruebas y Terraform. | Claude Code instalado y autenticado; herramientas y entorno del proyecto. | Leer estructura y requisitos, ejecutar una comprobación real. |
| CLAUDE.md | Conservar instrucciones y contexto compartidos. | Archivo en la raíz del repo. | Confirmar que la sesión lo carga y entiende los roles. |
| Skills de proyecto | Repetir análisis, diseño, implementación, verificación y documentación. | Directorios .claude/skills con SKILL.md. | Invocar una skill y comprobar su salida. |
| GitHub MCP | Repositorios, issues, PR y ejecuciones de Actions. | Cuenta y acceso al repo, autenticación admitida por la integración. | Consultar el repo y una ejecución o PR existente. |
| Azure DevOps MCP | Work items, PR, builds y pipelines. | Organización, permisos y autenticación; Node.js 20+ para el servidor local. | Consultar proyecto y estado de un pipeline. |
| Azure CLI y plugin Azure | Consultar recursos y trabajar con configuración y despliegues; el plugin reúne MCP, agentes y skills de Azure. | Identidad autenticada, suscripción y permisos; herramientas necesarias. | Confirmar suscripción y consultar un recurso permitido. |
| Microsoft Learn MCP | Consultar documentación oficial y ejemplos. | Conexión HTTP pública sin autenticación. | Buscar y recuperar documentación relevante. |
| Playwright MCP o pruebas locales | Inspeccionar y comprobar una interfaz en navegador. | Aplicación accesible; runtime y navegador según la instalación elegida. | Ejecutar un recorrido y conservar su resultado. |
| Dynatrace MCP | Investigar datos de un entorno autorizado. | Entorno, token o OAuth y permisos apropiados. | Solo en un entorno que permita acceso externo. |

GitHub y Azure DevOps son opciones según el repositorio y pipeline que se utilicen; no duplicar tableros ni fuentes de verdad innecesariamente. Si el reto no incluye interfaz, Playwright puede omitirse. Terraform se ejecuta por terminal y no exige añadir un MCP de Terraform.

## Contexto y skills incluidos

CLAUDE.md contiene las reglas compartidas y remite al [protocolo completo](contexto-equipo-claude.md). Se incluyen ocho skills de proyecto, redactadas para el equipo:

- /incorporar-contexto: revisar material nuevo en features/ y actualizar el contexto afectado.
- /analizar: comprender arquitectura, síntomas y evidencia.
- /disenar: definir contratos o interfaz según el requisito.
- /implementar: desarrollar un cambio verificable.
- /verificar: comprobar criterios y registrar hallazgos.
- /gestionar-incidencias: registrar fallos, investigar y verificar correcciones autorizadas.
- /revisar-deuda: mantener limitaciones visibles y cerrar solo lo resuelto y comprobado.
- /documentar: convertir avances verificados en materiales de entrega.

Son instrucciones propias del kit, no plugins certificados ni dependencias instaladas. No llaman automáticamente a servidores que aún no estén conectados.

Consultar [herramientas de diseño y skills](herramientas-diseno-skills.md) para apoyos opcionales. Los registros de features/, incidencias, deuda y sesiones se comparten mediante Git; ninguna integración proporciona memoria automática entre los chats del equipo.

## Configuración de ejemplo

.mcp.example.json incluye únicamente Microsoft Learn y no activa conexiones. Para usarlo, revisar el contenido y copiar o combinar su definición en .mcp.json dentro del proyecto elegido. Claude puede requerir aprobación del servidor del proyecto. Cada integrante autentica sus accesos en su propia máquina; no compartir credenciales en Git.

Para Azure, el comando documentado dentro de Claude Code es:

```text
/plugin install azure@claude-plugins-official
```

Elegir el plugin o la configuración manual de Azure MCP según el entorno, evitando duplicar el mismo servidor. El plugin no otorga permisos por sí solo.

Para Azure DevOps, Microsoft recomienda el servidor local en clientes como Claude Code cuando no puedan autenticar al servidor remoto mediante el flujo requerido. Usar la guía oficial de ese servidor para la organización real.

Para revisar servidores configurados:

```text
claude mcp list
```

Dentro de Claude Code, /mcp muestra el estado. Registrado no equivale a conectado ni autenticado: hacer una consulta de prueba con los permisos esperados.

## Sesiones de los integrantes 2 y 3

Ambos pueden dirigir a Claude en paralelo. Cada frente debe tener una rama o worktree, archivos asignados y contratos acordados. Compartir decisiones por documentos y commits; no confiar en que el historial de una conversación se transfiera a otra. Integrar los cambios y repetir comprobaciones conjuntas.

El integrante 4 puede pedir a Claude resúmenes y borradores a partir de docs/evidencias.md y docs/avances.md. Los responsables técnicos comprueban las afirmaciones y la versión que aparece en el video.

## Restricciones del entorno competitivo

El acceso técnico a un MCP no implica que esté permitido en el evento. El workshop de Dynatrace establece restricciones a agentes externos en su entorno competitivo. Mantener esa investigación dentro de los accesos autorizados y no transferir datos restringidos para sustituir la conexión bloqueada. Confirmar el alcance de las reglas de IA para los demás frentes.

## Fuentes oficiales

- [MCP en Claude Code](https://code.claude.com/docs/en/mcp)
- [Skills](https://code.claude.com/docs/en/skills)
- [Contexto del proyecto](https://code.claude.com/docs/en/memory)
- [Azure MCP y plugin para Claude](https://github.com/microsoft/mcp/blob/main/servers/Azure.Mcp.Server/README.md)
- [Azure DevOps MCP](https://learn.microsoft.com/en-us/azure/devops/mcp-server/mcp-server-overview?view=azure-devops)
- [GitHub MCP](https://github.com/github/github-mcp-server)
- [Microsoft Learn MCP](https://learn.microsoft.com/en-us/training/support/mcp)
- [Playwright MCP](https://github.com/microsoft/playwright-mcp)
- [Dynatrace MCP](https://docs.dynatrace.com/docs/dynatrace-intelligence/dynatrace-mcp)
