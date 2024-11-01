class TelaMesa():
    def tela_opcoes(self):
        print("-------- CLIENTES ----------")
        print("Escolha a opcao")
        print("1 - Incluir mesa")
        print("2 - Excluir mesa")
        print("3 - Listar mesa")


        opcao = int(input("Escolha a opcao: "))
        while opcao > 3 or opcao < 1:
              opcao = int(input("Escolha errada, selecione um valor válido: "))
      
        return opcao
    

    def mensagem_de_criação(self, numero):
         print(f"-----Mesa Numero {numero} criada!")

    def mensagem_de_exclusão(self, numero):
         print(f"---Mesa {numero} excluida")
         
    def mostrar_mesa(self,dados_mesa):
         print(f"Mesa Numero {dados_mesa['numero']}, Clientes na Mesa: {dados_mesa["clientes"]}")

    def seleciona_mesa(self):
        numero = input("Numero da mesa que deseja selecionar: ")
        return numero
    
    def mostra_mensagem(self, msg):
        print(msg)
         
