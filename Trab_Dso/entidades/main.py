from ..controladores.controladorCliente import ControladorCliente
from ..telas.telacliente import TelaCliente
from ..controladores.controladorMesa import ControladorMesa #
from ..telas.telamesa import TelaMesa
TelaCliente1 = TelaCliente()
# if __name__ == "__main__":
#     ControladorCliente(TelaCliente1).inicializa_tela()
ControladorCliente1 = ControladorCliente(TelaCliente1)
TelaMesa1 = TelaMesa()
if __name__ == "__main__":


    ControladorMesa(TelaMesa1).inicializa_tela()
