from os import name, system

def clear() -> int:
    """Clears the terminal

    Returns:
        int: os.system return code
    """

    return system("cls" if name == "nt" else "clear")


def main_interface() -> int:
    return