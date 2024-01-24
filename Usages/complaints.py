from tkinter import *
from tkcalendar import Calendar
from datetime import datetime


class Complaints:

    def __init__(self):
        self.root = Tk()
        self.root.title("Dodaj uwagę")
        self.root.geometry("500x400")

        now = datetime.now()

        self.cal = Calendar(self.root, selectmode='day',
                               year=now.year, month=now.month,
                               day=now.day)

        self.cal.grid(column=0, row=0, columnspan=2, rowspan=2)

        Button(self.root, text="Pokaż wydarzenia",
               command=self.grad_date).grid(row=0, column=2)

        self.date = Label(self.root, text="")
        self.date.grid(column=3, row=0)

        self.event_list = Listbox(self.root, selectmode=SINGLE, height=5, width=20)
        self.event_list.bind('<<ListboxSelect>>', self.selected)

        self.event_list.grid(column=2, row=1)

    def selected(self, event):
        selected_index = self.event_list.curselection()
        if selected_index:
            selected_event = self.event_list.get(selected_index[0])
            print(f"Selected Event: {selected_event}")
            self.input_reason()

    def grad_date(self):
        # wybor dnia -----------------------------------------------
        # self.date.config(text="Wybrana data: " + self.cal.get_date())

        # tablica string [day, month, year]---------------------------------------------------------------
        result = self.cal.get_date().split("/")[0]

        # tu daj eventy ----------------------------------------------------------------------------------
        events = ["Event 1", "Event 2", "Event 3"]
        self.event_list.delete(0, END)
        for event in events:
            self.event_list.insert(END, event)

    def input_reason(self):
        reason_window = Tk()
        reason_window.title("Uwaga")

        text_edit = Text(reason_window, height=20, width=100)
        text_edit.grid(column=0, row=0, columnspan=2)

        def accept():
            text_content = text_edit.get("1.0", "end-1c")
            print("Text content:", text_content) # tu dostajesz to co wpisałeś -------------------------------------
            reason_window.destroy()

        Button(reason_window, text="Zapisz", command=accept).grid(column=0, row=1)

        Button(reason_window, text="Cofnij", command=reason_window.destroy).grid(column=1, row=1)
        reason_window.mainloop()



if __name__ == "__main__":
    Complaints().root.mainloop()