"""Conserva eventos confirmados; no envía respuestas ni usa Git automáticamente."""
import argparse
from datetime import datetime
import json
import math
from pathlib import Path
import re

ID = re.compile(r'[A-Za-z0-9][A-Za-z0-9_-]{0,79}\Z')


def validar(evento):
    if not isinstance(evento, dict):
        raise ValueError('El evento debe ser un objeto JSON')
    for key in ('evento_id', 'envio_id', 'reto_id', 'pregunta_id'):
        if not isinstance(evento.get(key), str) or not ID.fullmatch(evento[key]):
            raise ValueError(f'{key}: identificador seguro obligatorio')
        if evento[key].startswith('REEMPLAZAR'):
            raise ValueError('No registrar una plantilla como intento real')
    if evento.get('confirmacion_humana') is not True:
        raise ValueError('Se requiere confirmación humana de un envío observado')
    if evento.get('dominio') not in ('microsoft', 'dynatrace'):
        raise ValueError('Dominio desconocido')
    if evento.get('tipo_evento') not in ('envio', 'feedback'):
        raise ValueError('tipo_evento debe ser envio o feedback')
    if evento.get('resultado') not in ('correcta', 'incorrecta', 'pendiente', 'error-plataforma'):
        raise ValueError('Resultado desconocido')
    for key in ('actor', 'confirmado_por'):
        if evento.get(key) not in ('I1', 'I2', 'I3', 'I4'):
            raise ValueError(f'{key}: integrante inválido')
    if not isinstance(evento.get('respuesta_enviada'), str) or not evento['respuesta_enviada'].strip():
        raise ValueError('Falta respuesta enviada exacta')
    if not isinstance(evento.get('feedback'), str) or not evento['feedback'].strip():
        raise ValueError('Falta feedback o explicación de que sigue pendiente')
    if evento.get('fuente_feedback') not in ('confirmacion_humana', 'captura', 'observacion_directa'):
        raise ValueError('Indicar origen del feedback')
    if not isinstance(evento.get('fecha'), str):
        raise ValueError('Fecha ISO obligatoria')
    if evento['tipo_evento'] == 'feedback' and (
        not isinstance(evento.get('actualiza_evento_id'), str)
        or not ID.fullmatch(evento['actualiza_evento_id'])
    ):
        raise ValueError('Feedback requiere ID seguro del evento actualizado')
    try:
        fecha = datetime.fromisoformat(evento['fecha'].replace('Z', '+00:00'))
    except (KeyError, TypeError, ValueError):
        raise ValueError('Fecha ISO obligatoria') from None
    if fecha.utcoffset() is None:
        raise ValueError('La fecha debe incluir zona/offset')
    if evento.get('consumio_intento') is not None and type(evento['consumio_intento']) is not bool:
        raise ValueError('Consumo de intento: true, false o null')
    remaining = evento.get('intentos_restantes_observados')
    if remaining is not None and (type(remaining) is not int or remaining < 0):
        raise ValueError('Restantes debe ser entero no negativo o null')
    for key in ('pistas_usadas', 'evidencias'):
        if not isinstance(evento.get(key), list) or not all(isinstance(x, str) for x in evento[key]):
            raise ValueError(f'{key}: lista de textos obligatoria')
    for key in ('costo_pistas_observado', 'cambio_puntos_observado'):
        number = evento.get(key)
        if number is not None and type(number) not in (int, float):
            raise ValueError(f'{key}: número observado o null')
        if number is not None and not math.isfinite(number):
            raise ValueError(f'{key}: número finito obligatorio')
    return evento


def registrar(root, evento):
    validar(evento)
    root = Path(root).resolve()
    folder = root / 'retos' / evento['dominio'] / evento['reto_id'] / 'preguntas' / evento['pregunta_id'] / 'intentos'
    if not folder.resolve().is_relative_to(root):
        raise ValueError('Destino fuera del repositorio')
    destination = folder / (evento['evento_id'] + '.json')
    if destination.exists():
        previous = json.loads(destination.read_text(encoding='utf-8'))
        if previous == evento:
            return destination  # Confirmación repetida: idempotente, sin otro intento.
        raise ValueError('ID de evento existente con contenido distinto; conservar historial')
    records = {p.stem: json.loads(p.read_text(encoding='utf-8')) for p in folder.glob('*.json')}
    same_submission = [e for e in records.values() if e.get('envio_id') == evento['envio_id']]
    if evento['tipo_evento'] == 'envio':
        if same_submission:
            raise ValueError('envio_id ya existe; feedback posterior usa tipo_evento feedback')
        if evento.get('actualiza_evento_id') is not None:
            raise ValueError('Un envío inicial no actualiza otro evento')
    else:
        original = records.get(evento.get('actualiza_evento_id'))
        if not original or original.get('envio_id') != evento['envio_id']:
            raise ValueError('Feedback debe referenciar evento existente del mismo envío')
        if original.get('respuesta_enviada') != evento['respuesta_enviada']:
            raise ValueError('Feedback no puede cambiar la respuesta enviada')
    folder.mkdir(parents=True, exist_ok=True)
    with destination.open('x', encoding='utf-8', newline='\n') as handle:
        json.dump(evento, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write('\n')
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archivo', required=True, type=Path, help='JSON preparado con la confirmación real del humano')
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        evento = json.loads(args.archivo.read_text(encoding='utf-8-sig'))
        if not isinstance(evento, dict):
            raise ValueError('El evento debe ser un objeto JSON')
        destination = registrar(args.repo, evento)
    except (ValueError, OSError) as error:
        parser.exit(2, f'No registrado: {error}\n')
    print(f'Guardado: {destination.relative_to(args.repo.resolve())}')
    print('Actualizar ficha/estado y sincronizar a GitHub según el protocolo; este comando no hace push.')


if __name__ == '__main__':
    main()
