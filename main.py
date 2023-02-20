import webbrowser
import pystray

from PIL import Image
from pystray import MenuItem
from customtkinter import *

from interface import build_application, version

set_appearance_mode("dark")

app = CTk()
app.title(f"PythonRP v{version}")
app.wm_iconbitmap("icon.ico")
app.geometry("600x530")
app.resizable(False, False)

build_application(app)

if not os.path.exists("PythonRP"):
    os.makedirs("PythonRP")


def open_github():
    webbrowser.open("https://github.com/")


def quit_window(icon):
    icon.stop()
    app.destroy()


def show_window(icon):
    icon.stop()
    app.after(0, app.deiconify)


def withdraw_window():
    app.withdraw()
    image = Image.open("icon.ico")
    menu = (
        MenuItem('Quit', quit_window),
        MenuItem('Show', show_window),
        MenuItem('Github', open_github)
    )
    icon = pystray.Icon("Icon", image, "PythonRP", menu)
    icon.run()


app.protocol("WM_DELETE_WINDOW", withdraw_window)

app.mainloop()
