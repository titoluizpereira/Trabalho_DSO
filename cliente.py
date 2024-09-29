from fila import Fila_Karaoke, Fila
from musica import Musica
class Cliente:
    def __init__(self, nome, cpf, email, telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone
        self.__musicas_cantadas = 0
        self.__prioridade_fila = 0
        

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def nome(self, cpf: int):
        self.__cpf = cpf

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def nome(self, email: str):
        self.__email = email
    
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def nome(self, telefone: int):
        self.__telefone = telefone
        
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
        
