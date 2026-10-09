# Incidencias operativas

Guardar fallas de acceso, consultas, entorno o Git que afectan la resolución. Una respuesta incorrecta se registra primero en su pregunta; enlazarla aquí solo si existe un problema operativo adicional.

- [ ] INC-[integrante]-[ID] — Título
  - Fecha, pregunta afectada, entorno:
  - Esperado / observado y evidencia:
  - Hipótesis / causa confirmada:
  - Impacto sobre intentos o coordinación:
  - Acción y comprobación:
  - Responsable y siguiente paso:

Check y tachado solo tras resolver y comprobar. Conservar historial y reabrir si reaparece. No afirmar que un timeout de envío no consumió intento: verificar en la plataforma.

- [ ] INC-I4-001 — Registros npm/pip bloqueados en el contenedor cloud de Claude (I4)
  - Fecha, pregunta afectada, entorno: 2026-10-08 21:48 America/Panama; ninguna pregunta aún; sesión cloud Claude de I4.
  - Esperado / observado y evidencia: `npm view express` y `npm view @dynatrace-oss/dynatrace-mcp-server` → E403 Forbidden desde registry.npmjs.org; `pip download requests` → sin distribución. API de releases de dynatrace-oss/dtctl → 403 (repo no adjunto a la sesión).
  - Hipótesis / causa confirmada: política de red del entorno; no se comprobó una causa adicional.
  - Impacto sobre intentos o coordinación: no se instaló Dynatrace MCP ni dtctl en este contenedor. Disponibles: Python 3 (stdlib), Node 22, jq, gh, git con push al repo. Sin URL/token de tenant Dynatrace en el entorno.
  - Acción y comprobación: tests del helper OK (6/6). Para consultas DQL, usar la UI/Notebooks del tenant entregado o instalar las herramientas en el equipo local de I4.
  - Responsable y siguiente paso: I4; reintentar instalación solo si el reto entrega tenant/token y hace falta CLI/MCP.
  - 2026-10-08 22:00 America/Bogota, equipo local Windows de I4: `npm view @dynatrace-oss/dynatrace-mcp-server version` → 2.1.2 y API de releases de dtctl → 200. El bloqueo solo afecta al contenedor cloud; en local la instalación es posible cuando haya tenant/token. Se mantiene abierta hasta instalar y probar con el tenant.

