from tkinter import Tk, Button
from Usages.complaints import Complaints


class Sportowiec:
    def __init__(self):
        self.root = Tk()
        self.root.title("Sportowiec")
        self.root.geometry("500x400")

        def launch():
            Complaints().root.mainloop()

        Button(self.root, text="Dodaj plan żywieniowy", command=launch, background="yellow").pack(pady=50)