from controladores.controladorCliente import ControladorCliente
from telas.telacliente import TelaCliente

TelaCliente1 = TelaCliente()
if __name__ == "__main__":
    ControladorCliente(TelaCliente1).inicializa_tela()