# Helper de registro local

Python 3.9+; solo biblioteca estándar. Leer [protocolo](../docs/protocolo-respuestas.md) y preparar el JSON de [la plantilla](../retos/plantillas/evento-ejemplo.json) con datos reales confirmados. La plantilla no se acepta sin completar y confirmar.

```text
python scripts/registrar_intento.py --archivo RUTA-AL-EVENTO.json
```

Guarda el evento en la carpeta de dominio/reto/pregunta. No responde en la plataforma, no descuenta intentos, no calcula puntaje, no cambia README/estado ni hace commit/push. El asistente realiza esas actualizaciones y sincroniza después siguiendo el protocolo. Sin acceso de escritura, entrega el JSON propuesto y su ruta.

`evento_id` es único por registro; `envio_id` identifica un envío real. Feedback posterior conserva envio_id y respuesta, usa un nuevo evento_id, tipo_evento feedback y actualiza_evento_id del evento anterior. Una confirmación repetida idéntica no crea otro registro; mismo ID con datos distintos se rechaza. Resultados desconocidos permanecen pendientes y consumo/puntos desconocidos permanecen null.

La confirmación humana del JSON documenta lo que el usuario comunicó; el script no autentica ni verifica por sí solo esa conversación o la plataforma. IDs de pregunta seguros deben mapearse a IDs oficiales en la ficha si contienen caracteres no admitidos. No usar la raíz alternativa `--repo` para escribir fuera del checkout elegido.

Comprobar el helper:

```text
python -m unittest discover -s tests -v
```

Los tests usan carpetas temporales de laboratorio y no generan intentos reales ni acceden a la plataforma.
