import sys
import os
import keyboard
from board import Board


def clear_screen():
    """Clears the terminal screen based on the operating system."""
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For Linux/macOS
        _ = os.system('clear')

def to_move(logged_move):
    try:
        return int(float(logged_move))
    except:
        return logged_move[1:len(logged_move)-1]
    
def main():

    try:
        games = []
        for i in range(len(sys.argv)):
            filename = sys.argv[i]
            with open(filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if len(line) > 0 and line[0] == '[':
                        games.append([to_move(x) for x in line[1:len(line)-1].split(", ")])
        for i in range(len(games)):
            print(str(i + 1) + ". " + str(games[i]))
        choice = int(input("which game would you like to replay (choose by number)")) - 1
        game = games[choice]

        board = Board()
        idx = -1


        print("go through moves with arrow keys")
        board.printboard()
        while True:
            if keyboard.read_key() == "left":
                if idx > -1:
                    idx -= 1
                    board = Board()
                    for i in range(idx + 1):
                        if isinstance(game[i], int):
                            print(board.turn)
                            if board.wall(game[i]) == -1:
                                print(board.turn)
                                board.move_num(game[i])
                        else:
                            board.move(game[i])
                    clear_screen()
                    board.printboard()
                    print(game[i])
            elif keyboard.read_key() == "right":
                if idx < (len(game) - 1):
                    idx += 1
                    board = Board()
                    for i in range(idx + 1):
                        if isinstance(game[i], int):
                            if board.wall(game[i]) == -1:
                                board.move_num(game[i])
                        else:
                            board.move(game[i])
                    clear_screen()
                    board.printboard()
                    print(game[i])
            continue




    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()

