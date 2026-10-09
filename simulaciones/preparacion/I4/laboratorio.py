"""LAB I4: cálculo y formato; no representa telemetría ni un envío CTF."""
from decimal import Decimal
import json
from pathlib import Path
import re

fallos, solicitudes = 3, 12
porcentaje = Decimal(fallos) * 100 / Decimal(solicitudes)
punto = format(porcentaje, '.2f')
coma = punto.replace('.', ',')
assert porcentaje == Decimal('25')
assert punto == '25.00' and re.fullmatch(r'\d+\.\d{2}', punto)
assert coma == '25,00' and re.fullmatch(r'\d+,\d{2}', coma)
assert '%' not in punto + coma
evidencia = {
    'tipo': 'LABORATORIO', 'integrante': 'I4',
    'fuente': 'Caso sintético autorizado por el usuario; no entorno competitivo',
    'fallos': fallos, 'solicitudes': solicitudes,
    'formula': '3 / 12 * 100', 'punto': punto, 'coma': coma,
    'comprobacion': 'OK: valor 25, dos decimales, separador exacto, sin %',
    'envio_ctf': False,
}
destino = Path(__file__).with_name('evidencia.json')
contenido = json.dumps(evidencia, ensure_ascii=False, indent=2) + '\n'
if destino.exists():
    assert destino.read_text(encoding='utf-8') == contenido, 'No sobrescribir evidencia distinta'
else:
    destino.write_text(contenido, encoding='utf-8')
print(contenido, end='')
