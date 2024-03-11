from functools import partial
from Constants import OS, PathConstants
import os
import time

def handlePress(path:str) -> None:
    if (OS.IOS):
        import subprocess
        localPath = '/'.join(path.split("/")[:-1])
        subprocess.run([f"open {localPath}"], shell=True, check=True)
    elif (OS.WINDOWS):
        import os
        os.startfile(path)


def notification(title: str, subtitle: str, icon: str, path: str) -> None:
    if (OS.IOS):
        from mac_notifications import client
        client.create_notification(
            title=title,
            subtitle=subtitle,
            icon=icon,
            action_button_str="open",
            action_callback=partial(handlePress, path=path)
        )
        time.sleep(1)
        client.stop_listening_for_callbacks()
    elif (OS.WINDOWS):
        from win11toast import toast
        toast(title, subtitle, icon=icon, duration=10, image=path, on_click=path)


def filter_by_full_name(skypeContacts:list[object], full_names: list[str]) -> list[object]:
    filtered_objects = []
    for contact in skypeContacts:
        for name in full_names:
            if contact["name"].lower() == name.lower():
                filtered_objects.append(contact)

    return filtered_objects


def jarvis_init(directory_path):
    base_path = PathConstants.BasePath
    full_path = os.path.join(base_path, directory_path)
    os.chdir(full_path)
    return full_path