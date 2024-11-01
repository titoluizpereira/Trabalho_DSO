from cliente import Cliente

class Mesa:
    def __init__(self, numero:int):
        self.__numero = numero
        self.__clientes = []

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero: int):
        self.__numero = numero

    @property
    def clientes(self):
        return self.__clientes
    
    @clientes.setter
    def clientes(self, clientes: int):
        self.__clientes.append(clientes)


    def alocar_cliente(self, cliente):
        if isinstance(cliente, Cliente):
            if cliente not in self.__clientes:
                self.__clientes.append(cliente)
            else:
                return print('Cliente já adicionado')
        else:
            return print('Apenas objetos da classe clientes são permitidos como parametro')
        
    def desalocar_cliente(self, cliente):
        if isinstance(cliente, Cliente):
            if cliente in self.__clientes:
                self.__clientes.remove(cliente)
            else:
                return print('Cliente não está nessa mesa')
        else:
            return print('Apenas objetos da classe clientes são permitidos como parametro')
        