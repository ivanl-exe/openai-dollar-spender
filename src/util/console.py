from os import system, name

def flush() -> None:
    system('cls' if name == 'nt' else 'clear')