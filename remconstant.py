"""Reminders Constants
"""
# remconstant.py

# Database file name
DB_NAME = "reminders.db"

# Date and Time formats
DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M"
DATETIME_FORMAT = f"{DATE_FORMAT} {TIME_FORMAT}"

# UI Constants
WINDOW_TITLE = "Event Reminder"
WINDOW_SIZE = "400x400"

# Messages
ERROR_MSG_INPUT = "Please fill all fields!"
SUCCESS_MSG_ADDED = "Reminder added successfully!"
REMINDER_MSG = "It's time for: {event}"

# Threading Interval (in seconds)
CHECK_INTERVAL = 60
