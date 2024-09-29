from musica import Musica
class BibliotecaDeMusicas:
    def __init__(self):
        self.__musicas = []
        self.__artistas = []
        self.__idiomas = []
        self.__generos = []

    @property
    def musicas(self):
        return self.__musicas
    
    @musicas.setter
    def musicas(self, musicas: Musica):
        self.__musicas.append(musicas)

    @property
    def artistas(self):
        return self.__artistas
    
    @artistas.setter
    def artistas(self, artistas: Artista):
        self.__artistas.append(artistas)

    @property
    def idiomas(self):
        return self.__idiomas
    
    @idiomas.setter
    def idiomas(self, idiomas: Idioma):
        self.__idiomas.append(idiomas)

    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, genero: Genero):
        self.__genero.append(genero)

    def buscar_musica(self, criterio: str, filtro: str):
        if criterio == "Gênero":
            musicas = self.buscar_genero
        elif criterio == "Artista":
            musicas = self.buscar_artista
        else:
            musicas = self.buscar_idioma
        

        

    def buscar_genero(self, genero: Genero):
        cont = 0
        for genero in self.__generos:
            print(f"{genero} [{cont}]")
            cont =+ 1
        escolha = int(input("Insira o id do gênero escolhido: "))
        return self.__generos[escolha]
    
    def buscar_artista(self, artista):
        pass

    
    def buscar_idioma(self, idioma):
        pass