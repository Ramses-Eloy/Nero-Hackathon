# Preparación I4 — LABORATORIO, sin publicación verificada

Fecha de preparación: 2026-10-08, America/Panama.
Coordinador de este chat: I4, Dynatrace, pareja I3. Perfil activo único:
`equipo/04-dynatrace-infra-experiencia.md`. Pregunta competitiva pendiente.

## Workspace y capacidades comprobadas

- `C:\Codex` estaba vacío. Clonado directamente, sin checkout anidado ni
  archivos previos sobrescritos. Remoto fetch/push:
  `https://github.com/Ramses-Eloy/Nero-Hackathon.git`; rama `main`.
  Base leída: `4fa0c02659eeabbeac6bc372490bd28a44da5f3f`.
- Git 2.55.0.windows.5 disponible. Python 3.12.14 ya incluido en el runtime
  oficial de Codex; el alias WindowsApps `python` no tenía intérprete.
  `activar.ps1` añade el runtime únicamente al PATH de la terminal actual.
  No hizo falta instalar Git, Python ni dependencias externas para el registro.
- Leídos AGENTS.md, perfil I4, proyectos/contexto-dynatrace.md,
  equipo/README.md, docs/contexto-ctf.md, docs/estrategia-ctf.md,
  docs/protocolo-respuestas.md, docs/comandos-coordinador.md,
  docs/modelos-rapidez.md, docs/asistentes-skills.md, docs/reglas-pendientes.md,
  features/INDEX.md, estudio/dynatrace.md, estudio/scripts-consultas.md,
  GUIA-EQUIPO.md y CONFIGURAR-EQUIPO.md. Los PDF y referencias/fuentes.md
  no fueron necesarios para este cálculo; no se afirma su lectura.
- Siete SKILL.md de `.agents/skills/` leídos para validar disponibilidad:
  nombres únicos coinciden con carpetas, metadatos name/description no vacíos,
  cuerpo de instrucciones presente. Evidencia: `skills.json`.
  Disponibles en esta sesión por lectura directa; ctf-revisar-respuesta
  aplicada a la prueba. No se afirma aparición verificada en el selector
  automático del cliente ni ejecución de las otras seis skills.
  No hubo duplicación global ni cambios a configuración global.
- Herramientas nativas collaboration disponibles; prueba real delegada a
  `/root/revision_lab_i4`, de solo lectura. Revisión completada: cálculo
  independiente con Decimal en PowerShell, coincidencia de evidencia y script,
  ambos separadores exactos y sin dudas materiales. El coordinador contrastó
  el resultado con la evidencia ejecutada; no hubo envíos ni pistas.
  Modelo/esfuerzo heredados: no se pidió cambio del modelo principal ni se
  atribuye un nombre no comprobado. Ninguna configuración de agentes fue
  necesaria para habilitar las herramientas ya presentes.
- Registro: ejecución única de `python -m unittest discover -s tests -v`:
  6 tests, todos OK; evidencia en `pruebas-registro.txt`.
- Cálculo ejecutado con Decimal y aserciones: 3 / 12 × 100 = 25;
  punto `25.00`, coma `25,00`, dos decimales y sin `%`.
  Evidencia: `laboratorio.py`, `evidencia.json` y `nota.md`.

## Git, identidad y bloqueo de publicación

El conector GitHub autentica el perfil Ramses-Uvilor / Ramses-Sarsanedas.
No había identidad Git configurada. Se reutilizaron el nombre y correo
devueltos por ese perfil, únicamente en `.git/config`, sin inventar identidad.
Ninguna credencial se mostró, guardó en el repo ni transfirió del conector.

Lectura del repo confirmada por clone/fetch. Metadatos del conector:
pull=true, push=false. La consulta de permiso de colaborador devolvió 403
`Resource not accessible by integration`; no permite concluir el permiso
personal fuera del conector. GCM no enumeró cuentas locales.
`git push --dry-run origin HEAD:main` falló sin interacción:
`could not read Username for 'https://github.com': terminal prompts disabled`.
Un dry-run no se considera prueba de publicación real.

Bloqueo imprescindible: autenticar Git local con una cuenta que tenga
escritura en Ramses-Eloy/Nero-Hackathon. Publicación no verificada.
Los archivos de preparación se conservarán localmente y se hará commit
únicamente de esta carpeta. No se autoriza publicar otros archivos.

## Handoff, incidencias y deuda local de preparación

Incidencia abierta I4-GIT-AUTH: autenticación local ausente; responsable I4.
Cierre: push real del commit de preparación y comprobación de su SHA en
la rama remota, además de lectura del archivo remoto publicado.

Retomar este chat como I4, pareja I3; aplicar clasificación automática FACIL,
SCRIPT, DIAGNOSTICO o DIFICIL, ciclo interpretar/analizar/comprobar/revisar
y formato exacto. Antes de enviar una respuesta real hacen falta pregunta,
responsable único y presupuesto observado; análisis no autoriza envío/pistas.
No hay envíos, puntos, intentos ni feedback competitivo en estos archivos.

Próximo paso de preparación: resolver autenticación Git, obtener cambios
sin perder trabajo, publicar solo el commit I4 y comprobar la publicación.
Para otra terminal: `. .\simulaciones\preparacion\I4\activar.ps1`.
URL/acceso de CTF y tenant Dynatrace llegarán después y no bloquean el
laboratorio. No se instalaron OneAgent, Azure, Docker, Terraform ni runtimes
de aplicaciones. No se conectó un tenant ni una API inventados.

Documentación oficial vigente consultada para configuración y límites:
[skills locales](https://learn.chatgpt.com/docs/build-skills) y
[subagentes](https://learn.chatgpt.com/docs/agent-configuration/subagents).
Las skills se mantienen en el repo; la disponibilidad nativa observada
evitó cambios innecesarios de proyecto/globales.
