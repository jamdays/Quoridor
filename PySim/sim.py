from mcts import Node
from board import Board
import time

board = Board()
while not board.won:
    if board.turn == 0:
        board.printboard()
        board.prompt()
    else:
        runs = 5000
        node = Node(board)
        while runs != 0:
            node.run()
            runs -= 1
        new_board = board
        max_wr = 0 
        for child in node.children:
            if child.n != 0 and (child.w/child.n) < max_wr:
                max_wr = child.w/child.n
                board = child.board
        if board.turn != 0:
            board.printboard()
            break
        
