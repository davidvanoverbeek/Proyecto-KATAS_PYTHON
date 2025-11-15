# Ejercicio 35:
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente=True):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            raise ValueError("Saldo insuficiente")

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            otro_usuario.agregar_dinero(cantidad)
        else:
            raise ValueError("Saldo insuficiente para transferencia")

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

if __name__ == "__main__":
    alicia = UsuarioBanco("Alicia", 100)
    bob = UsuarioBanco("Bob", 50)
    bob.agregar_dinero(20)
    bob.transferir_dinero(alicia, 80)
    alicia.retirar_dinero(50)
    print(f"Alicia: {alicia.saldo}, Bob: {bob.saldo}")  # Alicia: 150, Bob: -10
