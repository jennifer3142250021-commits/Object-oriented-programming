from inventory import Inventario
from exceptions import ErrorInventario

def main():
    inventario = Inventario()

    # try intenta ejecutar la entrada de datos y el retiro del inventario
    try:
        codigo = input("Ingresa el código del producto (ej. P01, P02, P03): ").strip()
        # int() lanzará ValueError automáticamente si el usuario ingresa texto
        cantidad = int(input("Ingresa la cantidad a retirar: "))

        stock_restante = inventario.retirar(codigo, cantidad)

    # except captura si el usuario escribió texto en lugar de un número entero
    except ValueError:
        print("Error: Debes ingresar un número entero válido para la cantidad.")

    # except captura cualquiera de nuestras excepciones personalizadas (ErrorInventario)
    except ErrorInventario as e:
        print(f"Error de inventario: {e}")

    # else se ejecuta ÚNICAMENTE si no ocurrió ninguna excepción en el bloque try
    else:
        print(f"Retiro exitoso. Stock restante: {stock_restante}")

if __name__ == "__main__":
    main()