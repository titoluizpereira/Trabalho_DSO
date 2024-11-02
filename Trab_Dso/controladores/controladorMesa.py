from ..entidades.mesa import Mesa
from ..telas.telamesa import TelaMesa

class ControladorMesa():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__mesas = []
        self.__tela = TelaMesa()


    def incluir_mesa(self):
        numero = len(self.__mesas)

        novamesa = Mesa(numero = numero+1)
        self.__mesas.append(novamesa)
        self.__tela.mensagem_de_criação(numero+1)

    def excluir_mesa(self):
        self.lista_mesa()
        numero_mesa = self.__tela.seleciona_mesa()
        mesa = self.buscar_mesa_por_numero(numero_mesa)

        if mesa is not None:
            print("chegou ate aqui")
            self.__mesas.remove(mesa)
            self.lista_mesa()
            self.__tela.mensagem_de_exclusão(numero_mesa)
        else:
            self.__tela.mostra_mensagem("MESA NÃO EXISTE!!!!!!!")

    def buscar_mesa_por_numero(self, numero):
        for mesa in self.__mesas:
            if int(mesa.numero) == int(numero): 
                return mesa
            else:
                print(f"mesa de nuero {mesa.numero} não corresponde ao valor passado {numero}")
    
    def lista_mesa(self):
        for mesa in self.__mesas:
            self.__tela.mostrar_mesa({"numero" : mesa.numero, "clientes": mesa.clientes})


    def abrir_tela(self):
        listaopcoes = {1: self.incluir_mesa, 2: self.excluir_mesa, 3: self.lista_mesa, 4:self.alocar_cliente, 5: self.desalocar_cliente, 0: self.sair }
        continua = True
        
        while continua:
            listaopcoes[self.__tela.tela_opcoes()]()

    def inicializa_tela(self):
        self.abrir_tela()

    def alocar_cliente(self):
        self.lista_mesa()
        numero_mesa = self.__tela.seleciona_mesa()
        mesa = self.buscar_mesa_por_numero(numero_mesa)
        from ..entidades.main import ControladorCliente1, TelaCliente1
        ControladorCliente1.lista_cliente()
        cliente = TelaCliente1.seleciona_cliente()
        cliente = ControladorCliente1.buscar_cliente_cpf(cliente)

        mesa.clientes.append(cliente)

    def desalocar_cliente(self):
        self.lista_mesa()
        numero_mesa = self.__tela.seleciona_mesa()
        mesa = self.buscar_mesa_por_numero(numero_mesa)
        from ..entidades.main import ControladorCliente1, TelaCliente1
        ControladorCliente1.lista_cliente()
        cliente = TelaCliente1.seleciona_cliente()
        cliente = ControladorCliente1.buscar_cliente_cpf(cliente)

        mesa.clientes.remove(cliente)

    def sair(self):
        self.__controlador_sistema.abrir_tela()


