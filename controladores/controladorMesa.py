from entidades.mesa import Mesa
from telas.telacliente import TelaMesa
from entidades.main import ControladorCliente, TelaCliente1
class ControladorMesa():
    def __init__(self, controladormesa):
        self.__mesas = []
        self.__tela = TelaMesa()
        self.__controladormesa = controladormesa

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
            self.__mesas.remove(mesa)
            self.lista_mesa()
            self.__tela.mensagem_de_exclusão(numero_mesa)
        else:
            self.__tela.mostra_mensagem("MESA NÃO EXISTE!!!!!!!")

    def buscar_mesa_por_numero(self, numero):
        for mesa in self.__mesas:
            if mesa.numero == numero: 
                return mesa
    
    def lista_mesa(self):
        for mesa in self.__mesas:
            self.__tela.mostrar_mesa({"numero" : mesa.numero, "clientes": mesa.cliente})


    def abre_tela(self):
        listaopcoes = {1: self.incluir_mesa, 2: self.excluir_mesa, 3: self.lista_mesa }
        continua = True
        
        while continua:
            listaopcoes[self.__tela.tela_opcoes()]()

    def inicializa_tela(self):
        self.abre_tela()

    def alocar_cliente(self):
        self.lista_mesa()
        numero_mesa = self.__tela.seleciona_mesa()
        mesa = self.buscar_mesa_por_numero(numero_mesa)

        ControladorCliente.lista_cliente()
        cliente = TelaCliente1.seleciona_cliente()
        cliente = ControladorCliente.selecionar_cliente(cliente)

        mesa.clientes.append(cliente)





