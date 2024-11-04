class TelaMesa():
    def tela_opcoes(self):
        print("-------- MESA ----------")
        print("Escolha a opcao")
        print("1 - Incluir mesa")
        print("2 - Excluir mesa")
        print("3 - Listar mesa")
        print("4 - Alocar Cliente")
        print("5 - Desalocar Cliente")
        print("0 - Retornar")


        opcao = int(input("Escolha a opcao: "))
        while opcao > 5 or opcao < 0:
              opcao = int(input("Escolha errada, selecione um valor válido: "))
      
        return opcao
    

    def mensagem_de_criação(self, numero):
         print(f"-----Mesa Numero {numero} criada!")

    def mensagem_de_exclusão(self, numero):
         print(f"---Mesa {numero} excluida")
         
    def mostrar_mesa(self,dados_mesa):
         print(f"Mesa Numero {dados_mesa['numero']}, Clientes na Mesa: {dados_mesa['clientes']}")

    def seleciona_mesa(self):
        numero = input("Numero da mesa que deseja selecionar: ")
        return numero
    
    def mostra_mensagem(self, msg):
        print(msg)
         
