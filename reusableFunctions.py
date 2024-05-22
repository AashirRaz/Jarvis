from functools import partial
from Constants import OS, PathConstants
import os
import time
from art import tprint

def handlePress(path:str) -> None:
    if (OS.IOS):
        import subprocess
        localPath = '/'.join(path.split("/")[:-1])
        print(localPath)
        subprocess.run([f"open {localPath}"], check=True)
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
        time.sleep(5)
        client.stop_listening_for_callbacks()
    elif (OS.WINDOWS):
        from win11toast import toast
        toast(title, subtitle, icon=icon, duration=10, image=path, on_click=path)


def filter_by_full_name(skypeContacts:list[str], full_names: list[str]) -> list[object]:
    filtered_objects = []
    for contact in skypeContacts:
        for name in full_names:
            if contact.lower() == name.lower():
                filtered_objects.append(contact)

    return filtered_objects


def jarvis_init(directory_path):
    base_path = PathConstants.BasePath
    full_path = os.path.join(base_path, directory_path)
    os.chdir(full_path)
    return full_path

def jarvis_logo():
    print("\n")
    tprint("     JARVIS      ", font="tarty8") #broadway colossal
    print("\n")
    # print("""
    #                  .B@@@@@@!  ?###&&&@@@@   . ^5GB#&&&@@@@@@&B7 !@@@@@@7  J@@@@@&:JGGB#&G    :!YPB&&@@@&#G 
    #                  !@@@@@@P. ^&@@@@@@@@@@     J@@@@@@@@@@@@@@@@ !@@@@@@^ :&@@@@@7:@@@@@@? :?G&@@@@@@@@@@@@&
    #                  G@@@@@@~  P@@@@@J#@@@@     G@@@@@#JJJY5#@@@@ 7@@@@@#. ?@@@@@B.J@@@@@#.7#@@@@@@GJ7P@@@@@@
    #                 ^@@@@@@P  ?@@@@@P:&@@@@    ^@@@@@@J    :G@@@# J@@@@@P .#@@@@@~ B@@@@@Y?@@@@@@@J   :##G5J7
    #                 Y@@@@@@~ :&@@@@@^~@@@@@    J@@@@@&: .~5&@@@B^ 5@@@@@? 7@@@@@P !@@@@@&^B@@@@@@@@     
    #                .#@@@@@G  5@@@@@5 ?@@@@@   .#@@@@@B?P#@@@@@5:  G@@@@@~ G@@@@@^ P@@@@@P ?@@@@@@@@@@
    #                7@@@@@@! !@@@@@&^ 5@@@@@   7@@@@@@@@@@@@#Y^    #@@@@&:~@@@@@5 ^@@@@@@~   P&@@@@@@@@@B     
    #                G@@@@@B .#@@@@@J  B@@@@@   P@@@@@@@@@@@J       &@@@@B P@@@@&: Y@@@@@B     ^?G@@@@@@@@@
    #               ^&@@@@@? Y@@@@@&7~7&@@@@@  :&@@@@@?P@@@@#~      @@@@@5^@@@@@J :&@@@@@?        ~J#@@@@@@#   
    #               Y@@@@@# ~@@@@@@@@@@@@@@@@  J@@@@@#.~@@@@@#^     @@@@@7Y@@@@#. ?@@@@@#:  ^^      ^&@@@@@@
    #           JJ!J@@@@@@7 B@@@@@@BBB#@@@@@@  #@@@@@Y  P@@@@@#:    @@@@@P&@@@@? .B@@@@@Y  !&&57^   Y@@@@@@G    
    #          Y@@@@@@@@@P Y@@@@@@?   Y@@@@@@ !@@@@@@~  :&@@@@@B:   @@@@@@@@@@B. 7@@@@@@~ 7@@@@@@&&@@@@@@@#
    #         Y@@@@@@@@@P ~@@@@@@B    G@@@@@@ P@@@@@B   J@@@@@@5   t@@@@@@@@@? .B@@@@@G  #@@@@@@@@@@@@@&Y 
    #         JG&@@@@&B?  G&##BGG~   :#@&#BBP &&#BP5~    .GB5J!^:  @@@&&#BBG5. 7@@&&##7   7P#@@@@@@&B57   
    # """)
