# Roles del equipo con Claude como desarrollador principal

El integrante 1 es lead y coordinador. Prepara con Claude la base y sus integraciones. Los integrantes 2 y 3 dirigen dos frentes técnicos en paralelo, analizan y verifican el trabajo de Claude. El integrante 4 comprende el reto y prepara documentos, presentación y video desde el inicio. No se asignan horas obligatorias ni se anticipa el enunciado.

## Lead y coordinador

- Interpretar el reto, alcance, restricciones y criterios de aceptación.
- Preparar con Claude repo, entorno, interfaces y configuración común.
- Mantener CLAUDE.md, decisiones y contexto técnico compartido.
- Comprobar las integraciones y explicar cómo continuar desde la base.
- Acordar ramas, sesiones y archivos de los dos frentes técnicos.
- Resolver bloqueos, revisar integración y confirmar la entrega.

## Dirección técnica y análisis A

- Comprender requisitos y herramientas mientras se prepara la base.
- Encargar a Claude el primer bloque técnico según el enunciado.
- Aportar contexto, datos autorizados y criterios de aceptación.
- Analizar código, comportamiento, errores y trazas con las herramientas disponibles.
- Usar skills de análisis, implementación y verificación según la tarea.
- Revisar resultados del otro frente y compartir evidencias con el integrante 4.

## Dirección técnica y análisis B

- Comprender contratos, diseño y comprobaciones necesarias.
- Encargar a Claude el segundo bloque técnico según el enunciado.
- Revisar interfaz, configuración, comunicación y experiencia cuando corresponda.
- Usar skills de diseño, análisis y verificación.
- Integrar cambios con el otro frente y comprobar el recorrido conjunto.
- Aportar capturas y tomas demostrativas verificadas.

## Documentación, presentación y video

- Comprender el enunciado, arquitectura y criterios desde el inicio.
- Preparar esqueleto del informe y guiones, con ayuda de Claude si se desea.
- Ordenar avances, decisiones y evidencias de ambos frentes.
- Mantener claros los resultados implementados, verificados y pendientes.
- Preparar materiales basados en la versión entregada.
- Pedir revisión técnica de afirmaciones al lead y los responsables de cada frente.

## Claude Code

- Desarrollar la base e implementación principal contra requisitos reales.
- Ejecutar herramientas locales e integraciones disponibles y autorizadas.
- Aplicar skills de proyecto para análisis, diseño, implementación, verificación y documentación.
- Registrar cambios y comprobaciones para revisión humana.
- No afirmar resultados sin evidencia ni asumir acceso a herramientas no conectadas.

## Colaboración entre sesiones

Los integrantes 2 y 3 pueden dirigir sesiones distintas de Claude. Usar ramas o worktrees separados y acordar archivos y contratos. El contexto compartido se mantiene en el repo; no se presupone memoria común entre conversaciones.

## Comprobaciones compartidas

| Resultado | Quién dirige | Quién implementa o prepara | Quién comprueba |
|---|---|---|---|
| Base e integraciones | Lead | Claude con el lead | Integrantes 2 y 3 |
| Bloque técnico A | Integrante 2 | Claude | Integrante 3 y lead cuando corresponda |
| Bloque técnico B | Integrante 3 | Claude | Integrante 2 y lead cuando corresponda |
| Recorrido integrado | Lead con integrantes 2 y 3 | Claude y equipo | Responsables de ambos frentes |
| Informe, presentación y video | Integrante 4 | Integrante 4 con apoyo de Claude | Equipo técnico |
| Entrega final | Lead | Equipo | Recepción o aceptación cuando exista |

Las herramientas y skills no sustituyen la comprobación humana. La disponibilidad de MCP o IA no modifica las reglas de acceso del evento.

## Contexto vivo y seguimiento

Todos los roles siguen [el protocolo completo](contexto-equipo-claude.md), revisan [features](../features/README.md), mantienen [incidencias](incidencias.md) y [deuda técnica](deuda-tecnica.md), y dejan [handoffs](sesiones.md). El integrante 4 conoce pendientes y límites para no afirmar resultados sin evidencia. Los errores y la deuda se tachan solo tras comprobar su resolución.
