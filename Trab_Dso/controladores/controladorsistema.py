from ..controladores import controladorCliente, controladorFila, controladorMesa, controladorMusica, controladorBibliotecaDeMusica 

class Systemcontrolador:
    def __init__(self):
        self.__cliente_controlador = ControladorCliente(self)
        self.__musicacontrolador = ControladorMusica(self)
        self.__fila_controlador = ControladorFila(self)
        self.__mesa_controlador = ControladorMesa(self)
        self.__tela = TelaSistema()


    def abri(self):
        self.abrir_tela()

    def abrir_tela(self):
        opcoes = {
            1: self.__cliente_controlador.abrir_tela,
            2: self.__musica_controlador.abrir_tela,
            3: self.__fila_controlador.abrir_tela,
            4: self.__mesa_controlador.abrir_tela,
            0: self.fechar_sistema
        }

        while True:
            try:
                opcao = self.__tela.mostrar_opcoes()
                if opcao in opcoes:
                    opcoes[opcao]()
                else:
                    self.__tela.mostra_menssagem("Opção invalida")
            except ValueError:
                self.__tela.mostra_menssagem("Por favor coloque um valor valido")


    def fechar_sistema(self):
        self.__tela.mostra_menssagem("Fechando ...")
    