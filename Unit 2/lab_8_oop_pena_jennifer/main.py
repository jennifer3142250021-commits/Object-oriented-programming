import tkinter as tk
from models.login_models import UserModel
from view.login_view import LoginView
from models.products_model import Authentication

class System:
    def __init__(self):
        self.root = tk.Tk()
        self.modelo = UserModel()
        self.vista = LoginView(self.root)
        self.controlador = Authentication(self.modelo, self.vista)

    def iniciar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = System()
    app.iniciar()