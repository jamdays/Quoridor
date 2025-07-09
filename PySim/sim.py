from mcts import Node
from board import Board
import time

num_runs = int(input("how many simulations? (please enter an integer)"))
logging = input("logging enabled? (y/n)") != "n"
log = None
if (logging):
    log = input("file to log to?")
    try: 
        log = open(log, 'w')
    except:
        print("could not open file")
        exit()
one_rp = .7
two_rp = .7
one_expansion = False
two_expansion = False
one_move_time = 2
two_move_time = 2
if (input("advanced options? (y/n)") != "n"):
    one_rp = float(input("level of bias towards moving for player one? (.5 = 50%)"))
    two_rp = float(input("level of bias towards moving for player two?"))
    one_expansion = input("full or progressive expansions for player one? (f/p)") == "p"
    two_expansion = input("full or progressive expansions for player two? (f/p)") == "p"
    one_move_time = float(input("move time for player one? (seconds)"))
    two_move_time = float(input("move time for player two? (seconds)"))

game_count = 1

while num_runs > 0:
    print("Starting game " + str(game_count))
    board = Board()
    while not board.won:
        if board.turn == 0:
            board.printboard()
            print(board.num_walls)
            runs = 0
            start = time.time()
            node = Node(board, one_rp, one_expansion)
            while (time.time() - start) < one_move_time:
                node.run()
                runs += 1
            print(runs)
            if logging:
                print(runs, file=log)
            board = node.children[0].board
            max_n = node.children[0].n
            max_wr = node.children[0].w/(node.children[0].n + 1)
            for child in node.children:
                ##child.board.printboard()
                if child.board.won:
                    board = child.board
                    board.printboard()
                    break
                if child.n > max_n:
                    max_wr = child.w/(child.n + 1)
                    max_n = child.n
                    board = child.board
                elif abs(child.n - max_n) < 2 and child.w/(child.n + 1) > max_wr:
                    max_wr = child.w/(child.n + 1)
                    max_n = child.n
                    board = child.board

            if board.turn != 1:
                print("FAIL")
                board.printboard()
                break
            ##board.printboard()
            ##board.prompt()
        else:
            board.printboard()
            runs = 0
            start = time.time()
            node = Node(board, two_rp, two_expansion)
            while (time.time() - start) < two_move_time:
                node.run()
                runs += 1
            print(runs)
            if logging:
                print(runs, file=log)
            board = node.children[0].board
            max_n = node.children[0].n
            max_wr = node.children[0].w/(node.children[0].n + 1)
            for child in node.children:
                if child.board.won:
                    board = child.board
                    board.printboard()
                    break
                if child.n > max_n:
                   max_wr = child.w/(child.n + 1)
                   max_n = child.n
                   board = child.board
                # and child.w/(child.n + 1) < max_wr because of switching players
                elif abs(child.n - max_n) < 2 and child.w/(child.n + 1) < max_wr:
                    max_wr = child.w/(child.n + 1)
                    max_n = child.n
                    board = child.board

            if board.turn != 0:
                board.printboard()
                break
    if logging:
        print(board.turn, file=log)
        print(board.playstack, file=log)
    print("Finished game " + str(game_count))
    game_count += 1
    num_runs -= 1

## close log file
log.close()
