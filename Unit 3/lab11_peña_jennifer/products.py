from exceptions import CantidadInvalida, StockInsuficiente

class Producto:
    def __init__(self, codigo, nombre, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.stock = stock

    def retirar(self, cantidad):
        # Validación: verificar que sea un entero positivo (evitando booleanos)
        if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad <= 0:
            # raise lanza la excepción personalizada si la cantidad es inválida
            raise CantidadInvalida("La cantidad debe ser un número entero mayor a 0.")

        # Validación: verificar que haya suficiente stock disponible
        if cantidad > self.stock:
            # raise lanza la excepción si se excede el stock
            raise StockInsuficiente(f"Stock insuficiente. Disponible: {self.stock}")

        # Si las validaciones pasan, se descuenta y retorna el stock restante
        self.stock -= cantidad
        return self.stock