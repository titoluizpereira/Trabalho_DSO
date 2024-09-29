class Artista:
    def __init__(self, nome_artista):
        self.__nome_artista = nome_artista
        self.__lista_artista = []  
        self.__contador_artista = 0  

    @property
    def nome_artista(self):
        return self.__nome_artista
    
    @nome_artista.setter
    def nome_artista(self, nome_artista):
        self.__nome_artista = nome_artista

    @property
    def lista_artista(self):
        return self.__lista_artista

    @property
    def contador_artista(self):
        return self.__contador_artista

    def _adicionar_musica(self, musica):
        if musica not in self.__lista_artista:
            self.__lista_artista.append(musica)