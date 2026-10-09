# Runbook — Ejecutar la narrativa Veraguas-Microsoft en Azure (equipo 36)

Ciclo DevOps del reto: **desplegar → diagnosticar → corregir → redeploy → validar**.
Valores concretos para `team_id = 36` (`plan_index = 18`).

## 0. Acceso al tenant
- Aceptar la invitación en el correo (Remitente "Microsoft Invitacion", asunto "esteban-meza85 invited you to collaborate with Directorio predeterminado"). Revisar spam.
- **Solo 1 (máx. 2) personas** entran al tenant y configuran.
- Validar: suscripción **Azure subscription 1**, directorio **marcoayalalitumaoutlook.onmicrosoft.com**, RG **`rg-team-36`** (rol Contributor solo ahí).

## 1. Desplegar la infraestructura (IaC)
En Azure **Cloud Shell (Bash)**:
```bash
git clone <repo-IaC>
cd <repo-IaC>            # 2026-Veraguas-Microsoft-IaC
chmod u+x deploy.ps1
./deploy.ps1 -TeamId 36
```
Esperar "Infraestructura del equipo desplegada correctamente". Crea 4 recursos en `rg-team-36`:
`hackathon-copa-2026-team-36-law`, `-appi`, `-frontend`, `-api`.

## 2. Desplegar frontend y backend
Desde la raíz del repo `2026-Veraguas-Microsoft`:
```bash
# Backend (.NET 10) — build durante el deploy (Oryx) ya está activado
az webapp deploy -g rg-team-36 -n hackathon-copa-2026-team-36-api \
  --src-path hackathon_files/templates/backend/backend.zip --type zip
# Frontend (React Native Web) — si el zip es código, requiere build:
#   npm ci && npm run build  → zipear el output → desplegar
az webapp deploy -g rg-team-36 -n hackathon-copa-2026-team-36-frontend \
  --src-path hackathon_files/templates/frontend/frontend.zip --type zip
```

## 3. Diagnóstico (Application Insights `-appi`)
- Portal → App Insights → **Failures** (requests/dependencies/exceptions).
- KQL útiles en `2026-Veraguas-Microsoft/hackathon_files/notebooks/*.kql`.
- Correlacionar cada fallo con el archivo del repo (ver tabla abajo).

## 4. Corregir los 6 errores
E1, E2, E3 son independientes (en paralelo). E4 requiere E1+E2+E3. E5 requiere E4. E6 requiere E5.
Tras cada fix: **rebuild** (`dotnet build` / `npm run build`) y **redeploy** al App Service correspondiente.

| Error | Archivo | Valor incorrecto | Corrección |
|---|---|---|---|
| **E1** URL backend | `frontend/src/environments/environment.prod.ts` | `apiBaseUrl: 'https://api.occ.copa.com'` | `apiBaseUrl: 'https://hackathon-copa-2026-team-36-api.azurewebsites.net'` → rebuild+redeploy frontend |
| **E2** CORS | `backend/appsettings.Production.json` | `AllowedOrigins: "http://localhost:4300"` | `"https://hackathon-copa-2026-team-36-frontend.azurewebsites.net"` → redeploy backend |
| **E3** variable | ver nota | nombre de variable incorrecto | Corregir el nombre exacto que App Insights reporta como no encontrado (candidatos: frontend `SERVICE_ENDPOINT_URLX`→`SERVICE_ENDPOINT_URL`; doc/KQL apuntan a `PRODUCT_SERVICE_URL` como app setting del backend). Confirmar con la excepción real antes de fijar. |
| **E4** health profundo | `backend/appsettings.Production.json` | `HealthCheckMode: "basic"` | `"deep"` (+ requiere handshake: con E1/E2 ok, el frontend llama a `/api/information` y `/api/services` con Origin permitido) → redeploy |
| **E5** feature flag | `backend/appsettings.Production.json` | `FeatureFlags.EnableFinalValidation: false` | `true` → redeploy |
| **E6** POST create | `backend` (no existe `FlightsController`) | endpoint no implementado | Implementar `POST /api/flights/create` con validación de payload (falta campo → 400; éxito → 201 Created) y persistencia in-memory visible en el listado |

## 5. Validación operativa
Contra `https://hackathon-copa-2026-team-36-api.azurewebsites.net`:
- `/health` → 200 `{"status":"Healthy"}` (siempre).
- `/health/deep` → 200 (deep) tras E1+E2+E3+E4; antes 503 `errorCode E4`.
- `/api/status` → `{ready/available: true}` tras E5; antes 503 `errorCode E5`.
- `/api/information` y `/api/services` → 200 con datos.
- Frontend carga y sus llamadas a la API funcionan (sin errores DNS/CORS en Network).

## Notas DevOps
- No cambiar lógica de negocio ni la config del RG; solo corregir los 6 errores.
- Responder cada pregunta en CTFd al resolver su error (scoring all-or-nothing, desempate por tiempo).
- Reparto sugerido: 1–2 hacen cambios/deploys; el resto revisa App Insights y documenta.
