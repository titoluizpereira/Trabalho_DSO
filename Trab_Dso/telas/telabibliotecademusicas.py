class TelaBibliotecaDeMusica:
    def mostrar_mensagem(self, mensagem: str):
        print(f"\n{mensagem}")

    def mostrar_lista_musicas(self, lista_musicas: list):
        print("\n=== Biblioteca de Músicas ===")
        if not lista_musicas:
            print("Nenhuma música disponível")
            return
        
        for musica in lista_musicas:
            print(f"\nTítulo: {musica.titulo}")
            print(f"Artista: {musica.artista}")
            print(f"Gênero: {musica.genero}")
            print(f"Idioma: {musica.idioma}")
            print(f"Código: {musica.codigo}")
            print(f"Vezes Tocada: {musica.numero_de_vezes_tocada}")