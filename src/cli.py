from os import name, system

def clear():
    """Clears the terminal
    """

    system("cls" if name == "nt" else "clear")