from tkinter import Tk, Button, Toplevel
from Usages.doctorDelete import DoctorDelete
from Usages.doctoredit import DoctorEdit


class Doktor:
    def __init__(self, root):
        self.root = root
        self.root.title("Doktor")
        self.root.geometry("500x400")

        def launch():
            DoctorEdit().root.mainloop()

        Button(self.root, text="Edytuj wydarzenie", command=launch, background="yellow").pack(pady=50)

        def launch2():
            sub = Toplevel(self.root)
            DoctorDelete(sub)

        Button(self.root, text="Usuń wydarzenie", command=launch2, background="yellow").pack(pady=20)