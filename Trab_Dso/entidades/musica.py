class Musica():
    def __init__(self,codigo, titulo, artista, genero, idioma):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__artista = artista
        self.__genero = genero
        self.__idioma = idioma
        self.__ja_cantada = False
        self.__contador = 0
   
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def artista(self):
        return self.__artista

    @property
    def genero(self):
        return self.__genero

    @property
    def idioma(self):
        return self.__idioma

    @property
    def ja_cantada(self):
        return self.__ja_cantada
    
    @ja_cantada.setter
    def ja_cantada(self, ja_cantada):
        self.__ja_cantada = True
    
    @property
    def contador(self):
        return self.__contador

    def incrementar_contador(self):
        self.__contador += 1
        self.__genero.incrementar_contador_genero()
        self.__artista.incrementar_contador_artista()
        self.__idioma.incrementar_contador_idioma()

    
    def __str__(self):
        return self.__titulo