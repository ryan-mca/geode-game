from os import name, system

class GeodeGame:
    def __init__(self) -> int:
        """Sets up default values

        Returns:
            int: Exit Code
        """
        self.turnCounter: int = 1
        self.woodChoppers: int = 0
        self.clayMiners: int = 0
        self.oreMiners: int = 0
        self.geodeMiners: int = 0

        return 0

    def addWoodChopper(self) -> int:
        """Adds a single wood chopper

        Returns:
            int: Exit Code
        """
        self.woodChoppers += 1
        return 0

    def addClayMiner(self) -> int:
        """Adds a single clay miner

        Returns:
            int: Exit Code
        """
        self.clayMiners += 1

    def addOreMiner(self) -> int:
        """Adds a single ore miner

        Returns:
            int: Exit Code
        """
        self.oreMiners += 1

    def addGeodeMiner(self) -> int:
        """Adds a single geode miner

        Returns:
            int: Exit Code
        """
        self.geodeMiners += 1
        return 0

    def saveCurrentGame(self) -> int:
        return 1

    def loadGame(self) -> int:
        return 1

def clear() -> int:
    """Clears the terminal

    Returns:
        int: os.system return code
    """

    return system("cls" if name == "nt" else "clear")


def main_interface(turnCounter: int) -> int:
    print(f"Turn: {turnCounter}")

    return 0