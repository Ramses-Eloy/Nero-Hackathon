# Estrategia de resolución 2+2

**Rapidez obligatoria:** en chat, solo respuesta exacta o pregunta indispensable con contexto mínimo. Sin explicación ni narración; evidencia y explicación van al MD de la pregunta. [Modelos y escalado por dificultad](modelos-rapidez.md).

Trayectoria flexible: **estudiar y practicar → reconocer el entorno → repartir preguntas → investigar → revisar → enviar → confirmar y registrar → continuar/aprender**. Se puede volver a investigar en cualquier paso. No hay fase de construir un producto ni de preparar presentación/video.

## Preparación conjunta

Todos comprenden HTTP, logs/métricas/trazas, lectura de enunciados, unidades, ventanas temporales y registro de intentos. Microsoft profundiza en Azure, aplicaciones, DevOps y KQL; Dynatrace en navegación, DQL, trazas, infraestructura y experiencia de usuario. Cada persona practica también lo necesario para revisar a su pareja.

Al recibir el entorno identificar tenant/suscripción/proyecto, recursos, repositorios, servicios, reloj/zona horaria, permisos y herramientas disponibles. No modificar configuración para una pregunta que solo pide identificar un dato. Registrar las reglas reales de la plataforma antes de gastar intentos.

## Reparto durante la competencia

1. Hacer un inventario breve: ID, dominio, dependencia, puntos conocidos, intentos, costo de pistas y quién la toma.
2. Cada pareja puede investigar dos preguntas distintas en paralelo. El revisor interviene cuando una candidata necesita contraste, especialmente si hay un solo intento o ambigüedad de formato.
3. El integrante 1 coordina bloqueos, duplicaciones y ayuda cruzada sin detener todo el equipo para aprobar cada operación.
4. Mantener un único responsable de envío por pregunta. Acordarlo en el canal humano en tiempo real y registrar el claim; un archivo Git por sí solo no impide que dos personas envíen simultáneamente.

Atender primero preguntas con camino de evidencia claro y dependencia útil. No adoptar un orden rígido por plataforma o dificultad. Si una investigación se estanca, escribir qué se comprobó y cambiar temporalmente de pregunta o pedir revisión cruzada. Tiempo de preparación y tiempo estimado no equivalen a reglas oficiales de puntuación.

## Antes de responder

Entender qué pide exactamente: nombre visible o ID, servicio o recurso, valor absoluto o porcentaje, unidad, decimal, intervalo, instancia y formato. Buscar evidencia en el entorno correcto y comprobar que responde al enunciado, no a una pregunta parecida.

Una candidata sólida tiene valor concreto, fundamento reproducible y ninguna ambigüedad material pendiente. Evitar porcentajes de confianza inventados; explicar observaciones y dudas. Para un solo intento, revisión cruzada si está disponible. Si la respuesta es inequívoca, no añadir burocracia innecesaria.

## Intentos y pistas

No usar el primer intento como prueba de una conjetura. Tras una respuesta incorrecta detener reenvíos automáticos: comprobar feedback, formato, alcance temporal, fuente y presupuesto real restante. Cambiar la hipótesis solo con nueva evidencia; no repetir el mismo valor por esperanza ni enumerar variantes para agotar posibilidades.

Intentar sin pistas primero. Una pista puede resultar conveniente si desbloquea más puntos de los que cuesta, pero esa comparación necesita costos reales. El humano decide usarla explícitamente; registrar pista, costo observado y efecto. No afirmar que ninguna pista debe usarse jamás, ni que existe una penalización por error si no se ha comunicado.

## Después de responder

Confirmar al chat exactamente lo enviado, feedback, consumo de intento, intentos restantes visibles, puntos observados y pistas usadas. El asistente registra en la carpeta de esa pregunta y sincroniza los archivos pertinentes. Si falla el push, conservar el commit/archivo y señalar pendiente de sincronización; no declarar publicado.

El registro no debe impedir tomar la siguiente pregunta: guardar pronto lo mínimo verificable y ampliar el diagnóstico posteriormente. Una respuesta incorrecta es útil para evitar repetirla, no se borra del historial. Los puntos no se calculan como intentos multiplicados por un valor supuesto; la plataforma es la fuente de la puntuación real.

## Comandos rápidos

[Palabras del coordinador](comandos-coordinador.md): FACIL, SCRIPT (SCRIP), DIAGNOSTICO y DIFICIL. Activan flujos de análisis/skills; modelos, subagentes y worktrees se usan según disponibilidad y ahorro de tiempo. No autorizan envíos ni pistas. Nuevas skills de GitHub quedan pendientes de recibir e incorporar.

## Aclaración de formato confirmada por el equipo

Formato de respuestas: según la aclaración del equipo, mayúsculas/minúsculas y puntuación de estilo no requieren revisión ni preguntas adicionales por defecto. Si el enunciado exige un formato, cumplirlo exactamente: números en lugar de palabras, cantidad de decimales, punto o coma decimal, unidad, porcentaje o estructura indicada. No agregar texto, unidades ni signos que el formato excluya. No alterar puntuación que cambie el valor o la sintaxis de IDs, URLs, código o consultas. El historial conserva exactamente lo enviado, sin normalizarlo.
