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

if __name__ == "__main__":
    unittest.main()
