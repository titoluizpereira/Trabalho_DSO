from .filakaraoke import Fila_Karaoke 
from .musica import Musica
from .bibliotecademusicas import BibliotecaDeMusicas
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
    def cpf(self, cpf: int):
        self.__cpf = cpf

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email: str):
        self.__email = email
    
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone: int):
        self.__telefone = telefone
        
    @property
    def musicas_cantadas(self):
        return self.__musicas_cantadas
    
    @musicas_cantadas.setter
    def musicas_cantadas(self, musicas_cantadas: int):
        self.__musicas_cantadas = musicas_cantadas

    @property
    def prioridade_fila(self):
        return self.__prioridade_fila
    
    @prioridade_fila.setter
    def prioridade_fila(self, prioridade_fila: int):
        self.__prioridade_fila = prioridade_fila

    def pedir_musica(self, biblioteca_de_musicas: BibliotecaDeMusicas, fila: Fila_Karaoke):
        if isinstance(biblioteca_de_musicas, BibliotecaDeMusicas) and isinstance(fila, Fila_Karaoke):
                buscar_criterio = int(input("Gostaria de buscar música por: Gênero[1], Artista[2],Idioma[3]? ou Apenas Nome[4]?"))
                if buscar_criterio == 1:
                    criterio = "Gênero"
                elif buscar_criterio == 2:
                    criterio = "Artista"
                elif buscar_criterio == 3:
                    criterio = "Idioma"
                else:
                    criterio = "Apenas_Nome"

 
                buscar_filtro = str(input("Nome da música (caso não queira filtrar por nome ou ver todas as musicas, deixe em branco):"))
                if not buscar_filtro.strip() : 
                    buscar_filtro = ""
                musica = biblioteca_de_musicas.buscar_musica(criterio, buscar_filtro)
                
                fila.adicionar_na_fila(self, musica)
            
    def adicionar_musica_biblioteca(self,bibliotecademusicas : BibliotecaDeMusicas, musica: Musica ):
        if isinstance(bibliotecademusicas, BibliotecaDeMusicas) and isinstance(musica, Musica):    
            bibliotecademusicas.adicionar_musica(musica)

    def remover_musica(self, musica: Musica, fila: Fila_Karaoke):
        if isinstance(fila, Fila_Karaoke):
            fila.remover_da_fila(self)

    def verificar_posicao_na_fila(self, fila: Fila_Karaoke):
        if isinstance(fila, Fila_Karaoke):
            fila.ver_posicao(self)

    def __str__(self):
        return self.__nome
