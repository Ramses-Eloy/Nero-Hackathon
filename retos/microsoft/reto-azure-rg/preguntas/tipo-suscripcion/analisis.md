# Análisis

## Evidencia (solo lectura, 2026-10-09)

`az rest GET /subscriptions/<id>?api-version=2022-12-01` devolvió:

- displayName: Azure subscription 1
- quotaId: Sponsored_2016-01-01
- spendingLimit: Off
- locationPlacementId: Public_2014-09-01

El quotaId `Sponsored_2016-01-01` corresponde a la oferta Azure Sponsorship. Aun así la plataforma marcó «Azure Sponsorship» como incorrecta. No se sabe qué cadena esperaba (posibles: «Sponsored», «Sponsorship» u otro nombre mostrado en el portal).

## Límites

Portal no accesible desde el navegador del asistente; dato obtenido con Azure CLI y la cuenta del usuario.
