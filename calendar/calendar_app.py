import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta


class CalendarEvent:
    def __init__(self, title, date, start_time, duration_hours, duration_minutes):
        self.title = title
        self.date = datetime.strptime(date, '%Y-%m-%d').date()
        self.start_time = datetime.strptime(start_time, '%H:%M').time()
        start_datetime = datetime.combine(self.date, self.start_time)
        duration = timedelta(hours=duration_hours, minutes=duration_minutes)
        self.end_time = (start_datetime + duration).time()

    def conflicts_with(self, other_event):
        if self.date == other_event.date:
            return (
                self.start_time < other_event.end_time
                and self.end_time > other_event.start_time
            )
        return False

    def __str__(self):
        return f"{self.title} on {self.date} from {self.start_time} to {self.end_time}"


class Calendar:
    def __init__(self):
        self.events = []

    def add_event(self, title, date, start_time, duration_hours, duration_minutes):
        new_event = CalendarEvent(title, date, start_time, duration_hours, duration_minutes)
        for event in self.events:
            if new_event.conflicts_with(event):
                return f"Conflict with event '{event.title}'."
        self.events.append(new_event)
        return "Event added successfully."

    def remove_event(self, title):
        for event in self.events:
            if event.title == title:
                self.events.remove(event)
                return "Event removed successfully."
        return "Event not found."

    def edit_event(self, old_title, new_title, date, start_time, duration_hours, duration_minutes):
        for event in self.events:
            if event.title == old_title:
                self.events.remove(event)
                return self.add_event(new_title, date, start_time, duration_hours, duration_minutes)
        return "Event not found."

    def list_events(self):
        if not self.events:
            return "No events in the calendar."
        return "\n".join(str(event) for event in self.events)


class CalendarApp:
    def __init__(self, root):
        self.calendar = Calendar()
        self.root = root
        self.root.title("Calendar App")

        # Labels
        tk.Label(root, text="Event Title:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(root, text="Start Time (HH:MM):").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(root, text="Duration (Hours):").grid(row=3, column=0, padx=10, pady=5)
        tk.Label(root, text="Duration (Minutes):").grid(row=4, column=0, padx=10, pady=5)

        # Entry fields
        self.title_entry = tk.Entry(root)
        self.date_entry = tk.Entry(root)
        self.start_time_entry = tk.Entry(root)
        self.duration_hours_entry = tk.Entry(root)
        self.duration_minutes_entry = tk.Entry(root)

        self.title_entry.grid(row=0, column=1, padx=10, pady=5)
        self.date_entry.grid(row=1, column=1, padx=10, pady=5)
        self.start_time_entry.grid(row=2, column=1, padx=10, pady=5)
        self.duration_hours_entry.grid(row=3, column=1, padx=10, pady=5)
        self.duration_minutes_entry.grid(row=4, column=1, padx=10, pady=5)

        # Buttons
        tk.Button(root, text="Add Event", command=self.add_event).grid(row=5, column=0, pady=10)
        tk.Button(root, text="Edit Event", command=self.edit_event).grid(row=5, column=1, pady=10)
        tk.Button(root, text="Delete Event", command=self.delete_event).grid(row=6, column=0, pady=10)
        tk.Button(root, text="Show Events", command=self.show_events).grid(row=6, column=1, pady=10)

    def add_event(self):
        title = self.title_entry.get()
        date = self.date_entry.get()
        start_time = self.start_time_entry.get()
        try:
            duration_hours = int(self.duration_hours_entry.get())
            duration_minutes = int(self.duration_minutes_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Duration must be a number.")
            return

        if not title or not date or not start_time:
            messagebox.showerror("Invalid Input", "All fields are required.")
            return

        try:
            result = self.calendar.add_event(title, date, start_time, duration_hours, duration_minutes)
            if "Conflict" in result:
                messagebox.showwarning("Conflict Detected", result)
            else:
                messagebox.showinfo("Success", result)
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def edit_event(self):
        old_title = self.title_entry.get()
        new_title = self.title_entry.get()
        date = self.date_entry.get()
        start_time = self.start_time_entry.get()
        try:
            duration_hours = int(self.duration_hours_entry.get())
            duration_minutes = int(self.duration_minutes_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Duration must be a number.")
            return

        if not old_title or not new_title or not date or not start_time:
            messagebox.showerror("Invalid Input", "All fields are required.")
            return

        try:
            result = self.calendar.edit_event(old_title, new_title, date, start_time, duration_hours, duration_minutes)
            if "Conflict" in result:
                messagebox.showwarning("Conflict Detected", result)
            else:
                messagebox.showinfo("Success", result)
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def delete_event(self):
        title = self.title_entry.get()
        if not title:
            messagebox.showerror("Invalid Input", "Event title is required to delete.")
            return
        result = self.calendar.remove_event(title)
        if "not found" in result:
            messagebox.showwarning("Error", result)
        else:
            messagebox.showinfo("Success", result)

    def show_events(self):
        events = self.calendar.list_events()
        messagebox.showinfo("Events", events)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
