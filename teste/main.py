from controladorCliente import Controlador
from tela import TelaCliente

TelaCliente1 = TelaCliente()
if __name__ == "__main__":
    Controlador(TelaCliente1).inicializa_tela()