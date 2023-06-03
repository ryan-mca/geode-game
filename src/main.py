import cli

def main():
    cli.clear()

    while True:
        cli.main_interface()
        break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit("\nCTRL+N")