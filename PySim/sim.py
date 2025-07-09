from mcts import Node
from board import Board
import time

'''
choose the child node by which one has been visited the most
returns child node
'''
def choose_by_visits(player, node):
    board = node.children[0].board
    max_n = node.children[0].n
    max_wr = node.children[0].w/(node.children[0].n + 1)
    compare = lambda x,y: x < y
    if player == 0:
        compare = lambda x,y: x > y
        
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
        elif abs(child.n - max_n) < 2 and compare(child.w/(child.n + 1), max_wr):
            max_wr = child.w/(child.n + 1)
            max_n = child.n
            board = child.board
    return board


'''
choose the child node by which one has the highest win rate
returns child node
'''
def choose_by_wr(player, node):
    board = node.children[0].board
    max_n = node.children[0].n
    max_wr = node.children[0].w/(node.children[0].n + 1)
    compare = lambda x,y: x < y
    if player == 0:
        compare = lambda x,y: x > y
        
    for child in node.children:
        if child.board.won:
            board = child.board
            board.printboard()
            break
        if compare(child.w/(child.n + 1), max_wr):
           max_wr = child.w/(child.n + 1)
           max_n = child.n
           board = child.board
        # and child.w/(child.n + 1) < max_wr because of switching players
        elif child.n > max_n:
            max_wr = child.w/(child.n + 1)
            max_n = child.n
            board = child.board
    return board

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
one_chooser = lambda x: choose_by_visits(0, x)
two_chooser = lambda x: choose_by_visits(1, x)

if (input("advanced options? (y/n)") != "n"):
    one_rp = float(input("level of bias towards moving for player one? (.5 = 50%)"))
    two_rp = float(input("level of bias towards moving for player two?"))
    one_expansion = input("full or progressive expansions for player one? (f/p)") == "p"
    two_expansion = input("full or progressive expansions for player two? (f/p)") == "p"
    one_move_time = float(input("move time for player one? (seconds)"))
    two_move_time = float(input("move time for player two? (seconds)"))
    if input("choose child by visits or winrate for player one? (w/v)") == 'w':
        one_chooser = lambda x: choose_by_wr(0, x)
    if input("choose child by visits or winrate for player two?") == 'w':
        two_chooser = lambda x: choose_by_wr(1, x)

game_count = 1

while num_runs > 0:
    if logging:
        print("Game " + str(game_count), file=log)
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

            board = choose_by_visits(0, node)

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

            board = choose_by_visits(1, node)

            if board.turn != 0:
                board.printboard()
                break
    if logging:
        print(board.turn, file=log)
        print(board.plays, file=log)
    print("Finished game " + str(game_count))
    game_count += 1
    num_runs -= 1

## close log file
if logging:
    log.close()
