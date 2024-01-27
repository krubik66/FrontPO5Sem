from tkinter import *
from tkcalendar import Calendar
from datetime import datetime


class FreeTime:

    def __init__(self):
        self.root = Tk()
        self.root.title("Dodanie przerwy")

        now = datetime.now()
        self.result_day = ""
        self.result_hour = ""

        self.cal = Calendar(self.root, selectmode='day',
                               year=now.year, month=now.month,
                               day=now.day)

        self.cal.grid(column=3, row=0, columnspan=2, rowspan=2)

        self.hour_list = Listbox(self.root, selectmode=SINGLE)
        self.hour_list.bind('<<ListboxSelect>>', self.selected)

        self.choose_hour_button = Button(self.root, text="Potwierdź godzinę", command=self.choosen_hour)
        self.choose_hour_button.configure(state="disabled")
        self.choose_hour_button.grid(column=0, row=3)
        self.cancel_button = Button(self.root, text="Anuluj wybieranie", command=self.cancel_hour)
        self.cancel_button.configure(state="disabled")
        self.cancel_button.grid(column=1, row=3)

        self.accept_day_button = Button(self.root, text="Potwierdź dzień", command=self.choosen_day)
        self.accept_day_button.grid(column=3, row=3)
        self.cancel_day_button = Button(self.root, text="Cofnij dzień", command=self.cancel_day)
        self.cancel_day_button.grid(column=4, row=3)
        self.hour_list.grid(column=0, row=0, rowspan=2, columnspan=2)

        events = [f"{i}.00 - {i + 2}.00" for i in range(6, 18, 2)]
        self.hour_list.delete(0, END)
        for event in events:
            self.hour_list.insert(END, event)

    def selected(self, event):
        self.choose_hour_button.configure(state="active")
        self.cancel_button.configure(state="active")

    def result_window(self):
        # tu możesz pobrać wyniki --------------------------------------------------------------------------------------------------------------
        # tu możesz pobrać wyniki --------------------------------------------------------------------------------------------------------------
        # tu możesz pobrać wyniki --------------------------------------------------------------------------------------------------------------

        # self.result_day  <--------------------- dzień miesiąc i rok w tabelce jak zawsze
        # self.result_hour <--------------------- przedział godzinowy w stringu

        self.accept_window = Tk()
        self.accept_window.title("Potwierdzenie")

        self.accept_window.geometry("200x100")
        Label(self.accept_window, text="Termin przerwy został wybrany").pack()
        Button(self.accept_window, text="Ok", command=self.accept_window.destroy).pack(expand=YES)

    def choosen_day(self):
        # tablica string [day, month, year]---------------------------------------------------------------
        self.result_day = self.cal.get_date().split("/")[0]
        self.accept_day_button.configure(state="disabled")
        if self.result_hour != "":
            self.result_window()

    def choosen_hour(self):
        selected_index = self.hour_list.curselection()
        if selected_index:
            selected_hour = self.hour_list.get(selected_index[0])
            print(f"Selected hour: {selected_hour}")
            self.result_hour = selected_hour
            self.choose_hour_button.configure(state="disabled")
            if self.result_day != "":
                self.result_window()

    def cancel_day(self):
        self.result_day = ""
        self.accept_day_button.configure(state="active")

    def cancel_hour(self):
        self.result_hour = ""
        self.choose_hour_button.configure(state="active")

if __name__ == "__main__":
    FreeTime().root.mainloop()