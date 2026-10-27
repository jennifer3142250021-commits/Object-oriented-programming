import tkinter as tk
from tkinter import messagebox

class LoginView:

    def __init__(self, root):
        self.root = root

        
        self.root.title("Sistema de Acceso")

       
        self.root.geometry("480x420")

        
        self.root.configure(bg="#EBF5FB")

        self.root.resizable(False, False)

       
        self.titulo = tk.Label(
            root,
            text="INICIAR SESIÓN",
            font=("Segoe UI", 20, "bold"),
            bg="#EBF5FB",
            fg="#2471A3"
        )
        self.titulo.pack(pady=25)

       
        self.lbl_email = tk.Label(
            root,
            text="Correo electrónico:",
            font=("Segoe UI", 11),
            bg="#EBF5FB",
            fg="#2E4053"
        )
        self.lbl_email.pack()

        self.entry_email = tk.Entry(
            root,
            width=38,
            font=("Segoe UI", 11),
            relief="flat",
            bg="#FFFFFF",
            fg="#1C2833",
            insertbackground="#1C2833"
        )
        self.entry_email.pack(pady=8)

        self.lbl_password = tk.Label(
            root,
            text="Contraseña:",
            font=("Segoe UI", 11),
            bg="#EBF5FB",
            fg="#2E4053"
        )
        self.lbl_password.pack()

        self.entry_password = tk.Entry(
            root,
            width=38,
            font=("Segoe UI", 11),
            show="*",
            relief="flat",
            bg="#FFFFFF",
            fg="#1C2833",
            insertbackground="#1C2833"
        )
        self.entry_password.pack(pady=8)

        # PERSONALIZAR 7 y 8: Botones
        self.btn_login = tk.Button(
            root,
            text="Ingresar",
            width=24,
            bg="#AED6F1",
            fg="#1B4F72",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            cursor="hand2"
        )
        self.btn_login.pack(pady=20)

        self.btn_register = tk.Button(
            root,
            text="Crear cuenta",
            width=24,
            bg="#A9DFBF",
            fg="#196F3D",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2"
        )
        self.btn_register.pack()

    def obtener_datos(self):
        email = self.entry_email.get().strip()
        password = self.entry_password.get()

        return email, password

    def limpiar_campos(self):
        self.entry_email.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje, parent=self.root)
        else:
            messagebox.showinfo(titulo, mensaje, parent=self.root)