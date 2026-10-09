# Preparación del equipo de I1 (Microsoft/Azure)

Fecha: 2026-10-08. Equipo local Windows 11 Home (10.0.26200). Sin credenciales ni tokens en este archivo.

## Listo

| Herramienta | Estado | Versión | Ruta / método |
|---|---|---|---|
| Git | Ya instalado | 2.51.0.windows.1 | En PATH |
| Azure CLI | Instalado con winget (`Microsoft.AzureCLI`, MSI oficial de Microsoft, hash verificado) | 2.91.0 | `C:\Program Files\Microsoft SDKs\Azure\CLI2\wbin\az.cmd` |
| Terraform | Instalado con winget (`Hashicorp.Terraform`, zip oficial de releases.hashicorp.com, hash verificado) | 1.16.5 | Paquete WinGet, alias `terraform` en PATH de usuario |

- Las terminales abiertas antes de la instalación deben reiniciarse para ver el PATH nuevo.
- Repo: `C:\Users\angel\OneDrive\Documentos\Hackathon\Nero-Hackathon`, `origin` = https://github.com/Ramses-Eloy/Nero-Hackathon.git, rama `main`. Árbol limpio; `git pull --ff-only` (3deba1f → 6ef1111) sin tocar cambios locales.
- GitHub: `git push --dry-run` autentica por HTTPS (Git Credential Manager). `gh` CLI no instalado; no hace falta para el flujo actual.
- Aviso: `C:\Users\angel` (carpeta de usuario) también es un repo Git con `origin` = Roxx29/Laboratorio-1. No se tocó; trabajar siempre desde la ruta del repo Nero.

## Pendiente

- [ ] Acceso a la suscripción Azure del evento. `az login --use-device-code --allow-no-subscriptions` terminó con código 0 con la cuenta Microsoft personal, pero no devolvió tenants ni suscripciones (`az account list` vacío). No se creó suscripción ni prueba gratuita.
  - El entorno se entrega el 2026-10-09 mediante un script de la organización con el número de grupo. Al recibirlo: leer el script antes de ejecutarlo, no guardar las credenciales que genere, luego `az account list -o table` y `az account set --subscription <id>` con la suscripción que asigne el script.
- [ ] Archivos Terraform/scripts de la competencia. No se ejecutó `terraform init/plan/apply/destroy` ni despliegues.
