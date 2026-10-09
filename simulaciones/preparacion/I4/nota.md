# LAB — preparación I4 (no es un reto ni un envío real)

- Fecha: 2026-10-08, America/Bogota. Equipo local Windows 11, Claude Code 2.1.295, checkout `C:\Claude\Nero`.
- Integrante I4 (Dynatrace — infraestructura/experiencia), pareja I3. Perfil leído: equipo/04-dynatrace-infra-experiencia.md.
- Skills en repo: 7 en `.claude/skills/` (ctf-aprender-error, ctf-consultar, ctf-contrastar, ctf-cuestionar, ctf-diagnosticar, ctf-incorporar-contexto, ctf-revisar-respuesta). La sesión se inició antes de clonar: Claude Code las descubre al reabrir desde la raíz del repo.
- Prueba de formato: «De 12 solicitudes, 3 fallaron; porcentaje con dos decimales y punto, sin %». Comprobación: 3/12 = 0.25 → 25.00. Candidata LAB: `25.00`. No se envió a ninguna plataforma.
- Herramientas comprobadas: git 2.55, Python 3.14.5 (tests del helper 6/6 OK), Node 24.19 / npm 11.17, winget. Registros npm y GitHub API accesibles desde este equipo. No instalados: gh, az, dtctl, Dynatrace MCP (sin tenant/token todavía).
- Este archivo es la prueba de commit/push de I4.

# LABORATORIO — preparación I4

Caso sintético del usuario: 3 fallos de 12 solicitudes. No es pregunta,
telemetría, regla, intento ni feedback del entorno competitivo.

Interpretación: porcentaje de solicitudes fallidas sobre el total completo de
12 solicitudes, con dos decimales y sin el símbolo de porcentaje.
Comprobación: 3 / 12 = 0.25; 0.25 × 100 = 25.
Candidata con punto: `25.00`. Variante cuando se exige coma: `25,00`.
Revisión: denominador 12, dos cifras decimales, separador solicitado y sin `%`.

Ejecución reproducible: `python simulaciones/preparacion/I4/laboratorio.py`.
El script usa Decimal y aserciones; guarda la evidencia en `evidencia.json`.
No se ha enviado ninguna respuesta ni abierto ninguna pista.
