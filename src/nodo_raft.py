class NodoRaft:
    def __init__(self, id, term=0, estado="Seguidor"):
        """
        Inicializa un nodo Raft con un identificador único, término inicial y estado.
        """
        self.id = id
        self.term = term
        self.estado = estado  # Puede ser 'Seguidor', 'Candidato' o 'Líder'
        self.log = []
        self.votos_recibidos = 0
        self.lider_actual = None
        self.activo = True  # Indica si el nodo está activo
        self.followers = []  # Lista de nodos seguidores

    def simular_caida(self):
        """
        Simula la caída del nodo, marcándolo como inactivo.
        """
        print(f"[Nodo {self.id}] Simulando caída...")
        self.activo = False

    def reincorporarse(self):
        """
        Simula la reincorporación del nodo, marcándolo como activo.
        """
        print(f"[Nodo {self.id}] Reincorporándose...")
        self.activo = True

    def iniciar_eleccion(self):
        """
        Inicia un proceso de elección de líder. Incrementa el término y solicita votos.
        """
        print(f"[Nodo {self.id}] Iniciando elección...")
        self.term += 1
        self.estado = "Candidato"
        self.votos_recibidos = 1  # El nodo vota por sí mismo

        for nodo in self.followers:
            if nodo.activo and nodo.request_vote(self.id, self.term, len(self.log), self.term):
                self.votos_recibidos += 1

        if self.votos_recibidos > len(self.followers) // 2:
            print(f"[Nodo {self.id}] Ha sido elegido como líder.")
            self.estado = "Líder"
            self.lider_actual = self.id

    def request_vote(self, candidato_id, term, last_log_index, last_log_term):
        """
        Responde a una solicitud de voto.

        Args:
            candidato_id (int): ID del candidato solicitando el voto.
            term (int): Término del candidato.
            last_log_index (int): Último índice de log del candidato.
            last_log_term (int): Último término de log del candidato.

        Returns:
            bool: True si el voto es otorgado, False en caso contrario.
        """
        if not self.activo:
            return False

        if term > self.term:
            self.term = term
            self.estado = "Seguidor"
            print(f"[Nodo {self.id}] Votando por Nodo {candidato_id}")
            return True

        return False

    def append_entries(self, leader_id, term, prev_log_index, prev_log_term, entries, leader_commit):
        """
        Recibe entradas del líder y las aplica al log del nodo.

        Args:
            leader_id (int): ID del líder que envía las entradas.
            term (int): Término actual del líder.
            prev_log_index (int): Índice de la entrada previa al log.
            prev_log_term (int): Término de la entrada previa al log.
            entries (list): Nuevas entradas del log.
            leader_commit (int): Índice de compromiso del líder.

        Returns:
            bool: True si las entradas se aplicaron correctamente, False si hubo conflicto.
        """
        if term < self.term:
            print(f"[Nodo {self.id}] Rechazando entradas: término del líder {term} menor que término actual {self.term}")
            return False

        # Aceptar entradas del líder
        self.term = term
        self.lider_actual = leader_id
        self.log.extend(entries)
        print(f"[Nodo {self.id}] Entradas aceptadas y aplicadas: {entries}")
        return True
