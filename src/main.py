import cli

def main() -> int:
    cli.clear()

    turnCounter: int = 0

    while True:
        turnCounter += 1
        cli.main_interface(turnCounter)
        break

    return 0

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit("\nCTRL+N")