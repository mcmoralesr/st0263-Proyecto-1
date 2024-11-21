import unittest
from src.nodo_raft import NodoRaft
from src.entrada_log import EntradaLog

class TestNodoRaft(unittest.TestCase):
    def test_request_vote(self):
        nodo = NodoRaft(1)
        self.assertTrue(nodo.request_vote(2, 1, 0, 0))
        self.assertEqual(nodo.term, 1)
        self.assertEqual(nodo.estado, "Seguidor")

    def test_append_entries(self):
        nodo = NodoRaft(1)
        entries = [EntradaLog(1, 1, "Comando1")]
        self.assertTrue(nodo.append_entries(2, 1, 0, 0, entries, 0))
        self.assertEqual(len(nodo.log), 1)
        self.assertEqual(nodo.log[0].comando, "Comando1")

    def test_reeleccion_conflicto(self):
        nodo1 = NodoRaft(1)
        nodo2 = NodoRaft(2)
        nodo3 = NodoRaft(3)

        nodo1.followers = [nodo2, nodo3]
        nodo2.followers = [nodo1, nodo3]
        nodo3.followers = [nodo1, nodo2]

        nodo1.iniciar_eleccion()
        nodo2.iniciar_eleccion()

        lideres = [nodo for nodo in [nodo1, nodo2, nodo3] if nodo.estado == "Líder"]
        self.assertEqual(len(lideres), 1)

    def test_reincorporacion(self):
        nodo1 = NodoRaft(1)
        nodo2 = NodoRaft(2)
        nodo3 = NodoRaft(3)

        nodo1.followers = [nodo2, nodo3]
        nodo2.followers = [nodo1, nodo3]
        nodo3.followers = [nodo1, nodo2]

        nodo2.simular_caida()
        self.assertFalse(nodo2.activo)

        nodo2.reincorporarse()
        self.assertTrue(nodo2.activo)

    def test_logs_inconsistentes(self):
        nodo = NodoRaft(1)
        nodo.term = 2
        nodo.log = [EntradaLog(index=1, term=1, comando="Comando1")]

        entries = [EntradaLog(index=2, term=1, comando="Comando2")]
        result = nodo.append_entries(leader_id=2, term=1, prev_log_index=1, prev_log_term=2, entries=entries, leader_commit=1)

        self.assertFalse(result)
        self.assertEqual(len(nodo.log), 1)

    def test_compromiso_consistente(self):
        nodo = NodoRaft(1)
        nodo.log = [EntradaLog(index=1, term=1, comando="Comando1")]
        nodo.term = 2

        result = nodo.append_entries(leader_id=2, term=2, prev_log_index=1, prev_log_term=1, entries=[], leader_commit=1)
        self.assertTrue(result)
