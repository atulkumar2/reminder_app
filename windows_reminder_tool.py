"""A simple Windows reminder tool using Python.
It will allow users to add, view, and receive notifications for different events.
The tool will have a graphical user interface (GUI) using Tkinter and
will use a local database (SQLite) to store reminders.
"""
import time
import tkinter as tk
from tkinter import messagebox
import sqlite3
import datetime
import threading

# Database setup
def init_db():
    """Initialize the SQLite database and create the reminders table."""
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reminders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Add reminder
def add_reminder():
    """Add a reminder to the database and update the listbox.
    The reminder consists of an event, date, and time.
    """
    event = event_entry.get()
    date = date_entry.get()
    dt = time_entry.get()

    if not event or not date or not dt:
        messagebox.showwarning("Input Error", "Please fill all fields!")
        return

    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reminders (event, date, time) VALUES (?, ?, ?)", (event, date, dt))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Reminder added!")
    event_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    show_reminders()

# Show reminders
def show_reminders():
    """Show all reminders in the listbox."""
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reminders")
    rows = cursor.fetchall()
    conn.close()
    reminder_list.delete(0, tk.END)
    for row in rows:
        reminder_list.insert(tk.END, f"{row[1]} - {row[2]} {row[3]}")

# Check reminders
def check_reminders():
    """Check for reminders that match the current date and time.
    If a match is found, show a notification.
    """
    while True:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        conn = sqlite3.connect("reminders.db")
        cursor = conn.cursor()
        cursor.execute("SELECT event FROM reminders WHERE date || ' ' || time = ?", (now,))
        rows = cursor.fetchall()
        conn.close()
        if rows:
            for row in rows:
                messagebox.showinfo("Reminder", f"It's time for: {row[0]}")

        time.sleep(60)

# GUI Setup
root = tk.Tk()
root.title("Event Reminder")
root.geometry("400x400")

init_db()

# Widgets
tk.Label(root, text="Event:").pack()
event_entry = tk.Entry(root)
event_entry.pack()

tk.Label(root, text="Date (YYYY-MM-DD):").pack()
date_entry = tk.Entry(root)
date_entry.pack()

tk.Label(root, text="Time (HH:MM, 24hr):").pack()
time_entry = tk.Entry(root)
time_entry.pack()

tk.Button(root, text="Add Reminder", command=add_reminder).pack()

reminder_list = tk.Listbox(root)
reminder_list.pack(fill=tk.BOTH, expand=True)

show_reminders()

# Run reminder checker in background
thread = threading.Thread(target=check_reminders, daemon=True)
thread.start()

root.mainloop()
