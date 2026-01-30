from Board import Board
import os

def __main__():
    try:
        b = Board(1, 12, 5)
        print(b)
    except ValueError as e:
        print("Error! Board parameters provided are not valid:", e)
        exit(1)
    
    while True:
        command = input("Enter command (or 'help' for commands): ").strip().lower()
        if command == "help":
            commands()
            continue
        elif command == "quit":
            clear_screen()
            print("Thanks for playing. Goodbye!")
            break
        elif command == "reveal":
            # debug command to reveal the board
            clear_screen()
            b.uncover()
            print(b)
            continue
        command = command.split()
        if command[0] == "flag":
            try:
                x = x_to_list(int(command[1]))
                y = y_to_list(int(command[2]), b.width)
                b.flag(x, y)
            except ValueError as e:
                clear_screen()
                print(b)
                print("Error:", e)
                continue
        elif command[0] == "dig":
            try:
                x = x_to_list(int(command[1]))
                y = y_to_list(int(command[2]), b.width)
                if not b.dig(x, y):
                    clear_screen()
                    print(b)
                    print("Game Over! You hit a mine.")
                    break
            except ValueError as e:
                clear_screen()
                print(b)
                print("Error:", e)
                continue
        else:
            clear_screen()
            print(b)
            print("Invalid command. Type 'help' for a list of commands.")
            continue
        
        if b.win():
            clear_screen()
            print(b)
            print("Congratulations! You've won the game!")
            break
        clear_screen()
        print(b)  

def x_to_list(x: int) -> int:
    return x - 1
    
def y_to_list(y: int, max: int) -> int:
    return max - y  

def clear_screen():
    """Clear the terminal screen in a cross-platform way."""
    # Use the native command where available, fallback to ANSI if needed
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def commands():
    clear_screen()
    print("==============")
    print("|| Commands ||")
    print("==============")
    print()
    print("dig x y      dig at space (x, y)")
    print("flag x y     toggle flag at space (x, y)")
    print("quit         quit the game")
    print()
    print("Press any key to continue: ", end="")
    input()

if __name__ == "__main__":
    __main__()