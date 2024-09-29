from musica import Musica

class Genero:
    def __init__(self, nome_genero):
        self.__nome_genero = nome_genero
        self.__lista_genero = []  
        self.__contador_genero = 0  

    @property
    def nome_genero (self):
        return self.__nome_genero
    
    @nome_genero.setter
    def nome_genero(self, nome_genero):
        self.__nome_genero = nome_genero

    @property
    def lista_genero(self):
        return self.__lista_genero

    @property
    def contador_genero(self):
        return self.__contador_genero

    def _adicionar_musica(self, musica):
        if musica not in self.__lista_genero:
            self.__lista_genero.append(musica)