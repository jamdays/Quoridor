import math
import random

class node:
    def __init__(self, board):
        self.parent = None
        self.board = board
        self.w = 0
        self.n = 0
        self.children = []
    
    def run(self):
        if self.n == 0:
            self.backprop(partial_rollout(200))
        else:
            run(self.best_child())


    def uct(self, c, total):
        return (self.w)/((self.n) + 1) + c*((math.log(total)/self.n)**.5)

    def partial_rollout(self, depth):
        sim = self.board.copy()
        c = 0;

        moves = ["wa", "wd", "aw", "as", "sa", "sd", "dw", "ds"]
        while c < depth:
            if sim.won:
                break
            if (random.random() > .7 || sim.walls[sim.turn] == 0):
                if (sim.move(moves[random.randint(0,7)]) !=-1):
                    c += 1
            else:
                tries = 20
                while tries > 0:
                    if (sim.wall(random.randint(0, 17*17 -1)) != -1):
                        c += 1
                        break
                    tries -= 1
        lens = sim.path_lens()
        if lens[0] == 0 or (lens[0] == 1 and sim.turn == 0):
            ##TODO THINK OF A GOOD VALUE HERE
            return 100
        elif lens[0] == 0 or (lens[0] == 1 and sim.turn == 0):        
            return -100
        ##TODO THINK OF A FUNCTION OF TWO VARIABLES THAT IS more positive WHEN x is smaller than y
        ## AND more negative WHEN x is greater than y. AND the further the distance, the greater the
        ## value
        return lens[0] - lens[1] + .25(sim.walls[0] - sim.walls[1])

    ##TODO tune probablilties
    def full_rollout(self): sim = self.board.copy()
        moves = ["wa", "wd", "aw", "as", "sa", "sd", "dw", "ds"]
        while !sim.won:
            if (random.random() > .7 || sim.walls[sim.turn] == 0):
                sim.move(moves[random.randint(0,7)])
            else:
                tries = 20
                while tries > 0:
                    if (sim.wall(random.randint(0, 17*17 -1)) != -1):
                        c += 1
                        break
                    tries -= 1
        return sim.turn


    ##TODO tune probablilties
    def full_biased_rollout(self):
        sim = self.board.copy()
        moves = ["wa", "wd", "aw", "as", "sa", "sd", "dw", "ds"]
        while !sim.won:
            if (random.random() > .7 || sim.walls[sim.turn] == 0):
                if (random.random() > .6):
                    sim.move_num(sim.get_shortest_path_move())
                else:
                    sim.move(moves[random.randint(0,7)])
            else:
                tries = 20
                while tries > 0:
                    if (sim.wall(random.randint(0, 17*17 -1)) != -1):
                        c += 1
                        break
                    tries -= 1
        return sim.turn


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
                child = node(newboard.copy())
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
                child = node(newboard.copy())
                child.parent = self
                self.children += child
            elif move == "w":
                for w in ws:
                    new_other_board = self.board.copy()
                    if (new_other_board.move(w) != -1)
                        child = node(new_other_board.copy())
                        child.parent = self
                        self.children += child
            elif move == "a":
                for a in ehs:
                    new_other_board = self.board.copy()
                    if (new_other_board.move(a) != -1)
                        child = node(new_other_board.copy())
                        child.parent = self
                        self.children += child
            elif move == "d":
                for d in ds:
                    new_other_board = self.board.copy()
                    if (new_other_board.move(d) != -1)
                        child = node(new_other_board.copy())
                        child.parent = self
                        self.children += child
            elif move == "s":
                for s in ss:
                    new_other_board = self.board.copy()
                    if (new_other_board.move(s) != -1)
                        child = node(new_other_board.copy())
                        child.parent = self
                        self.children += child




