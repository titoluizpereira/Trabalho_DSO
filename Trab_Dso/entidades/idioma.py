from .musica import Musica

class Idioma:
    def __init__(self, nome_idioma):
        self.__nome_idioma = nome_idioma
        self.__lista_idioma = []  
        self.__contador_idioma = 0  

    @property
    def nome_idioma (self):
        return self.__nome_idioma
    
    @nome_idioma.setter
    def nome_idioma(self, nome_idioma):
        self.__nome_idioma = nome_idioma

    @property
    def lista_idioma(self):
        return self.__lista_idioma

    @property
    def contador_idioma(self):
        return self.__contador_idioma

    def _adicionar_musica(self, musica):
        if musica not in self.__lista_idioma and isinstance(musica, Musica):
            self.__lista_idioma.append(musica)
    
    def incrementar_contador_idioma(self):
            self.__contador_idioma += 1

    
    def __str__(self):
        return self.__nome_idioma
