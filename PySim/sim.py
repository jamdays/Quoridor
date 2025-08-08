from mcts import Node
from board import Board
import time
import sys

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


'''
START CONFIG
'''

quiet = input("quiet? (y/n)") == "y"
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
one_rp = .9
two_rp = .9
one_spp = .9
one_spp = .9
one_expansion = True
two_expansion = True
one_move_time = 2
two_move_time = 2
one_chooser = lambda x: choose_by_visits(0, x)
two_chooser = lambda x: choose_by_visits(1, x)
checker ="Default"
if len(sys.argv) > 2: 
    checker = "UF"

if (input("advanced options? (y/n)") != "n"):
    one_rp = float(input("level of bias towards moving for player one? (.5 = 50%)"))
    two_rp = float(input("level of bias towards moving for player two?"))
    one_spp = float(input("level of bias towards moving to shortest path for player one? (.5 = 50%)"))
    two_spp = float(input("level of bias towards moving to shortest path for player two?"))
    one_expansion = input("full or progressive expansions for player one? (f/p)") == "p"
    two_expansion = input("full or progressive expansions for player two? (f/p)") == "p"
    one_move_time = float(input("move time for player one? (seconds)"))
    two_move_time = float(input("move time for player two? (seconds)"))
    if input("choose child by visits or winrate for player one? (wr/v)") != 'wr':
        one_chooser = lambda x: choose_by_visits(0, x)
    if input("choose child by visits or winrate for player two?") == 'wr':
        two_chooser = lambda x: choose_by_visits(1, x)



'''
player one default configuration
'''
def player_one_default(board):
    if not quiet:
        board.printboard()
        print(board.num_walls)
    runs = 0
    start = time.time()
    node = Node(board, one_rp, one_expansion)
    while (time.time() - start) < one_move_time:
        node.run()
        runs += 1
    if not quiet:
        print(runs)
    if logging:
        print(runs, file=log)

    return one_chooser(node)


'''
player two default configuration
'''
def player_two_default(board):
    if not quiet:
        board.printboard()
    runs = 0
    start = time.time()
    node = Node(board, two_rp, two_expansion)
    while (time.time() - start) < two_move_time:
        node.run()
        runs += 1
    if not quiet:
        print(runs)
    if logging:
        print(runs, file=log)

    return two_chooser(node)

def user_play(board):
    board.printboard()
    board.prompt()
    return board

def basline_agent(board):
    if not quiet:
        board.printboard()
    board.follow_shortest()

    return board

def wall_basline_agent(board):
    if not quiet:
        board.printboard()
    board.follow_shortest_or_wall()

    return board
play_one = player_one_default
play_two = player_two_default

if input("play with user input?(y/n)") == 'y':
    if input("player one user input?(y/n)") == 'y':
        play_one = user_play 
    if input("player two user input?(y/n)") == 'y':
        play_two = user_play 

if input("play with basline agent?(y/n)") == 'y':
    if input("player one baslien agent?(y/n)") == 'y':
        if input("baseline with walls or basic? (w/b)") == 'w':
            play_one = wall_basline_agent
        else: 
            play_one = basline_agent
    if input("player two baseline agent?") == 'y':
        if input("baseline with walls or basic? (w/b)") == 'w':
            play_two = wall_basline_agent
        else: 
            play_two = basline_agent
'''
END  CONFIG
'''





'''
START SIMULATION
'''
game_count = 1

while num_runs > 0:
    if logging:
        print(game_count)
        print("Game " + str(game_count), file=log)
        
    if not quiet:
        print("Starting game " + str(game_count))
    board = Board(check=checker)
    while not board.won:
        if not quiet:
            print(len(board.playstack))
            print(board.num_walls)
        if board.turn == 0:
            if (board.num_walls[0] + board.num_walls[1] != 0):
                board = play_one(board)
            else:
                board = basline_agent(board)
        else:
            if (board.num_walls[0] + board.num_walls[1] != 0):
                board = play_two(board)
            else:
                board = basline_agent(board)
        if len(board.playstack) > 99:
            break
    if logging:
        if board.won: 
            print(board.turn, file=log)
        else:
            print("-1", file=log)
        print(board.plays, file=log)
    if not quiet:
        print("Finished game " + str(game_count))
    game_count += 1
    num_runs -= 1

## close log file
if logging:
    log.close()
