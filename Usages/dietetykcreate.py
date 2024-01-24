from tkinter import Tk, Button, Label, Listbox, MULTIPLE, END
from datetime import datetime
from tkcalendar import Calendar


class DietykCreate:
    def __init__(self):
        self.root = Tk()
        self.root.title("Dodawanie planu żywieniowego")
        self.root.geometry("500x400")
        self.root.configure(background="green")

        now = datetime.now()

        self.calendar = Calendar(self.root, selectmode='day',
                                 year=now.year, month=now.month,
                                 day=now.day)
        self.calendar.pack(pady=20)

        self.button = Button(self.root, text="Wybierz",
               command=self.create_meal)
        self.button.pack()

    def create_meal(self):
        # tablica string [day, month, year]---------------------------------------------------------------
        result = self.calendar.get_date().split("/")[0]

        self.calendar.pack_forget()
        self.button.pack_forget()

        label1 = Label(self.root, text="Składniki")
        label2 = Label(self.root, text="Posiłki")

        def selectedSkladniki(event):
            selected_index = skladniki.curselection()
            selected_items = [skladniki.get(index) for index in selected_index] # wybrane składniki ----------------------
            print(selected_items)
            pass

        skladniki = Listbox(self.root, selectmode=MULTIPLE, height=5, width=20)
        skladniki.bind('<<ListboxSelect>>', selectedSkladniki)

        skladnikiLista = ["Mąka", "Mleko", "Ser"]# składniki ------------------------------------------------------
        skladniki.delete(0, END)
        for skladnik in skladnikiLista:
            skladniki.insert(END, skladnik)
        label1.pack(pady=5)
        skladniki.pack()

        def selectedPosilki(event):
            selected_index = posilki.curselection()
            selected_items = [posilki.get(index) for index in selected_index] # wybrane posiłki ----------------------
            print(selected_items)
            pass

        posilki = Listbox(self.root, selectmode=MULTIPLE, height=5, width=20)
        posilki.bind('<<ListboxSelect>>', selectedPosilki)

        posilkiLista = ["Zupa grzybowa", "Schabowy z ziemniakami", "Frytki"]# posiłki -------------------------------
        posilki.delete(0, END)
        for posilek in posilkiLista:
            posilki.insert(END, posilek)
        label2.pack(pady=5)
        posilki.pack()

        Button(self.root, text="Zapisz", command=self.root.destroy).pack(pady=20)


if __name__ == "__main__":
    DietykCreate().root.mainloop()
