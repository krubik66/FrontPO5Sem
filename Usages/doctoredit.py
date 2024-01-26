from tkinter import *
from tkcalendar import Calendar
from datetime import datetime


class DoctorEdit:

    def __init__(self):
        self.root = Tk()
        self.root.title("Edycja wydarzenia")

        now = datetime.now()

        self.cal = Calendar(self.root, selectmode='day',
                               year=now.year, month=now.month,
                               day=now.day)

        self.cal.grid(column=0, row=0, columnspan=2, rowspan=2)

        Button(self.root, text="Pokaż wydarzenia",
               command=self.grad_date).grid(row=0, column=2)

        self.date = Label(self.root, text="")
        self.date.grid(column=2, row=1)

        self.event_list = Listbox(self.root, selectmode=SINGLE, height=5, width=20)
        self.event_list.bind('<<ListboxSelect>>', self.selected)

        self.write_button = Button(self.root, text="Wypisz zwolnienie", command=self.on_select)
        self.write_button.configure(state="disabled")
        self.write_button.grid(column=3, row=1)
        self.block_button = Button(self.root, text="Zablokuj wydarzenie", command=self.blocking_window)
        self.block_button.configure(state="disabled")
        self.block_button.grid(column=3, row=2)
        self.event_list.grid(column=3, row=0)

    def selected(self, event):
        self.write_button.configure(state="active")
        self.block_button.configure(state="active")

    def blocking_window(self):
        self.accept_window = Tk()
        self.accept_window.title("Potwierdzenie")

        self.accept_window.geometry("200x100")
        Button(self.accept_window, text="Potwierdź", command=self.accept).pack(side=LEFT, expand=YES)
        Button(self.accept_window, text="Anuluj", command=self.accept_window.destroy).pack(side=RIGHT, expand=YES)

    def grad_date(self):
        # wybor dnia -----------------------------------------------
        self.date.config(text="Wybrana data: " + self.cal.get_date())

        # tablica string [day, month, year]---------------------------------------------------------------
        result = self.cal.get_date().split("/")[0]

        # tu daj eventy ----------------------------------------------------------------------------------
        events = ["Event 1", "Event 2", "Event 3"]
        self.event_list.delete(0, END)
        self.write_button.configure(state="disabled")
        self.block_button.configure(state="disabled")
        for event in events:
            self.event_list.insert(END, event)

    def on_select(self):
        selected_index = self.event_list.curselection()
        if selected_index:
            selected_event = self.event_list.get(selected_index[0])
            print(f"Selected Event: {selected_event}")
            self.input_reason()

    def input_reason(self):
        reason_window = Tk()
        reason_window.title("Zwolnienie lekarskie")

        text_edit = Text(reason_window, height=20, width=100)
        text_edit.grid(column=0, row=0, columnspan=2)

        def accept():
            text_content = text_edit.get("1.0", "end-1c")
            print("Text content:", text_content) # tu dostajesz to co wpisałeś -------------------------------------
            reason_window.destroy()

        Button(reason_window, text="Zapisz", command=accept).grid(column=0, row=1)

        Button(reason_window, text="Cofnij", command=reason_window.destroy).grid(column=1, row=1)
        reason_window.mainloop()

    def accept(self):
        self.event_list.delete(self.event_list.curselection())
        self.accept_window.destroy()


if __name__ == "__main__":
    DoctorEdit().root.mainloop()