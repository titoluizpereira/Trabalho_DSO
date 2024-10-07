class Telacliente():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- CLIENTES ----------")
    print("Escolha a opcao")
    print("1 - Incluir cliente")
    print("2 - Alterar cliente")
    print("3 - Excluir cliente")
    print("4 - Alterar cliente")
    # print("0 - Retornar")

    
    opcao = int(input("Escolha a opcao: "))
    while opcao > 4 or opcao < 1:
          opcao = int(input("Escolha errada, selecione um valor válido: "))
      
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def receber_dados(self):
    print("-------- DADOS cliente ----------")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

    if isinstance(nome, str) and isinstance(telefone, str) and isinstance(cpf, str) and isinstance(email, str):
      return {"nome": nome, "cpf": cpf, "email": email, "telefone": telefone}
      

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostrar_cliente(self, dados_cliente):
    print("NOME DO cliente: ", dados_cliente["nome"])
    print("CPF DO cliente: ", dados_cliente["cpf"])
    print("EMAIL DO cliente", dados_cliente["email"])
    print("FONE DO cliente: ", dados_cliente["telefone"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_cliente(self):
    cpf = input("CPF do cliente que deseja selecionar: ")
    return cpf

  def mostra_mensagem(self, msg):
    print(msg)