from cliente import Cliente

class Fila_Karaoke:
    def __init__(self):
        self.__fila_karaoke = [[]]
        self.__cliente = {}

    def adicionar_pedido(self, nome_cliente):
        if nome_cliente not in self.__cliente:
            novo_cliente = Cliente(nome_cliente)
            self.__cliente[nome_cliente] = novo_cliente
            self.__fila_karaoke[0].append(novo_cliente)
        else:
            cliente_existente = self.__cliente[nome_cliente]
            cliente_existente.aumentar_prioridade()
            
            while len(self.__fila_karaoke) <= cliente_existente.prioridade:
                self.__fila_karaoke.append([])
            self.__fila_karaoke[cliente_existente.prioridade].append(cliente_existente)

    def remover_pedido(self):
        for nivel_prioridade in self.__fila_karaoke:
            if nivel_prioridade:
                proximo_Cliente = nivel_prioridade.pop(0)
                return proximo_Cliente.nome
        return None 
