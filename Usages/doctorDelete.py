from tkinter import Tk, StringVar, Entry, Label, Radiobutton, Button, END, ttk, Text, Listbox, SINGLE


class DoctorDelete:
    def __init__(self):
        self.root = Tk()
        self.root.title("Usuwanie wydarzenia")
        self.root.geometry("500x400")
        self.root.configure(background="green")

        self.sportowiec_name_text = StringVar(value="Sportowiec")
        self.sportowiec_name_field = Entry(self.root, textvariable=self.sportowiec_name_text, width=20, )
        self.sportowiec_name_field.pack(pady=80)

        self.selected_option = StringVar(value="Zdrowy")

        # Create Radiobuttons
        self.radio1 = Radiobutton(self.root, text="Zdrowy", variable=self.selected_option, value="Zdrowy")
        self.radio1.pack()
        self.radio2 = Radiobutton(self.root, text="Wymagane dalsze badanie", variable=self.selected_option, value="Wymagane dalsze badanie")
        self.radio2.pack()
        self.save_button = Button(self.root, text="Zapisz", command=self.on_save)
        self.save_button.pack(pady=20)

    def on_save(self):
        def forget_old():
            self.save_button.pack_forget()
            self.radio1.forget()
            self.radio2.forget()
            self.sportowiec_name_field.forget()

        if self.selected_option.get() == "Zdrowy":
            forget_old()
        else:
            forget_old()
            self.more_tests_nedded()

    def more_tests_nedded(self):
        self.badanie_label = Label(self.root, text="Badanie specjalistyczne")
        self.badanie_label.pack(pady=10)

        columns = ('procedure')

        self.tree = ttk.Treeview(self.root, columns=columns, show='headings')

        # define headings
        self.tree.heading('procedure', text='Procedury')

        # generate sample data
        procedures = [("Badania dopingowe",), ("Badania ortopedyczne",)]

        # add data to the treeview
        for procedure in procedures:
            self.tree.insert('', END, values=procedure)

        def item_selected(event):
            for selected_item in self.tree.selection():
                item = self.tree.item(selected_item)
                record = item['values']
                print(record[0]) # typ przeprowadzonego badania --------------------------------------------------------

        self.tree.bind('<<TreeviewSelect>>', item_selected)
        self.tree.pack()

        def go_forth():
            self.badanie_label.pack_forget()
            self.tree.pack_forget()
            self.precedure_save_button.pack_forget()
            self.prescription_window()

        self.precedure_save_button = Button(self.root, text="Przeprowadź", command=go_forth)
        self.precedure_save_button.pack(pady=10)

    def prescription_window(self):
        self.sportowiec_name_field = Label(self.root, text="Sportowiec")
        self.sportowiec_name_field.pack(pady=30)
        text_edit = Text(self.root, height=10, width=60)
        text_edit.pack()

        def move_on():
            text_content = text_edit.get("1.0", "end-1c") # text z zwolnienia -----------------------------------
            self.sportowiec_name_field.pack_forget()
            text_edit.pack_forget()
            button.pack_forget()
            self.last_one()


        button = Button(self.root, text="Wypisz zwolnienie", command=move_on)
        button.pack(pady=10)

    def last_one(self):
        label = Label(self.root, text="Zaplanowane wydarzenia:")
        label.pack(pady=5)

        def selected(event):
            selected_index = event_list.curselection()
            pass

        event_list = Listbox(self.root, selectmode=SINGLE, height=5, width=20)
        event_list.bind('<<ListboxSelect>>', selected)

        events = ["Event 1", "Event 2", "Event 3"] # tu daj eventy -----------------------------------------------------
        event_list.delete(0, END)
        for event in events:
            event_list.insert(END, event)
        event_list.pack()

        def on_click():
            selected_index = event_list.curselection()
            if selected_index:
                selected_event = event_list.get(selected_index[0])  # to event do usuniecia ------------------------
                print(f"Selected Event: {selected_event}")
                event_list.delete(event_list.curselection())

        button = Button(self.root, text="Usuń", command=on_click)
        button.pack()



if __name__ == "__main__":
    DoctorDelete().root.mainloop()
