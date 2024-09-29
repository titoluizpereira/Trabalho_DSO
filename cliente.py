from fila import Fila_Karaoke, Fila
from musica import Musica
class Cliente:
    def __init__(self, nome):
        self.__nome = nome
        self.__musicas_cantadas = 0
        self.__prioridade_fila = 0

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: int):
        self.__nome = nome

    @property
    def musicas_cantadas(self):
        return self.__musicas_cantadas
    
    @musicas_cantadas.setter
    def musicas_cantadas(self, musicas_cantadas: int):
        self.__musicas_cantadasas = musicas_cantadas

    @property
    def prioridade_fila(self):
        return self.__prioridade_fila
    
    @prioridade_fila.setter
    def prioridade_fila(self, prioridade_fila: int):
        self.__prioridade_fila = prioridade_fila

    def pedir_musica(self, musica: Musica, fila: Fila):
        novo_pedido = [self, musica]
        fila.adcionar_na_fila(novo_pedido)
    
    def remover_da_fila(self, musica: Musica, fila: Fila):
        
