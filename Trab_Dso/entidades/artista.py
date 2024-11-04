from .atributoscategorias import AtributosCategorias

class Artista(AtributosCategorias):
    def __init__(self, nome_artista):
        super().__init__(nome_artista)

    @property
    def contador(self):
        return self._contador

    def __str__(self):
        return f"Artista: {self.nome}"
