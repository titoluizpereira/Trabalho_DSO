from abc import ABC, abstractmethod

class AtributosCategorias(ABC):
    def __init__(self, nome):
        self._nome = nome
        self._lista = []
        self._contador = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def lista(self):
        return self._lista

    @property
    def contador(self):
        return self._contador

    def adicionar_musica(self, musica):
        if musica not in self._lista:
            self._lista.append(musica)

    def incrementar_contador(self):
        self._contador += 1

    @abstractmethod
    def __str__(self):
        pass
