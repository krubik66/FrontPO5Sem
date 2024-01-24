from tkinter import Tk, Button
from Usages.makingreports import MakingReports


class Psycholog:
    def __init__(self):
        self.root = Tk()
        self.root.title("Psycholog")
        self.root.geometry("500x400")

        def launch():
            MakingReports().root.mainloop()

        Button(self.root, text="Edytuj wydarzenie", command=launch, background="yellow").pack(pady=50)
