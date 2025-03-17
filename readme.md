# Windows Reminder Tool

## Installation Instructions

### 1. Install Dependencies
Ensure you have Python installed on your system. If not, download and install it from [Python.org](https://www.python.org/downloads/).

Then, install the required dependencies using the following command:
```sh
pip install tk
```
(Note: `sqlite3` is included with Python by default.)

### 2. Running the Application
After installing dependencies, you can run the application with:
```sh
python windows_reminder_tool.py
```

### 3. Creating an Executable (Optional)
If you want to create an `.exe` file for Windows, install PyInstaller:
```sh
pip install pyinstaller
```
Then, create the executable:
```sh
pyinstaller --onefile --windowed windows_reminder_tool.py
```
The generated executable will be found in the `dist/` folder.

### 4. Using Conda (Optional)
If you are using a Conda-based Python installation, create a virtual environment:
```sh
conda create --name reminder_app python=3.9
conda activate reminder_app
```
Then, install dependencies:
```sh
conda install -c anaconda tk sqlite
pip install pyinstaller
```
Run the application or package it as an `.exe` as shown above.

### 5. Troubleshooting
- If Tkinter is missing, install it using:
  ```sh
  conda install -c anaconda tk
  ```
- If SQLite3 is missing, install it using:
  ```sh
  conda install -c anaconda sqlite
  ```
- If PyInstaller fails, ensure all dependencies are correctly installed and try running the `pyinstaller` command again.

### 6. Future Enhancements
- Add a system tray notification feature.
- Improve the UI with custom themes.
- Enable cloud sync for reminders.

---
This tool helps you keep track of important events efficiently. Enjoy using it!

