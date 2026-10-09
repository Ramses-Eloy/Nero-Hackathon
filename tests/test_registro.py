import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('registro', Path(__file__).resolve().parents[1] / 'scripts' / 'registrar_intento.py')
registro = importlib.util.module_from_spec(spec)
spec.loader.exec_module(registro)


class RegistroTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.event = {
            'evento_id': 'LAB-E1', 'envio_id': 'LAB-S1', 'tipo_evento': 'envio',
            'fecha': '2026-10-08T12:00:00-05:00', 'dominio': 'microsoft',
            'reto_id': 'LAB-R1', 'pregunta_id': 'LAB-Q1', 'actor': 'I1',
            'confirmado_por': 'I1', 'confirmacion_humana': True,
            'respuesta_enviada': 'dato-de-laboratorio', 'resultado': 'pendiente',
            'feedback': 'No llegó feedback concluyente', 'fuente_feedback': 'confirmacion_humana',
            'consumio_intento': None, 'intentos_restantes_observados': None,
            'pistas_usadas': [], 'costo_pistas_observado': None,
            'cambio_puntos_observado': None, 'evidencias': [], 'actualiza_evento_id': None,
        }

    def tearDown(self):
        self.temp.cleanup()

    def test_pending_and_unknown_budget_are_preserved(self):
        path = registro.registrar(self.root, self.event)
        saved = json.loads(path.read_text(encoding='utf-8'))
        self.assertEqual(saved['resultado'], 'pendiente')
        self.assertIsNone(saved['consumio_intento'])
        self.assertIsNone(saved['intentos_restantes_observados'])

    def test_incorrect_result_is_not_dropped(self):
        self.event.update(resultado='incorrecta', feedback='Plataforma mostró incorrecta', consumio_intento=True, intentos_restantes_observados=1)
        path = registro.registrar(self.root, self.event)
        self.assertEqual(json.loads(path.read_text(encoding='utf-8'))['resultado'], 'incorrecta')

    def test_duplicate_is_idempotent_but_cannot_overwrite_history(self):
        path = registro.registrar(self.root, self.event)
        self.assertEqual(registro.registrar(self.root, copy.deepcopy(self.event)), path)
        changed = dict(self.event, resultado='correcta')
        with self.assertRaises(ValueError):
            registro.registrar(self.root, changed)
        self.assertEqual(len(list(self.root.rglob('*.json'))), 1)

    def test_feedback_update_is_not_a_second_submission(self):
        registro.registrar(self.root, self.event)
        later = dict(self.event, evento_id='LAB-E2', tipo_evento='feedback', resultado='correcta', feedback='Correcta confirmado', actualiza_evento_id='LAB-E1')
        registro.registrar(self.root, later)
        events = [json.loads(p.read_text(encoding='utf-8')) for p in self.root.rglob('*.json')]
        self.assertEqual(sum(e['tipo_evento'] == 'envio' for e in events), 1)
        self.assertEqual({e['envio_id'] for e in events}, {'LAB-S1'})

    def test_requires_confirmation_and_safe_path(self):
        for change in ({'confirmacion_humana':False}, {'reto_id':'../escape'}, {'fecha':'2026-10-08T12:00:00'}, {'intentos_restantes_observados':True}, {'cambio_puntos_observado':float('nan')}):
            with self.subTest(change=change), self.assertRaises(ValueError):
                registro.registrar(self.root, dict(self.event, **change))
        self.assertFalse(list(self.root.rglob('*.json')))

    def test_repeated_submission_and_changed_feedback_answer_rejected(self):
        registro.registrar(self.root, self.event)
        with self.assertRaises(ValueError):
            registro.registrar(self.root, dict(self.event, evento_id='LAB-E2'))
        with self.assertRaises(ValueError):
            registro.registrar(self.root, dict(self.event, evento_id='LAB-E3', tipo_evento='feedback', actualiza_evento_id='LAB-E1', respuesta_enviada='otra'))


if __name__ == '__main__':
    unittest.main()
