from products import Producto
from exceptions import ProductoNoEncontrado

class Inventario:
    def __init__(self):
        # Diccionario con al menos 3 productos (código: objeto Producto)
        self.productos = {
            "P01": Producto("P01", "Laptop", 10),
            "P02": Producto("P02", "Mouse", 25),
            "P03": Producto("P03", "Teclado", 15)
        }

    def retirar(self, codigo, cantidad):
        # Validación: verificar que el código exista en el inventario
        if codigo not in self.productos:
            # raise detiene el flujo y lanza ProductoNoEncontrado hacia main.py
            raise ProductoNoEncontrado(f"El producto '{codigo}' no existe.")

        # Llama a retirar() del producto; si falla, la excepción se propaga sola
        producto = self.productos[codigo]
        return producto.retirar(cantidad)