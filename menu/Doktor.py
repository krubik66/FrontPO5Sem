from tkinter import Tk, Button
from Usages.doctorDelete import DoctorDelete
from Usages.doctoredit import DoctorEdit


class Doktor:
    def __init__(self):
        self.root = Tk()
        self.root.title("Doktor")
        self.root.geometry("500x400")

        def launch():
            DoctorEdit().root.mainloop()

        Button(self.root, text="Edytuj wydarzenie", command=launch, background="yellow").pack(pady=50)

        def launch2():
            DoctorDelete().root.mainloop()

        Button(self.root, text="Usuń wydarzenie", command=launch2, background="yellow").pack(pady=20)