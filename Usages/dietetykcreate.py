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

        self.kalorieSkladniki = 0

        def selectedSkladniki(event):
            selected_index = skladniki.curselection()
            selected_items = [skladnikiLista[index] for index in selected_index] # wybrane składniki ----------------------
            print(selected_items)
            self.kalorieSkladniki = 0
            for skladnik in selected_items:
                self.kalorieSkladniki += skladnik[1]
            kalorieLabel.configure(text=f"Kalorie: {self.kalorieSkladniki + self.kaloriePosilki}")
            pass

        skladniki = Listbox(self.root, selectmode=MULTIPLE, height=5, width=20)
        skladniki.bind('<<ListboxSelect>>', selectedSkladniki)

        skladnikiLista = [("Mąka", 1), ("Mleko", 5), ("Ser", 10)]# składniki ------------------------------------------------------
        skladniki.delete(0, END)
        for skladnik in skladnikiLista:
            skladniki.insert(END, skladnik[0])
        label1.pack(pady=5)
        skladniki.pack()

        self.kaloriePosilki = 0

        kalorieLabel = Label(self.root, text=f"Kalorie: {self.kalorieSkladniki + self.kaloriePosilki}")
        kalorieLabel.pack(pady=3)

        def selectedPosilki(event):
            selected_index = posilki.curselection()
            selected_items = [posilkiLista[index] for index in selected_index] # wybrane posiłki ----------------------
            print(selected_items)
            self.kaloriePosilki = 0
            for posilek in selected_items:
                self.kaloriePosilki += posilek[1]
            kalorieLabel.configure(text=f"Kalorie: {self.kalorieSkladniki + self.kaloriePosilki}")
            pass

        posilki = Listbox(self.root, selectmode=MULTIPLE, height=5, width=20)
        posilki.bind('<<ListboxSelect>>', selectedPosilki)

        posilkiLista = [("Zupa grzybowa", 500), ("Schabowy z ziemniakami", 1000), ("Frytki", 50)]# posiłki -------------------------------
        posilki.delete(0, END)
        for posilek in posilkiLista:
            posilki.insert(END, posilek[0])
        label2.pack(pady=5)
        posilki.pack()

        Button(self.root, text="Zapisz", command=self.root.destroy).pack(pady=20)


if __name__ == "__main__":
    DietykCreate().root.mainloop()
