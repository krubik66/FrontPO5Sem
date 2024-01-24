from tkinter import Tk, Button
from menu.Dietetyk import Dietetyk
from menu.Sportowiec import Sportowiec
from menu.Psycholog import Psycholog
from menu.Doktor import Doktor


class Menu:
    def __init__(self):
        self.root = Tk()
        self.root.title("Menu")
        self.root.geometry("500x400")

        def launch_dietetyk():
            Dietetyk().root.mainloop()

        Button(self.root, text="Dietetyk", command=launch_dietetyk, background="yellow").pack(pady=10)

        def launch_doktor():
            Doktor().root.mainloop()

        Button(self.root, text="Doktor", command=launch_doktor, background="yellow").pack(pady=10)

        def launch_psycholog():
            Psycholog().root.mainloop()

        Button(self.root, text="Psycholog", command=launch_psycholog, background="yellow").pack(pady=10)

        def launch_sportowiec():
            Sportowiec().root.mainloop()

        Button(self.root, text="Sportowiec", command=launch_sportowiec, background="yellow").pack(pady=10)