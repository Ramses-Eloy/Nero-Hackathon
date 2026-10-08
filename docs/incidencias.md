# Registro de errores e incidencias

No hay fallos del proyecto registrados todavía: el kit contiene preparación, no implementación del reto.

Crear entradas por fallos observados. IDs por rol: `ERR-L-001`, `ERR-A-001`, `ERR-B-001`, `ERR-D-001`; comprobar que no existan. Registrar también errores de comandos que afecten al trabajo.

## Plantilla

```markdown
- [ ] ERR-[rol]-[número] — [Título]
  - Estado: abierto / investigando / corregido pendiente de verificar / bloqueado / verificado.
  - Detección: fecha, persona/sesión y tarea.
  - Impacto: requisito, componente o recorrido afectado.
  - Versión y entorno: rama/commit, configuración sin secretos.
  - Reproducción: pasos, entrada y comando.
  - Esperado:
  - Observado:
  - Evidencia: ruta de log/captura/test y ventana temporal si aplica.
  - Hipótesis / causa confirmada: distinguir ambas.
  - Responsable y cambio aplicado:
  - Comprobación de cierre: pasos, resultado, fecha y versión.
  - Prueba de regresión necesaria y resultado:
  - Deuda/tarea relacionada:
  - Historial y reaperturas:
```

Después de resolver **y verificar**, usar `- [x] ~~ERR-A-001 — Título~~`, conservando detalles. Un fix sin prueba sigue abierto. Una prueba bloqueada no permite cerrar: explicar bloqueo. Si reaparece, retirar check/tachado y anotar evidencia. No descartar un fallo ni afirmar una causa sin evidencia.
