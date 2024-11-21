class EntradaLog:
    def __init__(self, index, term, comando):
        self.index = index
        self.term = term
        self.comando = comando

    def __repr__(self):
        return f"[EntradaLog index={self.index}, term={self.term}, comando={self.comando}]"
