from fila import Fila
from musica import Musica
from bibliotecademusicas import BibliotecaDeMusicas
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

    def pedir_musica(self, biblioteca_de_musicas: BibliotecaDeMusicas, fila: Fila):
        opcao_musica = int(input("Caso cliente queira buscar a música digite 1, caso queira adicionar música digite 2:"))
        if opcao_musica == 1:
            buscar_criterio = int(input("Gostaria de buscar música por: Gênero[1], Artista[2] ou Idioma[3]?"))
            
            if buscar_criterio == 1:
                criterio = "Gênero"
            elif buscar_criterio == 2:
                criterio = "Artista"
            else:
                criterio = "Idioma"
            
            buscar_filtro = str(input("Nome da música (caso não queira filtrar por nome, deixe em branco):"))
            
            musica = biblioteca_de_musicas.buscar_musica(criterio, buscar_filtro)
        
        else:
            musica = biblioteca_de_musicas.adicionar_musica()

            
        
        
        novo_pedido = [self, musica]
        fila.adcionar_na_fila(novo_pedido)
    
    def remover_da_fila(self, musica: Musica, fila: Fila):
        pass