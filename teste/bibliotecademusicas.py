from musica import Musica
from genero import Genero
from idioma import Idioma
from artista import Artista


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
        lista_de_musicas = []
        if criterio == "Gênero":
            opcao_escolhida = self.buscar_genero
            for musica in self.__musicas:
                if musica.genero == opcao_escolhida and filtro in musica.titulo:
                    lista_de_musicas.append(musica)
        elif criterio == "Artista":
            opcao_escolhida = self.buscar_artista
            for musica in self.__musicas:
                if musica.artista == opcao_escolhida and filtro in musica.titulo:
                    lista_de_musicas.append(musica)
        elif criterio == "Idioma":
            opcao_escolhida  = self.buscar_idioma
            for musica in self.__musicas:
                if musica.idioma == opcao_escolhida and filtro in musica.titulo:
                    lista_de_musicas.append(musica)
        else:
            for musica in self.__musicas:
                if filtro in musica.titulo:
                    lista_de_musicas.append(musica)
        
      
        cont = 0
        for musica in lista_de_musicas:
            print(f"{musica} {cont}")
        escolha_musica = int(input("Selecione o id da música desejada: "))
        return lista_de_musicas[escolha_musica]

        

        

               
    def buscar_genero(self, genero: Genero, filtro: str):
        cont = 0
        for genero in self.__generos:
            print(f"{genero} [{cont}]")
            cont += 1
        escolha = int(input("Insira o id do gênero escolhido: "))
        return self.__artistas[escolha]

    
    def buscar_artista(self, artista):
        cont = 0
        for artista in self.__artistas:
            print(f"{artista} [{cont}]")
            cont += 1
        escolha = int(input("Insira o id do artistas/banda escolhido: "))
        return self.__artistas[escolha]

    
    def buscar_idioma(self, idioma):
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

    def remover_musica(self, musica: Musica):
        if isinstance(musica, Musica):
            if musica in self.__musicas:
                self.__musicas.remove(musica)


    def verificar_se_ja_foi_cantada(self, musica):
        if musica.__ja_cantada == True:
            return True
        return False
