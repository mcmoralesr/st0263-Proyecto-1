class ProxyAplicacion:
    def __init__(self, nodos):
        """
        Inicializa el proxy con la lista de nodos Raft disponibles.

        Args:
            nodos (list): Lista de nodos Raft en el sistema.
        """
        self.nodos = nodos
        self.lider_id = None

    def actualizar_lider(self, nuevo_lider_id):
        """
        Actualiza el líder actual del sistema.

        Args:
            nuevo_lider_id (int): ID del nuevo líder.
        """
        self.lider_id = nuevo_lider_id
        print(f"[Proxy] Líder actualizado a Nodo {nuevo_lider_id}")

    def redirect_request(self, cliente_id, tipo_solicitud, datos):
        """
        Redirige las solicitudes al nodo líder o maneja errores si no hay un líder.

        Args:
            cliente_id (int): ID del cliente que envía la solicitud.
            tipo_solicitud (str): Tipo de la solicitud (lectura/escritura).
            datos (dict): Datos asociados a la solicitud.

        Returns:
            str: Respuesta al cliente.
        """
        if self.lider_id is None:
            return f"[Proxy] Error: No hay líder disponible para manejar la solicitud."

        if tipo_solicitud == "lectura":
            return f"[Proxy] Redirigido al Nodo {self.lider_id} (lectura): {datos}"
        elif tipo_solicitud == "escritura":
            return f"[Proxy] Enviando a Nodo {self.lider_id} (escritura): {datos}"
        else:
            return f"[Proxy] Tipo de solicitud no reconocido: {tipo_solicitud}"
