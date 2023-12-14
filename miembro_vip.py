
from cliente import Cliente
from usuario import Usuario

class MiembroVIP(Cliente, Usuario):
    def __init__(self, nombre, email, direccion, saldo, username, password, descuento):
        Cliente.__init__(self, nombre, email, direccion, saldo)
        Usuario.__init__(self, username, password)
        self.descuento = descuento

    def aplicar_descuento(self, monto):
        return monto - (monto * self.descuento / 100)
