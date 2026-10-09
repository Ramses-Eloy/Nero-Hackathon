# Veraguas — Microsoft (Centro de Monitoreo de Operaciones de Vuelo)

Evidencia extraída de los repos oficiales del reto:
- `HackathonLabsNetworks/2026-Veraguas-Microsoft` (app + narrativa + lookups + KQL)
- `HackathonLabsNetworks/2026-Veraguas-Microsoft-IaC` (Terraform)

Fuentes clave: `section_files/section_4.md`, `hackathon_files/lookups/matriz_errores.csv`,
`hackathon_files/lookups/endpoints_clave.csv`, `hackathon_files/notebooks/*.kql`,
`hackathon_files/templates/frontend/frontend.zip`, `.../backend/backend.zip`, IaC `main.tf`/`locals.tf`.

## Entorno confirmado (equipo 36)

- Suscripción: **Azure subscription 1** · Offer/tipo: **Azure Sponsorship** (portal: banner microsoftazuresponsorships.com; Subscription ID `d2dda6e6-81c9-42a9-86c8-55c8e8552a95`).
- Directorio/tenant: `marcoayalalitumaoutlook.onmicrosoft.com`.
- Resource Group del equipo: **`rg-team-36`** · Región: **Central US** (IaC: `location = data.azurerm_resource_group.team.location`).
- `plan_index = floor((team_id-1)/2)+1` → team 36 ⇒ **18** ⇒ planes `plan-front-18` / `plan-back-18` (en `rg-hackathon-shared`).
- Web Apps (IaC): Backend `hackathon-copa-2026-team-36-api`, Frontend `hackathon-copa-2026-team-36-frontend`.
  - URLs: `https://hackathon-copa-2026-team-36-api.azurewebsites.net`, `https://hackathon-copa-2026-team-36-frontend.azurewebsites.net`.
- Observabilidad: App Insights `hackathon-copa-2026-team-36-appi`, Log Analytics `hackathon-copa-2026-team-36-law`.
- cloud_RoleName del backend en App Insights contiene `api`.

Nota: la cuenta `angel.zhang21@outlook.com` tiene rol acotado "Resource access" y en el portal solo ve los 2 App Service plans; no ve Web Apps ni App Insights. Las Web Apps son públicas (azurewebsites.net), así que sus endpoints se pueden consultar directo por URL.

## Endpoints reales (código backend)

| endpoint | método | notas |
|---|---|---|
| `/health` | GET | liveness, siempre `{ "status": "Healthy" }` 200 |
| `/health/deep` | GET | 200 si Healthy; 503 Degraded/Unhealthy. Depende de handshake + `HealthCheckMode=deep` |
| `/api/information` | GET | catálogo de vuelos (equivale a "flights/list" de la doc) |
| `/api/services` | GET | estado de servicios |
| `/api/status` | GET | 200 `{available:true}` solo si deep Healthy **y** `FeatureFlags:EnableFinalValidation=true`; si no, 503 `{available:false, errorCode:"E5"}` |

Drift doc↔código: los lookups hablan de `/api/flights/list`, `/api/flights/create`, `/api/service` y campo `ready`; el código usa `/api/information`, `/api/services`, `/api/status` y campo `available`. CTFd suele graduar con la nomenclatura de la doc. E6 pide **implementar** `POST /api/flights/create` (no existe `FlightsController`).

## Errores (candidatas con evidencia)

### E1 — URL del backend incorrecta en el frontend
- Archivo: `frontend/src/environments/environment.prod.ts` → `apiBaseUrl: 'https://api.occ.copa.com'` (host inexistente).
- Corrección: `apiBaseUrl: 'https://hackathon-copa-2026-team-36-api.azurewebsites.net'`.
- Evidencia App Insights (doc oficial E1): "requests fallidos hacia el backend de tipo **connection refused** o **DNS resolution failed**".
- **Candidata tipo de error (reto 1301):** `DNS resolution failed` (host no resuelve). Alternativa oficial: `connection refused`.

### E2 — CORS mal configurado
- Archivo: `backend/appsettings.Production.json` → `AllowedOrigins: "http://localhost:4300"` (incorrecto).
- Corrección: `AllowedOrigins: "https://hackathon-copa-2026-team-36-frontend.azurewebsites.net"`.
- Evidencia App Insights: requests `OPTIONS` (preflight) rechazados (resultCode 403/204). Consola: "has been blocked by CORS policy".

### E3 — Variable de entorno con nombre incorrecto (configuration drift)
- Doc/KQL: backend busca `PRODUCT_SERVICE_URL`; excepción `ConfigurationException`; `/api/service` devuelve 400.
- Frontend `environment.prod.ts` usa `SERVICE_ENDPOINT_URLX` (sufijo X sospechoso) vs `INFORMATION_ENDPOINT_URL`.
- AMBIGÜEDAD: nombre exacto a corregir no verificable solo con el código visto. Requiere la excepción real en App Insights (KQL `AppInsights_Excepciones_E3.kql`) o el app_setting faltante en el portal. NO adivinar flag.

### E4 — Health check profundo (depende de E1+E2+E3)
- Archivo: `backend/appsettings.Production.json` → `HealthCheckMode: "basic"` (incorrecto).
- Corrección: `HealthCheckMode: "deep"`. Además requiere handshake del frontend verificado (llamadas con Origin permitido a `/api/information` y `/api/services`).
- `/health/deep` devuelve 503 Degraded con `errorCode E4` mientras no sea deep o no haya handshake.

### E5 — Feature flag (depende de E4)
- Archivo: `backend/appsettings.Production.json` → `FeatureFlags.EnableFinalValidation: false`.
- Corrección: `true`. Con false, `/api/status` → 503 (doc: `{ready:false}`; código: `{available:false, errorCode:"E5"}`).
- **Endpoint con `{"ready": false}` = `/api/status`.**

### E6 — POST /api/flights/create (depende de E5)
- No existe `FlightsController`. Hay que implementar `POST /api/flights/create` con validación de payload (400 si falta campo obligatorio; 201 Created con el vuelo) y persistencia in-memory visible en el GET de listado.

## Respuestas de teoría ya entregadas (Cat7 / API)
- Listar recursos de un RG por CLI: `az resource list`.
- Concurrencia POST create: colección compartida thread-safe + IDs atómicos.
- POST crea pero no aparece en list: se guarda en colección distinta/temporal a la que consulta el GET.
- Payload sin campo obligatorio: 400 Bad Request indicando el campo.
- POST create exitoso: 201 Created con los datos del vuelo.
- Endpoint de listado: `GET /api/flights/list`.

## Pendiente de entorno (no accesible con cuenta actual)
- Telemetría de App Insights (E1/E2/E3) y Dynatrace (reto minería cripto por `asset_id`): fuera del scope de esta cuenta. Las corre el CLI o se abren las URLs públicas de las Web Apps.
