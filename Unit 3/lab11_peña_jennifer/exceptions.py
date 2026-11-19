#A store needs to deduct products from its inventory. The system must prevent invalid operations and communicate errors appropiately, without terminating execution unexpectedly.

# Custom exceptions
class ErrorInventario(Exception):
    pass
class ProductoNoEncontrado(ErrorInventario):
    pass
class CantidadInvalida(ErrorInventario):
    pass
class StockInsuficiente(ErrorInventario):
    pass
