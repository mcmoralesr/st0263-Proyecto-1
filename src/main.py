from nodo_raft import NodoRaft
from proxy import ProxyAplicacion
from cliente import Cliente
import time
import random

def simular_raft():
    # Crear nodos Raft
    nodos = [NodoRaft(i) for i in range(1, 6)]

    # Inicializar proxy con nodos
    proxy = ProxyAplicacion(nodos)
    
    # Inicializar líder
    lider = random.choice(nodos)
    lider.estado = "Líder"
    lider.lider_actual = lider.id
    proxy.actualizar_lider(lider.id)
    print(f"Nodo {lider.id} comienza como líder.\n")

    # Crear clientes
    cliente1 = Cliente(cliente_id=1)
    cliente2 = Cliente(cliente_id=2)

    # Cliente envía solicitudes
    print(cliente1.enviar_solicitud(proxy, "lectura", {"key": "valor1"}))
    print(cliente2.enviar_solicitud(proxy, "escritura", {"key": "valor2"}))

    # Simular fallo del líder
    print("\nSimulando fallo del líder...\n")
    lider.simular_caida()
    proxy.actualizar_lider(None)

    # Elección de nuevo líder
    print("\nIniciando nueva elección...\n")
    for nodo in nodos:
        if nodo.estado == "Seguidor" and nodo.activo:
            nodo.iniciar_eleccion()
            if nodo.estado == "Líder":
                proxy.actualizar_lider(nodo.id)
                break

    # Cliente envía solicitudes con el nuevo líder
    print(cliente1.enviar_solicitud(proxy, "lectura", {"key": "nuevo_valor"}))
    print(cliente2.enviar_solicitud(proxy, "escritura", {"key": "otro_valor"}))


if __name__ == "__main__":
    simular_raft()
