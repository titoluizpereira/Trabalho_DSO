class Musica():
    def __init__(self, titulo, artista, genero, idioma):
        self.__titulo = titulo
        self.__artista = artista
        self.__genero = genero
        self.__idioma = idioma
        self.__ja_cantada = False
        self.__contador_musica = 0
   
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def artista(self):
        return self.__artista

    @artista.setter
    def artista(self, artista):
        self.__artista = artista

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero):
        self.__genero = genero

    @property
    def idioma(self):
        return self.__idioma

    @idioma.setter
    def idioma(self, idioma):
        self.__idioma = idioma

    @ja_cantada.setter
    def ja_cantada(self, ja_cantada):
        self.__ja_cantada = True
    
    def contar_musica(self):
        self.contar_musica += 1