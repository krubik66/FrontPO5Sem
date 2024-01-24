from tkinter import *
from tkinter import filedialog as fd


class MakingReports:

    def __init__(self):
        self.root = Tk()
        self.root.title("Tworzenie raportu")
        self.root.geometry("200x200")

        self.date = Label(self.root, text="")
        self.date.grid(column=3, row=0)

        self.event_list = Listbox(self.root, selectmode=SINGLE, height=5, width=20)

        self.event_list.bind('<<ListboxSelect>>', self.selected)

        self.make_report_button = Button(self.root, text="Napisz raport", command=self.on_select)
        self.make_report_button.configure(state="disabled")

        self.event_list.grid(column=0, row=0)
        self.make_report_button.grid(column=0, row=1)

        events = ["Event 1", "Event 2", "Event 3"]

        for event in events:
            self.event_list.insert(END, event)

    def selected(self, event):
        self.make_report_button.configure(state="active")

    def on_select(self):
        selected_index = self.event_list.curselection()
        if selected_index:
            selected_event = self.event_list.get(selected_index[0])
            print(f"Selected Event: {selected_event}") # wybór wydarzenia --------------------------------------------
            self.choose_option()
            self.root.destroy()

    def choose_option(self):
        options_window = Tk()
        options_window.title("Przekaż raport")
        options_window.geometry("200x200")

        def browse_file():
            file_path = fd.askopenfilename(title="Wybierz plik:",
                                                   filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if file_path:
                print(file_path) # tu będzie scieżka do pliku
                self.root.mainloop()
                options_window.destroy()

        Button(options_window, text="Przekaż plik", command=browse_file).pack()
        Button(options_window, text="Napisz raport", command=self.input_report).pack()

    def input_report(self):
        report_window = Tk()
        report_window.title("Raport")

        text_edit = Text(report_window, height=20, width=100)
        text_edit.grid(column=0, row=0, columnspan=2)

        def accept():
            text_content = text_edit.get("1.0", "end-1c")
            print("Text content:", text_content) # tu dostajesz to co wpisałeś -------------------------------------
            report_window.destroy()
            self.root.mainloop()

        Button(report_window, text="Zapisz", command=accept).grid(column=0, row=1)

        Button(report_window, text="Cofnij", command=report_window.destroy).grid(column=1, row=1)
        report_window.mainloop()

    def accept(self):
        self.event_list.delete(self.event_list.curselection())



if __name__ == "__main__":
    MakingReports().root.mainloop()