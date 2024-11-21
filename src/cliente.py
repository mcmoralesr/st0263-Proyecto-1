class Cliente:
    def __init__(self, cliente_id):
        """
        Inicializa un cliente con un identificador único.
        """
        self.cliente_id = cliente_id

    def enviar_solicitud(self, proxy, tipo_solicitud, datos):
        """
        Envía una solicitud al proxy de aplicación.

        Args:
            proxy (ProxyAplicacion): El proxy que redirige las solicitudes.
            tipo_solicitud (str): Tipo de la solicitud (lectura/escritura).
            datos (dict): Datos asociados a la solicitud.

        Returns:
            str: Respuesta del sistema.
        """
        print(f"[Cliente {self.cliente_id}] Enviando {tipo_solicitud}: {datos}")
        respuesta = proxy.redirect_request(self.cliente_id, tipo_solicitud, datos)
        self.recibir_respuesta(respuesta)
        return respuesta

    def recibir_respuesta(self, respuesta):
        """
        Recibe y muestra una respuesta del sistema.

        Args:
            respuesta (str): Respuesta del sistema.
        """
        print(f"[Cliente {self.cliente_id}] Recibió respuesta: {respuesta}")
