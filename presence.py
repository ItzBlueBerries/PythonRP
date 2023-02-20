import time
import pypresence
from customtkinter import CTkEntry

is_connected = False
presence = None


def create_presence(state=None, details=None, large_image=None, large_text=None, small_image=None, small_text=None, buttons=None, start=None, end=None):
    presence_dict = {}

    if state:
        presence_dict.update({"state": state})

    if details:
        presence_dict.update({"details": details})

    if large_image:
        presence_dict.update({"large_image": large_image})

    if large_text:
        presence_dict.update({"large_text": large_text})

    if small_image:
        presence_dict.update({"small_image": small_image})

    if small_text:
        presence_dict.update({"small_text": small_text})

    if buttons:
        presence_dict.update({"buttons": buttons})

    if start:
        presence_dict.update({"start": start})

    if end:
        presence_dict.update({"end": end})

    return presence_dict


def connect(client: int, presence_dict: dict, button1_name: CTkEntry, button1_url: CTkEntry, button2_name: CTkEntry, button2_url: CTkEntry):
    global is_connected
    global presence

    try:
        if not is_connected:
            presence = pypresence.Presence(client)
            presence.connect()

            buttons = []
            if button1_name.get() and button1_url.get():
                buttons.append({
                    "label": button1_name.get(),
                    "url": button1_url.get()
                })

            if button2_name.get() and button2_url.get():
                buttons.append({
                    "label": button2_name.get(),
                    "url": button2_url.get()
                })

            if len(buttons) == 0:
                buttons = None

            new_presence_dict = create_presence(
                state=presence_dict.get("state"),
                details=presence_dict.get("details"),
                large_image=presence_dict.get("large_image"),
                large_text=presence_dict.get("large_text"),
                small_image=presence_dict.get("small_image"),
                small_text=presence_dict.get("small_text"),
                buttons=buttons,
                start=presence_dict.get("start"),
                end=presence_dict.get("end")
            )

            presence.update(**new_presence_dict)
            print("Discord Presence Activated.")
            is_connected = True
        else:
            print("Discord Presence has already been activated. Cannot activate twice.")
    except Exception as e:
        print(f"Something went wrong: {e}")


def disconnect():
    global is_connected
    if presence is not None:
        if is_connected:
            presence.close()
            print("Discord Presence De-activated.")
        else:
            print("Discord Presence has not been activated. Cannot de-activate.")
    is_connected = False


def update(presence_dict: dict, button1_name: CTkEntry, button1_url: CTkEntry, button2_name: CTkEntry, button2_url: CTkEntry):
    try:
        if presence is not None:
            if is_connected:

                buttons = []
                if button1_name.get() and button1_url.get():
                    buttons.append({
                        "label": button1_name.get(),
                        "url": button1_url.get()
                    })

                if button2_name.get() and button2_url.get():
                    buttons.append({
                        "label": button2_name.get(),
                        "url": button2_url.get()
                    })

                if len(buttons) == 0:
                    buttons = None

                new_presence_dict = create_presence(
                    state=presence_dict.get("state"),
                    details=presence_dict.get("details"),
                    large_image=presence_dict.get("large_image"),
                    large_text=presence_dict.get("large_text"),
                    small_image=presence_dict.get("small_image"),
                    small_text=presence_dict.get("small_text"),
                    buttons=buttons,
                    start=presence_dict.get("start"),
                    end=presence_dict.get("end")
                )

                presence.update(**new_presence_dict)
                print("Discord Presence Updated.")
            else:
                print("Discord Presence has not been activated. Cannot update.")
    except Exception as e:
        print(f"Something went wrong: {e}")
