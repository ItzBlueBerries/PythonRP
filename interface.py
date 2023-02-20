import json
import pickle
import time
import webbrowser
from tkinter import Menu, messagebox

from customtkinter import *

from presence import connect, disconnect, update, create_presence

version = "1.0"


def auto_save(app: CTk, appid: CTkEntry, state: CTkEntry, details: CTkEntry, large_image: CTkEntry, large_text: CTkEntry, small_image: CTkEntry, small_text: CTkEntry,
              button1_name: CTkEntry, button1_url: CTkEntry, button2_name: CTkEntry, button2_url: CTkEntry, start: CTkEntry, end: CTkEntry):
    try:
        presence_dict = {
            "application_id": appid.get(),
            "state": state.get(),
            "details": details.get(),
            "large_image": large_image.get(),
            "large_text": large_text.get(),
            "small_image": small_image.get(),
            "small_text": small_text.get(),
            "buttons": [
                {
                    "label": button1_name.get(),
                    "url": button1_url.get()
                },
                {
                    "label": button2_name.get(),
                    "url": button2_url.get()
                }
            ],
            "start": start.get(),
            "end": end.get()
        }
        with open("PythonRP/autosave.pkl", "wb") as f:
            if presence_dict:
                pickle.dump(presence_dict, f)
                print("Discord Presence Autosave file saved.")
    except FileExistsError:
        pass

    app.destroy()


def auto_load(appid: CTkEntry, state: CTkEntry, details: CTkEntry, large_image: CTkEntry, large_text: CTkEntry, small_image: CTkEntry, small_text: CTkEntry,
              button1_name: CTkEntry, button1_url: CTkEntry, button2_name: CTkEntry, button2_url: CTkEntry, start: CTkEntry, end: CTkEntry):
    try:
        with open("PythonRP/autosave.pkl", "rb") as f:
            autosave = pickle.load(f)
            appid.insert(0, autosave["application_id"])
            state.insert(0, autosave["state"])
            details.insert(0, autosave["details"])
            large_image.insert(0, autosave["large_image"])
            large_text.insert(0, autosave["large_text"])
            small_image.insert(0, autosave["small_image"])
            small_text.insert(0, autosave["small_text"])
            button1_name.insert(0, autosave["buttons"][0]["label"])
            button1_url.insert(0, autosave["buttons"][0]["url"])
            button2_name.insert(0, autosave["buttons"][1]["label"])
            button2_url.insert(0, autosave["buttons"][1]["url"])
            start.insert(0, autosave["start"])
            end.insert(0, autosave["end"])
            print("Discord Presence Autosave file loaded.")
    except FileNotFoundError:
        pass


def save_preset(presence_dict: dict):
    # Allow user to select a file to save the preset to
    file_path = filedialog.asksaveasfilename(filetypes=[("JSON files", "*.json")], defaultextension=".json", initialdir="./PythonRP")
    if not file_path:
        return  # User cancelled file dialog

    # Save the preset dictionary to the selected file path
    with open(file_path, 'w') as file:
        json.dump(presence_dict, file, indent=4)

    # Print a message indicating the file was saved
    print(f"Discord Presence Preset saved to {file_path}.")


def load_preset(appid: CTkEntry, state: CTkEntry, details: CTkEntry, large_image: CTkEntry, large_text: CTkEntry, small_image: CTkEntry, small_text: CTkEntry,
                button1_name: CTkEntry, button1_url: CTkEntry, button2_name: CTkEntry, button2_url: CTkEntry, start: CTkEntry, end: CTkEntry):
    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")], initialdir="./PythonRP")
    if file_path:
        # Load the preset file and update the GUI with the values
        with open(file_path, "r") as f:
            preset_data = json.load(f)
        appid.delete(0, END)
        appid.insert(0, preset_data["appid"])
        state.delete(0, END)
        state.insert(0, preset_data["state"])
        details.delete(0, END)
        details.insert(0, preset_data["details"])
        large_image.delete(0, END)
        large_image.insert(0, preset_data["large_image"])
        large_text.delete(0, END)
        large_text.insert(0, preset_data["large_text"])
        small_image.delete(0, END)
        small_image.insert(0, preset_data["small_image"])
        small_text.delete(0, END)
        small_text.insert(0, preset_data["small_text"])
        button1_name.delete(0, END)
        button1_name.insert(0, preset_data["buttons"][0]["label"])
        button1_url.delete(0, END)
        button1_url.insert(0, preset_data["buttons"][0]["url"])
        button2_name.delete(0, END)
        button2_name.insert(0, preset_data["buttons"][1]["label"])
        button2_url.delete(0, END)
        button2_url.insert(0, preset_data["buttons"][1]["url"])
        start.delete(0, END)
        start.insert(0, preset_data["start"])
        end.delete(0, END)
        end.insert(0, preset_data["end"])

        print(f"Discord Presence Preset loaded from {file_path}.")


def build_application(app: CTk):
    # Other Vars
    starting_time = time.time()

    # Other Funcs

    # Menus

    menu = Menu(app)
    app.config(menu=menu)

    file_menu = Menu(menu, tearoff=0)
    help_menu = Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=file_menu)
    menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="Github", command=lambda: webbrowser.open("https://github.com/ItzBlueBerries/PythonRP"))
    help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "PythonRP - Custom Rich Presences using Python & Pypresence."
                                                                                      "\nCreated by FruitsyOG."
                                                                                      "\nCredits to TomSchimansky for CustomTkinter. (Nicer ui)"
                                                                                      "\nCredits to qwertyquerty for Pypresence. (Operates this thing)"))
    file_menu.add_command(label="Save Preset / Presence", command=lambda: save_preset(
        {
            "appid": appid.get(),
            "state": state.get(),
            "details": details.get(),
            "large_image": large_image.get(),
            "large_text": large_text.get(),
            "small_image": small_image.get(),
            "small_text": small_text.get(),
            "buttons": [
                {
                    "label": button1_name.get(),
                    "url": button1_url.get()
                },
                {
                    "label": button2_name.get(),
                    "url": button2_url.get()
                }
            ],
            "start": start.get(),
            "end": end.get()
        }
    ))
    file_menu.add_command(label="Load Preset / Presence", command=lambda: load_preset(
        appid,
        state,
        details,
        large_image,
        large_text,
        small_image,
        small_text,
        button1_name,
        button1_url,
        button2_name,
        button2_url,
        start,
        end
    ))
    file_menu.add_command(label="Quit", command=lambda: app.destroy())

    # Title / Version
    title = CTkLabel(master=app, text=f"PythonRP v{version}")
    title.pack()

    # Frame
    main = CTkFrame(master=app)
    main.pack(fill="y")

    # Entries

    # - APPLICATION
    appid_text = CTkLabel(master=main, text="Application ID")
    appid_text.grid(row=0, column=0, padx=15, pady=5)
    appid = CTkEntry(master=main)
    appid.grid(row=0, column=1, padx=15, pady=5)

    # - DETAILS
    details_text = CTkLabel(master=main, text="Presence Details")
    details_text.grid(row=1, column=0, padx=15, pady=5)
    details = CTkEntry(master=main)
    details.grid(row=1, column=1, padx=15, pady=5)

    # - STATE
    state_text = CTkLabel(master=main, text="Presence State")
    state_text.grid(row=2, column=0, padx=15, pady=5)
    state = CTkEntry(master=main)
    state.grid(row=2, column=1, padx=15, pady=5)

    # - LARGE IMAGE (+ TEXT)
    large_image_text = CTkLabel(master=main, text="Presence Large Image")
    large_image_text.grid(row=3, column=0, padx=15, pady=5)
    large_image = CTkEntry(master=main)
    large_image.grid(row=3, column=1, padx=15, pady=5)

    large_text_text = CTkLabel(master=main, text="Presence Large Text")
    large_text_text.grid(row=4, column=0, padx=15, pady=5)
    large_text = CTkEntry(master=main)
    large_text.grid(row=4, column=1, padx=15, pady=5)

    # - SMALL IMAGE (+ TEXT)
    small_image_text = CTkLabel(master=main, text="Presence Small Image")
    small_image_text.grid(row=5, column=0, padx=15, pady=5)
    small_image = CTkEntry(master=main)
    small_image.grid(row=5, column=1, padx=15, pady=5)

    small_text_text = CTkLabel(master=main, text="Presence Small Text")
    small_text_text.grid(row=6, column=0, padx=15, pady=5)
    small_text = CTkEntry(master=main)
    small_text.grid(row=6, column=1, padx=15, pady=5)

    # - BUTTONS (1 & 2)
    button1_text = CTkLabel(master=main, text="Presence Button 1 (Name & URL)")
    button1_text.grid(row=7, column=0, padx=15, pady=5)
    button1_name = CTkEntry(master=main)
    button1_name.grid(row=7, column=1, padx=15, pady=5)
    button1_url = CTkEntry(master=main)
    button1_url.grid(row=7, column=2, padx=15, pady=5)

    button2_text = CTkLabel(master=main, text="Presence Button 2 (Name & URL)")
    button2_text.grid(row=8, column=0, padx=15, pady=5)
    button2_name = CTkEntry(master=main)
    button2_name.grid(row=8, column=1, padx=15, pady=5)
    button2_url = CTkEntry(master=main)
    button2_url.grid(row=8, column=2, padx=15, pady=5)

    # - START & END TIMESTAMP
    start_text = CTkLabel(master=main, text="Presence Start Timestamp")
    start_text.grid(row=9, column=0, padx=15, pady=5)
    start = CTkEntry(master=main)
    start.grid(row=9, column=1, padx=15, pady=5)

    end_text = CTkLabel(master=main, text="Presence End Timestamp")
    end_text.grid(row=10, column=0, padx=15, pady=5)
    end = CTkEntry(master=main)
    end.grid(row=10, column=1, padx=15, pady=5)

    # print(state.get())
    # print(details.get())
    # print(large_image.get())
    # print(large_text.get())

    # Other Buttons

    def started():
        start.delete(0, END)
        start.insert(0, int(starting_time))

    set_started = CTkButton(master=main, text="Set PythonRP Started", fg_color="black", hover_color="grey", command=started)
    set_started.grid(row=9, column=2)

    buttonFrame = CTkFrame(master=app)
    buttonFrame.pack()

    run = CTkButton(master=buttonFrame, text="Connect", fg_color="green", hover_color="grey", command=lambda: connect(
        appid.get(),
        create_presence(
            state=state.get(),
            details=details.get(),
            large_image=large_image.get(),
            large_text=large_text.get(),
            small_image=small_image.get(),
            small_text=small_text.get(),
            start=start.get(),
            end=end.get()
        ),
        button1_name,
        button1_url,
        button2_name,
        button2_url
    ))
    run.grid(row=1, column=1, padx=15, pady=15)

    stop = CTkButton(master=buttonFrame, text="Disconnect", fg_color="red", hover_color="grey", command=lambda: disconnect())
    stop.grid(row=1, column=0, padx=15, pady=15)

    change = CTkButton(master=buttonFrame, text="Update", fg_color="blue", hover_color="grey", command=lambda: update(create_presence(
        state=state.get(),
        details=details.get(),
        large_image=large_image.get(),
        large_text=large_text.get(),
        small_image=small_image.get(),
        small_text=small_text.get(),
        start=start.get(),
        end=end.get()
    ),
        button1_name,
        button1_url,
        button2_name,
        button2_url
    ))
    change.grid(row=1, column=2, padx=15, pady=15)

    auto_load(
        appid,
        state,
        details,
        large_image,
        large_text,
        small_image,
        small_text,
        button1_name,
        button1_url,
        button2_name,
        button2_url,
        start,
        end
    )

    app.protocol('WM_DELETE_WINDOW', lambda: auto_save(
        app,
        appid,
        state,
        details,
        large_image,
        large_text,
        small_image,
        small_text,
        button1_name,
        button1_url,
        button2_name,
        button2_url,
        start,
        end
    ))
