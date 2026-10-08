---
name: gestionar-incidencias
description: Registra e investiga fallos observados y verifica correcciones dentro del alcance autorizado.
disable-model-invocation: true
---

1. Leer el contexto, features/INDEX.md, docs/incidencias.md y deuda relacionada. Identificar versión y entorno del fallo.
2. Reproducir cuando sea posible. Guardar esperado/observado y evidencia depurada con pasos concretos.
3. Separar hipótesis de causa confirmada. Comprobar la causa antes de aplicar cambios amplios.
4. Corregir dentro del alcance autorizado y ownership de archivos; si solo se pidió análisis, entregar diagnóstico y comprobación propuesta.
5. Repetir la reproducción y pruebas de regresión pertinentes. Registrar resultado real y versión; si hay bloqueo, mantener abierto.
6. Solo tras resolución verificada usar check y título tachado. Conservar historial; reabrir si reaparece. Vincular deuda genuina sin duplicar registros.
