from tkinter import Tk, Button
from Usages.complaints import Complaints
from Usages.freetime import FreeTime


class Sportowiec:
    def __init__(self):
        self.root = Tk()
        self.root.title("Sportowiec")
        self.root.geometry("500x400")

        def launch():
            Complaints().root.mainloop()

        Button(self.root, text="Dodaj uwagę", command=launch, background="yellow").pack(pady=50)

        def launch2():
            FreeTime().root.mainloop()

        Button(self.root, text="Dodaj przerwę", command=launch2, background="yellow").pack(pady=20)