class Telafila():
    def tela_opcoes(self):
        print("-------- FILA KARAOKE ----------")
        print("Escolha a opcao")
        print("1 - Mostrar Fila")
        print("2 - Passar a vez pro proximo")
        print("3 - Adicionar Pedido")
        print("4 - Remover Pedido")
        print("0 - Retornar")

    def mostrar_fila(self, posicao, cliente, musica):
        print(f'Posição: {posicao}, Cliente: {cliente.nome} Cpf: {cliente.cpf}, Musica: {musica.titulo}')

    def proximo_cantar(self, cliente, musica):
        print("---Proximo a cantar---")
        print(f"{cliente.nome} ira cantar {musica.titulo}")
    
    def receber_cpf_cliente(self):
        cpf = input("Cpf do cliente: ")
        return cpf
    
    def receber_id_musica(self):
        id= input("Id da musica: ")
        return id
    
    def mostra_mensagem(self, msg):
        print(msg)

    