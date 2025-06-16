from mcts import Node
from board import Board
import time

board = Board()
while not board.won:
    if board.turn == 0:
        board.printboard()
        print(board.num_walls)
        runs = 0
        start = time.time()
        node = Node(board)
        while (time.time() - start) < 2:
            node.run()
            runs += 1
        print(runs)
        board = node.children[0].board
        max_n = node.children[0].n
        max_wr = node.children[0].w/(node.children[0].n + 1)
        for child in node.children:
            ##child.board.printboard()
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
    else:
        board.printboard()
        runs = 0
        start = time.time()
        node = Node(board)
        while (time.time() - start) < 2:
            node.run()
            runs += 1
        print(runs)
        board = node.children[0].board
        max_n = node.children[0].n
        max_wr = node.children[0].w/(node.children[0].n + 1)
        for child in node.children:
            if child.n > max_n:
                max_wr = child.w/(child.n + 1)
                max_n = child.n
                board = child.board
            elif abs(child.n - max_n) < 2 and child.w/(child.n + 1) < max_wr:
                max_wr = child.w/(child.n + 1)
                max_n = child.n
                board = child.board

        if board.turn != 0:
            board.printboard()
            break
        
