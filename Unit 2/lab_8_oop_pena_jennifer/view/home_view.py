import tkinter as tk
from tkinter import messagebox

class RegisterView:

    def __init__(self, root):
        self.ventana = tk.Toplevel(root)

        # PERSONALIZAR 1: Título de la ventana
        self.ventana.title("Registro de Usuarios")

        # PERSONALIZAR 2: Dimensiones de la ventana (Más alta para que se vean los botones)
        self.ventana.geometry("500x620")

        # PERSONALIZAR 3: Color de fondo (Verde menta pastel)
        self.ventana.configure(bg="#E8F8F5")

        self.ventana.resizable(False, False)
        self.ventana.transient(root)
        self.ventana.grab_set()

        # PERSONALIZAR 4: Título principal
        self.titulo = tk.Label(
            self.ventana,
            text="CREAR CUENTA",
            font=("Segoe UI", 18, "bold"),
            bg="#E8F8F5",
            fg="#117864"
        )
        self.titulo.pack(pady=15)

        # PERSONALIZAR 5: Etiquetas y Campos
        self.lbl_nombre = tk.Label(
            self.ventana,
            text="Nombre completo:",
            bg="#E8F8F5",
            fg="#2E4053",
            font=("Segoe UI", 10, "bold")
        )
        self.lbl_nombre.pack()

        self.entry_nombre = tk.Entry(
            self.ventana,
            width=38,
            font=("Segoe UI", 11),
            bg="#FFFFFF",
            fg="#1C2833",
            insertbackground="#1C2833"
        )
        self.entry_nombre.pack(pady=4)

        self.lbl_email = tk.Label(
            self.ventana,
            text="Correo electrónico:",
            bg="#E8F8F5",
            fg="#2E4053",
            font=("Segoe UI", 10, "bold")
        )
        self.lbl_email.pack()

        self.entry_email = tk.Entry(
            self.ventana,
            width=38,
            font=("Segoe UI", 11),
            bg="#FFFFFF",
            fg="#1C2833",
            insertbackground="#1C2833"
        )
        self.entry_email.pack(pady=4)

        self.lbl_password = tk.Label(
            self.ventana,
            text="Contraseña:",
            bg="#E8F8F5",
            fg="#2E4053",
            font=("Segoe UI", 10, "bold")
        )
        self.lbl_password.pack()

        self.entry_password = tk.Entry(
            self.ventana,
            width=38,
            show="*",
            font=("Segoe UI", 11),
            bg="#FFFFFF",
            fg="#1C2833",
            insertbackground="#1C2833"
        )
        self.entry_password.pack(pady=4)

        self.lbl_confirmar = tk.Label(
            self.ventana,
            text="Confirmar contraseña:",
            bg="#E8F8F5",
            fg="#2E4053",
            font=("Segoe UI", 10, "bold")
        )
        self.lbl_confirmar.pack()

        self.entry_confirmar = tk.Entry(
            self.ventana,
            width=38,
            show="*",
            font=("Segoe UI", 11),
            bg="#FFFFFF",
            fg="#1C2833",
            insertbackground="#1C2833"
        )
        self.entry_confirmar.pack(pady=4)

        # PERSONALIZAR 6: Botones con bordes y colores pastel contrastados
        self.btn_guardar = tk.Button(
            self.ventana,
            text="Registrar usuario",
            width=24,
            bg="#A3E4D7",
            fg="#0E6251",
            font=("Segoe UI", 11, "bold"),
            highlightbackground="#A3E4D7",
            cursor="hand2"
        )
        self.btn_guardar.pack(pady=15)

        self.btn_cancelar = tk.Button(
            self.ventana,
            text="Cancelar",
            width=24,
            bg="#FADBD8",
            fg="#78281F",
            font=("Segoe UI", 10),
            highlightbackground="#FADBD8",
            command=self.cerrar,
            cursor="hand2"
        )
        self.btn_cancelar.pack(pady=5)

        self.entry_nombre.focus_set()

    def obtener_datos(self):
        nombre = self.entry_nombre.get().strip()
        email = self.entry_email.get().strip()
        password = self.entry_password.get()
        confirmar = self.entry_confirmar.get()

        return nombre, email, password, confirmar

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(
                titulo,
                mensaje,
                parent=self.ventana
            )
        else:
            messagebox.showinfo(
                titulo,
                mensaje,
                parent=self.ventana
            )

    def cerrar(self):
        self.ventana.destroy()