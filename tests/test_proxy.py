import unittest
from src.proxy import ProxyAplicacion

class TestProxyAplicacion(unittest.TestCase):
    def test_actualizar_lider(self):
        proxy = ProxyAplicacion(nodos=[])
        proxy.actualizar_lider(1)
        self.assertEqual(proxy.lider_id, 1)

    def test_redirect_request(self):
        proxy = ProxyAplicacion(nodos=[])
        proxy.actualizar_lider(1)
        respuesta = proxy.redirect_request(1, "escritura", {"key": "value"})
        self.assertIn("Nodo 1", respuesta)

    def test_redireccion_sin_lider(self):
        proxy = ProxyAplicacion(nodos=[])
        respuesta = proxy.redirect_request(cliente_id=1, tipo_solicitud="lectura", datos={"key": "valor"})
        self.assertIn("Error", respuesta)
