from typing import Optional, List
from ..telas.telamusica import TelaMusica
from ..entidades.musica import Musica
from ..entidades.artista import Artista
from ..entidades.genero import Genero
from ..entidades.idioma import Idioma

class ControladorMusica:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaMusica()
        self.__controlador_biblioteca = self.__controlador_sistema.bibliotecademusicas_controlador

    def abrir_tela(self):
        opcoes = {
            1: self.registrar_musica,
            2: self.buscar_musica,
            3: self.listar_musica,
            4: self.listar_por_artista,
            5: self.listar_por_genero,
            6: self.listar_por_idioma,
            0: self.sair
        }

        while True:
            try:
                opcao = self.__tela.mostrar_opcoes()
                if opcao in opcoes:
                    opcoes[opcao]()
                else:
                    self.__tela.mostrar_mensagem("Opção Inválida")
            except ValueError:
                self.__tela.mostrar_mensagem("Por favor, insira um número válido")
            except Exception as e:
                self.__tela.mostrar_mensagem(f"Um erro ocorreu: {str(e)}")

    def registrar_musica(self):

        try:
            codigo = self.__controlador_biblioteca.retornar_ultimo_codigo()
            dados_musica = self.__tela.pegar_dados_musica() #ID É O SISTEMA QUE DEFINE
            
            #FAZER FUNÇÃO INTERMEDIARIA PAR MOSTRAR CATEGORIAS JÁ CADASTRADAS E DAR OPCAO DE CRiAR NOVO
            
            opcoes_de_artista = self.__controlador_biblioteca.lista_de_artista()
            opcoes = self.__tela.escolher_ou_adicionar_artista(opcoes_de_artista)
            if opcoes.isdigit():
                artista = self.__controlador_biblioteca.retornar_artista_por_id(id)
                dados_musica["artista"] = artista
            else:
                novo_artista = Artista(opcoes)
                dados_musica["artista"] = novo_artista
            
            opcoes_genero = self.__controlador_biblioteca.lista_de_genero()
            opcoes = self.__tela.escolher_ou_adicionar_genero(opcoes_genero)
            if opcoes.isdigit():
                genero = self.__controlador_biblioteca.retornar_genero_por_id(id)
                dados_musica["genero"] = genero
            else:
                novo_genero = Genero(opcoes)
                dados_musica["genero"] = novo_genero

            opcoes_idioma = self.__controlador_biblioteca.lista_de_idioma()
            opcoes = self.__tela.escolher_ou_adicionar_idioma(opcoes_idioma)
            if opcoes.isdigit():
                idioma = self.__controlador_biblioteca.retornar_idioma_por_id(id)
                dados_musica["idioma"] = idioma
            else:
                novo_idioma = Idioma(opcoes)
                dados_musica["idioma"] = novo_idioma


            nova_musica = Musica(
                codigo,
                dados_musica["titulo"], 
                dados_musica["artista"],
                dados_musica["genero"],
                dados_musica["idioma"]
            )
            if self.__controlador_biblioteca.adicionar_musica(nova_musica):
                self.__tela.mostrar_mensagem("Música registrada com sucesso")
            else:
                self.__tela.mostrar_mensagem("Música já existe")
        except Exception as e:
            self.__tela.mostrar_mensagem(f"Erro registrando música: {str(e)}")

    def buscar_musica(self, codigo: str) -> Musica:
        return self.__controlador_biblioteca.achar_musica_por_codigo(codigo)

    def listar_musica(self):
        lista_musica = self.__controlador_biblioteca.lista_musica()
        if not lista_musica:
            self.__tela.mostrar_mensagem("Sem Músicas registrada")
            return
        
        for musica in lista_musica:
            self.__tela.mostrar_musica(musica)

    def listar_por_artista(self, artista: Artista):
        lista_musica = self.__controlador_biblioteca.pegar_musica_por_artista(artista)
        self.__mostrar_musica_por_filtro(lista_musica)

    def listar_por_genero(self, genero: Genero):
        lista_musica = self.__controlador_biblioteca.pegar_musica_por_genero(genero)
        self.__mostrar_musica_por_filtro(lista_musica)

    def listar_por_idioma(self, idioma: Idioma):
        lista_musica = self.__controlador_biblioteca.pegar_musica_por_idioma(idioma)
        self.__mostrar_musica_por_filtro(lista_musica)

    def __mostrar_musica_por_filtro(self, lista_musica):
        if not lista_musica:
            self.__tela.mostrar_mensagem("Música não encontrada")
            return
        
        for musica in lista_musica:
            self.__tela.mostrar_musica(musica)

    def sair(self):
        self.__controlador_sistema.abrir_tela()