from mcts import Node
from board import Board
import time

board = Board()
board.printboard()
while not board.won:
    if board.turn == 0:
        board.prompt()
    else:
        start = time.time()
        node = Node(board)
        while (time.time() - start < 3):
            node.run()
            print("DONE RUNNING ONCE")
        new_board = board
        max_wr = 0
        for child in node.children:
            if child.n != 0 and (child.w/child.n) > max_wr:
                max_wr = child.w/child.n
                board = child.board
                board.printboard()
        
