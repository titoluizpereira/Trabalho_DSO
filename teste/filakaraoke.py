from cliente import Cliente
from musica import Musica
class Fila_Karaoke:
    def __init__(self):
        self.__fila_karaoke = []


    def adicionar_na_fila(self, cliente: Cliente, musica: Musica):
        novo_pedido = [cliente, musica]
        tamanho = len(self.__fila_karaoke)

        if len(self.__fila_karaoke) == 0:
            self.__fila_karaoke.append(novo_pedido)
        else:
            for pedidos in self.__fila_karaoke:
                if pedidos[0].prioridade_fila < cliente.prioridade_fila:
                    posicao = self.__fila_karaoke.index(pedidos)
                    self.__fila_karaoke.insert(posicao, novo_pedido)
                    break
        cliente.prioridade_fila -= 1

    def ver_posicao(self, cliente: Cliente):
        for pedidos in self.__fila_karaoke:
            if pedidos[0] == cliente:
                return self.__fila_karaoke.index(pedidos)

    def remover_da_fila(self, cliente: Cliente):
        for pedidos in self.__fila_karaoke:
            if pedidos[0] == cliente:
                self.__fila_karaoke.remove(pedidos)

    def recomecar_prioridade(self):
        for pedidos in self.__fila_karaoke:
            pedidos[0].prioridade_fila = 0