
class Cliente:
    def __init__(self, nombre, email, direccion, saldo):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.saldo = saldo

    def __str__(self):
        return f'Cliente {self.nombre}, Email: {self.email}, Dirección: {self.direccion}, Saldo: {self.saldo}'

    def realizar_compra(self, monto):
        if monto > self.saldo:
            return "Saldo insuficiente"
        self.saldo -= monto
        return f"Compra realizada con éxito. Saldo actual: {self.saldo}"

    def actualizar_datos(self, nombre=None, email=None, direccion=None):
        if nombre:
            self.nombre = nombre
        if email:
            self.email = email
        if direccion:
            self.direccion = direccion
        return "Datos actualizados con éxito"
