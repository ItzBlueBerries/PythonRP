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

app.mainloop()
