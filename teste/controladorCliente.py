from cliente import Cliente
from teste.tela import TelaCliente

class Controlador():
    def __init__(self, tela: TelaCliente):
        self.__clientes = []
        self.__tela = tela

    

    def incluir_cliente(self):
        dados_cliente = self.__tela.receber_dados()
        NovoCliente = Cliente(dados_cliente["nome"], dados_cliente["cpf"], dados_cliente["email"], dados_cliente["telefone"])
        self.__clientes.append(NovoCliente)
    
    def alterar_cliente(self):
        self.lista_cliente()
        cpf_selecionado = self._tela.seleciona_cliente()
        cliente = self.buscar_cliente_cpf(cpf_selecionado)

        if cliente is not None:
            novos_dados_cliente = self.__tela.pegar_dados_cliente()
            cliente.nome = novos_dados_cliente["nome"]
            cliente.cpf = novos_dados_cliente["cpf"]
            cliente.email = novos_dados_cliente["email"]
            cliente.telefone = novos_dados_cliente["telefone"]
            self.lista_cliente()
        else:
            self.__tela.mostrar_mensagem("CLIENTE INFORMADO NÃO CADASTRADO!!!!!!!")

    def excluir_cliente(self):
        self.lista_cliente()
        cpf_cliente = self.__tela.seleciona_cliente()
        cliente = self.buscar_cliente_cpf(cpf_cliente)

        if cliente is not None:
            self.__clientes.remove(cliente)
            self.lista_cliente()
        else:
            self.__tela.mostrar_mensagem("CLIENTE INFORMADO NÃO CADASTRADO!!!!!!!")

    def buscar_cliente_cpf(self, cpf: int):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
        return None


    def lista_cliente(self):
        for cliente in self.__clientes:
            self.__tela.mostrar_cliente({"nome": cliente.nome,"cpf": cliente.cpf, "email" : cliente.email, "telefone": cliente.telefone})


    # def retornar(self):
    #     self.__controlador_sistema 

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cliente, 2: self.alterar_cliente, 3: self.excluir_cliente, 4:self.lista_cliente }
        continua = True
        while continua:
            lista_opcoes[self.__tela.opcoes]()

    def inicializa_tela(self):
        self.__abre_tela()

        

