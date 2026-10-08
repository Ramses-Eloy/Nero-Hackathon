# Registro de deuda técnica

No hay deuda de implementación registrada todavía. Stack y comandos por elegir son datos pendientes de preparación, no evidencia de una aplicación defectuosa.

Registrar limitaciones/atajos reales. IDs por rol: `TD-L-001`, `TD-A-001`, `TD-B-001`, `TD-D-001`. Vincular tareas/errores, evitando duplicación.

## Plantilla

```markdown
- [ ] TD-[rol]-[número] — [Título]
  - Estado: abierta / en resolución / aplazada / aceptada temporalmente / resuelta y verificada.
  - Origen: fecha, tarea y decisión.
  - Área y versión:
  - Limitación y motivo de aceptación:
  - Impacto observable o riesgo concreto:
  - Responsable:
  - Condición para retomarla: dependencia, requisito o siguiente cambio relevante.
  - Plan de resolución y criterio de cierre:
  - Evidencia inicial:
  - Cambio realizado y comprobaciones:
  - Evidencia de cierre: resultado, fecha y commit/entorno.
  - Incidencias relacionadas:
  - Historial:
```

Tras resolver y comprobar el criterio, usar `- [x] ~~TD-A-001 — Título~~`. Conservar historial y reabrir si reaparece. Aplazada/aceptada sigue `[ ]`: aceptar una limitación no la elimina.

Revisar deuda pertinente al iniciar/cerrar tareas y el conjunto antes de entregar. El lead acuerda qué afecta evaluación/demo y qué se declara como limitación. No se exige resolver toda la deuda ni priorizar por horas; sí mantenerla visible y comprobar lo que se afirma resuelto.
