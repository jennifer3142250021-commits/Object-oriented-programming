import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod
import os


class SmartDevice(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class SmartLight(SmartDevice):
    def __init__(self):
        super().__init__("Living room smartlight")

    def turn_on(self):
        return f"{self.name} set the brightness to 100"

    def turn_off(self):
        return f"{self.name} turned off"


class SmarSpeaker(SmartDevice):
    def __init__(self):
        super().__init__("Alexa speaker")

    def turn_on(self):
        return f"{self.name} playing lofi music at volume 8"

    def turn_off(self):
        return f"{self.name} turned off"


class SmartAC(SmartDevice):
    def __init__(self):
        super().__init__("Hisense inverter")

    def turn_on(self):
        return f"{self.name} compressor started, setting 20C"

    def turn_off(self):
        return f"{self.name} turned off"



class SmartTV(SmartDevice):
    def __init__(self):
        super().__init__("Samsung Smart TV")

    def turn_on(self):
        return f"{self.name} turned on"

    def turn_off(self):
        return f"{self.name} turned off"


# GUI with tkinter
class SmartHomeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Lab6. Smart Home Controller (polymorphism)")
        self.geometry("600x500")
        self.resizable(False, False)

        # Icon
        dir_actual = os.path.dirname(os.path.abspath(__file__))
        icon_dir = os.path.join(dir_actual, "app_icon.png")
        self.iconphoto(False, tk.PhotoImage(file=icon_dir))

        self.device = {
            "Light": SmartLight(),
            "Speaker": SmarSpeaker(),
            "AC": SmartAC(),
            "TV": SmartTV(),
        }

        self.built_ui()

    def built_ui(self):

        # Header
        title = ttk.Label(
            self,
            text="Smart Home Center",
            font=("Arial", 15, "bold")
        )
        title.pack(pady=15)

        # Label frame
        group_box = ttk.LabelFrame(
            self,
            text="Select device",
            padding=10
        )
        group_box.pack(fill="x", padx=20, pady=5)

        # Default selection
        first_key = list(self.device.keys())[0]
        self.selected_key = tk.StringVar(value=first_key)

        # Radiobuttons
        for key in self.device.keys():
            rb = ttk.Radiobutton(
                group_box,
                text=key,
                value=key,
                variable=self.selected_key
            )
            rb.pack(anchor="w", pady=2)

        # Buttons
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        btn_on = tk.Button(
            button_frame,
            text="TURN ON",
            command=self.turn_on_device,
            bg="#2980b9",
            fg="pink",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=6
        )
        btn_on.pack(side="left", padx=5)

        btn_off = tk.Button(
            button_frame,
            text="TURN OFF",
            command=self.turn_off_device,
            bg="#c0392b",
            fg="pink",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=6
        )
        btn_off.pack(side="left", padx=5)

        # Listbox with scrollbar
        list_frame = ttk.LabelFrame(
            self,
            text="Devices",
            padding=10
        )
        list_frame.pack(fill="both", padx=20, pady=5)

        self.listbox = tk.Listbox(
            list_frame,
            height=5,
            font=("Arial", 10)
        )
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(
            list_frame,
            orient="vertical",
            command=self.listbox.yview
        )
        scrollbar.pack(side="right", fill="y")

        self.listbox.config(yscrollcommand=scrollbar.set)

        # Add devices to Listbox
        for key in self.device.keys():
            self.listbox.insert(tk.END, key)

        # Output
        self.lbl_output = tk.Label(
            self,
            text="Select a device and click 'TURN ON' or 'TURN OFF'.",
            font=("Arial", 10, "italic"),
            bg="#ecf0f1",
            fg="#34495e",
            relief="groove",
            height=3,
            wraplength=500,
            justify="center"
        )
        self.lbl_output.pack(fill="x", padx=20, pady=10)

    def turn_on_device(self):

        chosen_key = self.selected_key.get()

        active_object = self.device[chosen_key]

        result_message = active_object.turn_on()

        self.lbl_output.config(
            text=result_message,
            font=("Arial", 10, "normal")
        )

    def turn_off_device(self):

        chosen_key = self.selected_key.get()

        active_object = self.device[chosen_key]

        result_message = active_object.turn_off()

        self.lbl_output.config(
            text=result_message,
            font=("Arial", 10, "normal")
        )


# LAUNCHER
if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()