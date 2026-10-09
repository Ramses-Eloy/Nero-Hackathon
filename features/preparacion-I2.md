# Preparación del equipo de I2 (Microsoft/Azure)

Fecha: 2026-10-08. Equipo local Windows 11 Pro Education (10.0.26200). Sin credenciales ni tokens en este archivo.

## Listo

| Herramienta | Estado | Versión | Ruta / método |
|---|---|---|---|
| Git | Ya instalado | 2.55.0.windows.5 | En PATH |
| Azure CLI | Instalado con winget (`Microsoft.AzureCLI`, MSI oficial de Microsoft, hash verificado) | 2.91.0 | `C:\Program Files\Microsoft SDKs\Azure\CLI2\wbin\az.cmd` |
| Terraform | Instalado con winget (`Hashicorp.Terraform`, zip oficial de releases.hashicorp.com, hash verificado) | 1.16.5 | Paquete WinGet, alias `terraform` en PATH de usuario |

- Las terminales abiertas antes de la instalación deben reiniciarse para ver el PATH nuevo.
- Repo: `origin` = https://github.com/Ramses-Eloy/Nero-Hackathon.git, rama `main`. Árbol limpio; se hizo `git pull --ff-only` (b85216b → b958eb3) sin tocar cambios locales.
- GitHub: `git ls-remote` y `git push --dry-run` autentican por HTTPS (Git Credential Manager). `gh` CLI no está instalado; no hace falta para el flujo actual.

## Pendiente

- [ ] Acceso a la suscripción Azure del evento. `az login --use-device-code` completó la autenticación con una cuenta Microsoft personal, pero Azure respondió «No subscriptions found». No se creó suscripción ni prueba gratuita. Siguiente paso: cuando el evento entregue cuenta/tenant, ejecutar `az login` (o `az login --tenant <tenant>`), luego `az account list -o table` y `az account set --subscription <id>` con la suscripción confirmada.
- [ ] Archivos Terraform/scripts de la competencia. No se ejecutó `terraform init/plan/apply/destroy` ni despliegues.
