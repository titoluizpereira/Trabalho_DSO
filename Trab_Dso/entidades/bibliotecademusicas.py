from .musica import Musica
from .genero import Genero
from .idioma import Idioma
from .artista import Artista


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
    def generos(self):
        return self.__generos
    
    @generos.setter
    def generos(self, genero: Genero):
        self.__generos.append(genero)

    def buscar_musica_por_codigo(self, codigo):
        for musica in self.__musicas:
            if musica.codigo == codigo:
                return musica
        

        
    def buscar_genero(self):
        cont = 0
        for genero in self.__generos:
            print(f"{genero} [{cont}]")
            cont += 1
        escolha = int(input("Insira o id do gênero escolhido: "))
        return self.__generos[escolha]

    
    def buscar_artista(self):
        cont = 0
        for artista in self.__artistas:
            print(f"{artista} [{cont}]")
            cont += 1
        escolha = int(input("Insira o id do artistas/banda escolhido: "))
        return self.__artistas[escolha]

    
    def buscar_idioma(self):
        cont = 0
        for idioma in self.__idiomas:
            print(f"{idioma} [{cont}]")
            cont +=1
        escolha = int(input("Insira o id do idioma escolhido: "))
        return self.__idiomas[escolha]
    


    def adicionar_musica(self, musica: Musica):
        if isinstance(musica, Musica):
            if musica not in self.__musicas:
                self.__musicas.append(musica)
            if musica.genero not in self.__generos:
                self.__generos.append(musica.genero)
            if musica.idioma not in self.__idiomas:
                self.__idiomas.append(musica.idioma)
            if musica.artista not in self.__artistas:
                self.__artistas.append(musica.artista)
            return "musica adicionada"



    def remover_musica(self, musica: Musica):
        if isinstance(musica, Musica):
            if musica in self.__musicas:
                self.__musicas.remove(musica)


    def verificar_se_ja_foi_cantada(self, musica):
        if musica.__ja_cantada == True:
            return True
        return False

    def buscar_musica_por_codigo(self,codigo):
        for musica in self.__musicas:
            if musica.codigo == codigo:
                return musica
