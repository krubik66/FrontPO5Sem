import calendar
import tkinter as tk
from tkinter import messagebox
import datetime


class CalendarApp:
    def __init__(self, root):
        self.frame = None
        self.root = root
        self.root.title("Calendar App")

        currentTime = datetime.datetime.now()

        self.cal = calendar.TextCalendar(calendar.SUNDAY)
        self.year = tk.StringVar(value=f"{currentTime.year}")
        self.month = tk.StringVar(value=f"{currentTime.month}")

        self.create_widgets()
        self.show_calendar()

    def create_widgets(self):
        # Frame to hold calendar and event list
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        # Year entry
        year_label = tk.Label(frame, text="Year:")
        year_label.grid(row=0, column=0)
        year_entry = tk.Entry(frame, textvariable=self.year, width=5)
        year_entry.grid(row=0, column=1)

        # Month entry
        month_label = tk.Label(frame, text="Month:")
        month_label.grid(row=0, column=2)
        month_entry = tk.Entry(frame, textvariable=self.month, width=5)
        month_entry.grid(row=0, column=3)

        # Calendar widget
        self.cal_widget = tk.Text(frame, height=10, width=20)
        self.cal_widget.grid(row=1, column=0, columnspan=4)

        # Event list
        event_list_label = tk.Label(frame, text="Events:")
        event_list_label.grid(row=2, column=0, columnspan=4, pady=(10, 0))

        self.event_list = tk.Listbox(frame, selectmode=tk.SINGLE, height=5, width=20)
        self.event_list.grid(row=3, column=0, columnspan=4)

        # Button to display calendar and events
        show_button = tk.Button(frame, text="Show Calendar", command=self.show_calendar)
        show_button.grid(row=4, column=0, columnspan=4, pady=(10, 0))

    def show_calendar(self):
        try:
            year = int(self.year.get())
            month = int(self.month.get())

            # Get the calendar for the specified year and month
            cal_data = self.cal.formatmonth(year, month)

            # Display the calendar in the Text widget
            self.cal_widget.delete("1.0", tk.END)
            self.cal_widget.insert(tk.END, cal_data)

            # Display events in the Listbox (dummy data for demonstration)
            events = ["Event 1", "Event 2", "Event 3"]
            self.event_list.delete(0, tk.END)
            for event in events:
                self.event_list.insert(tk.END, event)

        except ValueError:
            messagebox.showerror("Error", "Invalid year or month. Please enter valid values.")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
