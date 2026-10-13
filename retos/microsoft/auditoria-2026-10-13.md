# Auditoría Microsoft (2026-10-13, 21:15Z, solo lectura)

## Estado real en Azure (az + curl)

- rg-team-36 (centralus): 4 recursos. Son `hackathon-copa-2026-team-36-law`, `-appi`, `-api` y `-frontend`, y coinciden con el plan de Terraform (4 to add).
- Permiso actual de ramses.sarsanedas: **Reader** en rg-team-36. Contributor ya no existe: lo retiró esteban-meza85 el 2026-10-09 a las 21:38Z.
- Activity log: el organizador (esteban-meza85) detuvo las dos Web Apps el 2026-10-09 a las 21:50Z y las volvió a arrancar el 2026-10-13 a las 16:18Z.
- **Backend hoy:** `/` devuelve la página por defecto «Microsoft Azure App Service - Welcome». `/health`, `/health/deep`, `/api/status`, `/api/services`, `/api/information`, `/api/flights/list` y `/swagger/v1/swagger.json` devuelven **404** (Kestrel). No hay aplicación desplegada en el backend.
- **Frontend hoy:** responde 200 (React/Vite, «Copa Airlines — OCC»). Como el backend está vacío, muestra «Error al cargar vuelos: Error E1» (captura de Eloy).
- No se pudo consultar Application Insights desde la CLI, porque falta la extensión y la instalación pide confirmación interactiva.

## Errores E1–E6

| Error | Fix en código (evidencia/codigo-corregido) | Verificado el 2026-10-09 (evidencia/) | Verificado hoy |
|---|---|---|---|
| E1 URL backend | Sí: environment.prod.ts, apiBaseUrl | Sí: capturas | **No**: el front muestra Error E1 porque el backend no tiene app |
| E2 CORS | Sí: AllowedOrigins | Sí | **No**: el backend da 404 |
| E3 variable | Sí: SERVICE_ENDPOINT_URL | Sí | **No** |
| E4 health deep | Sí: HealthCheckMode=deep | Sí | **No**: /health/deep da 404 |
| E5 feature flag | Sí: EnableFinalValidation=true | Sí | **No**: /api/status da 404 |
| E6 POST vuelos | Sí: FlightsController | Sí | **No**: /api/flights/list da 404 |

## Preguntas registradas en retos/microsoft

| Pregunta | Estado en el repo |
|---|---|
| Región del RG | Candidata centralus; no consta envío ni resultado |
| Tipo de suscripción | Agotada: «Azure Sponsorship» incorrecta, 0 intentos |
| Error App Insights E1 | Candidata «DNS resolution failed»; el humano reportó que las anteriores eran incorrectas, sin texto exacto |
| Archivo E1 | Candidata environment.prod.ts, tras la pista; sin resultado registrado |
| Endpoint {"ready": false} | Candidata /api/status; sin envío |
| Preflight CORS | Candidata OPTIONS; sin envío |
| Endpoint E3 (400) | /api/services incorrecta; nueva candidata /api/service, sin resultado |
| 1201: recursos tras Terraform | 4 (plan y RG); sin envío registrado |
| Endpoints del backend | Código: /api/information, /api/services, /api/status, /api/diagnostics/probe, /health, /health/deep, más /api/flights/list y /api/flights/create (E6). No se puede comprobar en vivo |

## Pendiente

- Volver a publicar el backend corregido (zip de evidencia/codigo-corregido + repo del reto) y comprobar el frontend. Con Reader ya no podemos hacerlo: hace falta el permiso del organizador, o que el equipo confirme que la revisión ya cerró.
- La carpeta evidencia/ (2,7 MB de capturas) no está en Git.
