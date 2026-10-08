# Material compartido durante el desarrollo

Aquí se suben pruebas, documentación, diseños, notas y material por analizar. Claude consulta [INDEX.md](INDEX.md) al comenzar/retomar tareas, después de una carga anunciada y antes de integrar o preparar la entrega. No se incluye un observador automático.

## Organización

- `entrada/`: material recién recibido, sin clasificar.
- `requisitos/`: enunciado, reglas, criterios y aclaraciones con su origen.
- `diseno/`: bocetos, pantallas, contratos visuales y diagramas.
- `analisis/`: diagnósticos, hipótesis, consultas autorizadas y conclusiones.
- `pruebas/`: planes, casos, resultados y logs depurados. El código de tests puede estar en la estructura del stack, enlazado desde aquí.
- `documentacion/`: notas y borradores por revisar.
- `evidencias/`: capturas y resultados con versión y contexto.

Cuando convenga crear `features/<ID>-<nombre>/` a partir de [plantilla-feature.md](plantilla-feature.md). Enlazar originales en lugar de duplicarlos. Referencias oficiales están en `referencias/`; entrega en `docs/`, `presentacion/` y `video/`.

## Carga e incorporación

1. Nombrar el material y añadirlo al índice.
2. Indicar origen, fecha, tarea y qué analizar. Distinguir regla oficial, explicación y observación propia.
3. Claude inspecciona lo que puede leer, resume y actualiza requisitos/decisiones/pruebas afectados.
4. Marcar incorporado solo cuando existe una síntesis registrada. Anotar contradicciones y contenido inaccesible.

Estado: nuevo → en análisis → incorporado; alternativas: requiere aclaración o descartado con motivo. Conservar originales y usar enlaces relativos. Errores van en [incidencias](../docs/incidencias.md), atajos en [deuda](../docs/deuda-tecnica.md), enlazando su evidencia.

No subir secretos, datos restringidos ni logs sin depurar. Acordar almacenamiento de archivos grandes; el índice puede guardar enlaces permitidos. Comprobar permisos antes de enviar contenido a herramientas externas.
