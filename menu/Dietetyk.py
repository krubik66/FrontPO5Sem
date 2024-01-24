from tkinter import Tk, Button
from Usages.dietetykcreate import DietykCreate


class Dietetyk:
    def __init__(self):
        self.root = Tk()
        self.root.title("Dietetyk")
        self.root.geometry("500x400")

        def launch():
            DietykCreate().root.mainloop()

        Button(self.root, text="Dodaj plan żywieniowy", command=launch, background="yellow").pack(pady=50)