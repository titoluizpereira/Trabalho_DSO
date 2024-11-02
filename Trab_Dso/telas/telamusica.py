from ..entidades.artista import Artista
from ..entidades.idioma import Idioma
from ..entidades.genero import Genero   

class TelaMusica:
    def mostrar_opcoes(self) -> int:
        print("\n=== Gerenciamento de Músicas ===")
        print("1. Registrar Nova Música")
        print("2. Buscar Música")
        print("3. Listar Todas as Músicas")
        print("4. Listar por Artista")
        print("5. Listar por Gênero")
        print("6. Listar por Idioma")
        print("0. Retornar")
        
        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                if 0 <= opcao <= 6:
                    return opcao
                print("Por favor, insira uma opção válida (0-6)")
            except ValueError:
                print("Por favor, insira um número válido")

    def pegar_dados_musica(self) -> dict:
        print("\n=== Registro de Música ===")
        titulo = input("Título: ")
        # nome_artista = input("Nome do Artista: ")
        # nome_genero = input("Gênero: ")
        # nome_idioma = input("Idioma: ")
        
        #isso não pode ser feito aqui e verificar se não há um objeto desses já criado
        # artista = Artista(nome_artista)
        # genero = Genero(nome_genero)
        # idioma = Idioma(nome_idioma)
        
        return {
            "titulo": titulo,
            # "artista": artista,
            # "genero": genero,
            # "idioma": idioma
        }

    #Funções para mostrar as categorias e dar opção de escolhar
    def escolher_ou_adicionar_artista(self, lista):
        cont = 0
        print("Lista de Artistas:")
        for categoria in lista:
            print(f"{categoria.nome_artista} - Id: {cont}")
            cont+=1
        escolha = input("Escolha o id de um artista, caso queira adicionar novo digite o novo nome do artista: ")
        return escolha
    def escolher_ou_adicionar_genero(self, lista):
        cont=0
        print("Lista de Generos")
        for categoria in lista:
            print(f"{categoria.nome_genero} - Id: {cont}")
            cont+=1
        escolha = input("Escolha o id de um genero, caso queira adicionar novo digite o novo nome do genero: ")
        return escolha
    
    def escolher_ou_adicionar_idioma(self, lista):
        cont=0
        print("Lista de idiomas")
        for categoria in lista:
            print(f"{categoria.nome_idioma} - Id: {cont}")
            cont+=1
        escolha = input("Escolha o id de um idioma, caso queira adicionar novo digite o novo nome do idioma: ")
        return escolha

















    def mostrar_musica(self, musica):
        print("\n=== Detalhes da Música ===")
        print(f"Título: {musica.titulo}")
        print(f"Código: {musica.codigo}")
        print(f"Artista: {musica.artista.nome_artista}")
        print(f"Gênero: {musica.genero.nome_genero}")
        print(f"Idioma: {musica.idioma.nome_idioma}")
        print(f"Vezes tocadas: {musica.contador}")

    def mostrar_mensagem(self, mensagem: str):
        print(f"\n{mensagem}")
