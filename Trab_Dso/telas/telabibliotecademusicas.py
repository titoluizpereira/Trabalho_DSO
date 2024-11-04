class TelaBibliotecaDeMusica:
    def mostrar_opcoes(self) -> int:
        print("\n=== Relatório de Músicas ===")
        print("1. Relatório de Artista mais cantado")
        print("2. Relatório de Gênero mais cantado")
        print("3. Relatório de Idioma mais cantado")
        print("0. Retornar")
        
        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                if 0 <= opcao <= 3:
                    return opcao
                print("Por favor, insira uma opção válida (0-6)")
            except ValueError:
                print("Por favor, insira um número válido")

    def mostrar_mensagem(self, mensagem: str):
        print(f"\n{mensagem}")
