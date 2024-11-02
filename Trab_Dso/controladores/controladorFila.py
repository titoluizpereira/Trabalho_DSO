from ..entidades.filakaraoke import Fila_Karaoke
from ..telas.telafila_karaoke import Telafila

class ControladorFila:
    #controlador_sistema
    def __init__(self,  controlador_sistema ):
        self.__controlador_sistema = controlador_sistema
        self.__tela = Telafila()
        self.__fila = Fila_Karaoke()

    def abrir_tela(self):
        opcoes = {
            1: self.mostrar_fila,
            2: self.proximo_cantar,
            3: self.adicionar_pedido,
            4: self.remover_pedido,
            0: self.sair
        }

        while True:
            try:
                opcao = self.__tela.tela_opcoes()
                if opcao in opcoes:
                    opcoes[opcao]()
                else:
                    self.__tela.mostra_menssagem("Opcao Invalida")
            except ValueError:
                self.__tela.mostra_menssagem("Insira um numero valido")
            except Exception as e:
                self.__tela.mostra_menssagem(f"An error occurred: {str(e)}")

    def inicializa_tela(self):
        self.abrir_tela()
        
    def mostrar_fila(self):
        if not self.__fila.fila_karaoke:
            self.__tela.mostra_menssagem("fila está vazia")
            return
            
        for i, (cliente, musica) in enumerate(self.__fila.fila_karaoke):
            self.__tela.mostrar_fila(i, cliente, musica)

    def proximo_cantar(self):
        proximo = self.__fila.proximo_cantar()
        if proximo:
            cliente, musica = proximo
            self.__tela.proximo_cantar(cliente, musica)
        else:
            self.__tela.mostra_menssagem("fila está vazia")

    def adicionar_pedido(self):
        try:

            dados_cliente = self.__controlador_sistema.cliente_controlador.lista_cliente()
            dados_cliente = self.__tela.receber_cpf_cliente()
            dados_musica= self.__controlador_sistema.musica_controlador.listar_musica()
            dados_musica= self.__tela.receber_id_musica()
            

            cliente = self.__controlador_sistema.cliente_controlador.buscar_cliente_cpf(dados_cliente)
            musica = self.__controlador_sistema.musica_controlador.controlador_biblioteca.buscar_musica(int(dados_musica))
            
            if cliente and musica:
                self.__fila.adicionar_na_fila(cliente, musica)
                self.__tela.mostra_menssagem("Pedido adicionado")
            else:
                self.__tela.mostra_menssagem("Cliente ou Música não encontrados")
        except Exception as e:
            self.__tela.mostra_menssagem(f"Error adding request: {str(e)}")

    def remover_pedido(self):
        try:
            dados_cliente = self.__tela.get_client_data()
            cliente = self.__controlador_sistema._SystemController__client_controller.buscar_cliente_cpf(dados_cliente["cpf"])
            
            if cliente:
                if self.__fila.remover_fila(cliente):
                    self.__tela.mostra_menssagem("Pedido removido")
                else:
                    self.__tela.mostra_menssagem("Cliente não está na fila")
            else:
                self.__tela.mostra_menssagem("Cliente não encontrado")
        except Exception as e:
            self.__tela.mostra_menssagem(f"Error removing request: {str(e)}")

    def sair(self):
        self.__controlador_sistema.abrir_tela()