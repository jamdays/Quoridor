import math

class node:
    def __init__(self, board):
        self.parent = None
        self.board = board
        self.w = 0
        self.n = 0
        self.children = []

    def uct(self, c, total):
        return (self.w)/((self.n) + 1) + c*((math.log(total)/self.n)**.5)

    def rollout(self):
        ##TODO
        won = 0
        return won

    def best_child(self, c, total):
        max_uct = -1
        best_child = None
        for child in self.children:
            if child.uct(c, total) > max_uct:
                best_child = child
                max_uct = child.uct(c, total)
        return best_child

    def backprop(self, won):
        self.v += won
        self.n += 1
        node = self.parent
        while (node is not None):
            node.v += won
            node.n += 1
            node = node.parent
        return

    def generate_children(self):
        for i in range(17*17):
            newboard = self.board.copy()
            if (newboard.wall(i) != -1):
                child = node(newboard)
                child.parent = self
                self.children += child
        moves = ["w", "a", "s", "d"]
        ws = ["wa", "wd"]
        ss = ["sa", "sd"]
        ehs = ["aw", "as"]
        ds = ["dw", "ds"]
        for move in moves:
            newboard = self.board.copy()
            if (newboard.move(move) != -1):
                child = node(newboard)
                child.parent = self
                self.children += child
            ##TODO do upleft upright etc


            
