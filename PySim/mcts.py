import math
import random
from board import Board

class Node:
    def __init__(self, board, rp, progressive=False):
        self.parent = None
        self.board = board
        self.w = 0
        self.n = 0
        self.children = []
        self.choose = self.best_child 
        self.generator = self.generate_children
        self.rp = rp
        if (progressive):
            self.child_q = []
            self.choose = self.progressive_expansion_choice
            self.generator = self.prog_generator
    
    def run(self):
        node = self
        while node.n != 0:
            if len(node.children) == 0: 
                node.generator()
                if len(node.children) == 0:
                    #because turn is opposite
                    node.backprop((node.board.turn*2) - 1)
                    return
                else:
                    node = node.children[random.randint(0, len(node.children) -1)]
            else:
                node = node.choose(1.4)
        node.backprop(node.full_biased_rollout())

    '''
    progressive expansion logic
    '''
    def progressive_expansion_choice(self, c):
        if (len(self.child_q) == 0):
            max_uct = -1
            best_child = self.children[0]
            for child in self.children:
                if child.uct(c, self.n) > max_uct:
                    best_child = child
                    max_uct = child.uct(c, self.n)
            return best_child
        else:
            return self.make_new_child()

    
    '''
    progressive expansion generator
    '''
    def prog_generator(self):
        self.generate_child_q()
        self.make_new_child();

    '''
    Make new child for progressive expansion
    '''
    def make_new_child(self):
        child = None
        if (len(self.child_q) == 0):
            return
        move = self.child_q.pop()
        if (isinstance(move, int)):
            child = Node(self.board.copy(), self.rp, progressive=True)
            child.board.wall(move)
            child.parent = self
            self.children.append(child)
        else:
            child = Node(self.board.copy(), self.rp, progressive=True)
            child.board.move(move)
            child.parent = self
            self.children.append(child)
        return child



    def uct(self, c, total):
        if self.board.turn == 0:
            return (self.w)/((self.n) + 1) + c*((math.log(total)/(self.n + 1))**.5)
        else:
            return -1*(self.w)/((self.n) + 1) + c*((math.log(total)/(self.n + 1))**.5)

    def partial_rollout(self, depth):
        sim = self.board.copy()
        c = 0;

        moves = ["wa", "wd", "aw", "as", "sa", "sd", "dw", "ds"]
        while c < depth:
            if sim.won:
                break
            if (random.random() < self.rp or sim.num_walls[sim.turn] == 0):
                if (sim.move(moves[random.randint(0,7)]) !=-1):
                    sim.playstack.append(sim.to_str())
                    c += 1
            else:
                tries = 20
                while tries > 0:
                    if (sim.wall(random.randint(0, 17*17 -1)) != -1):
                        sim.playstack.append(sim.to_str())
                        c += 1
                        break
                    tries -= 1
        lens = sim.path_lens()
        if lens[0] == 0 or (lens[0] == 1 and sim.turn == 0):
            ##TODO THINK OF A GOOD VALUE HERE
            return 10000
        elif lens[0] == 0 or (lens[0] == 1 and sim.turn == 0):        
            return -10000
        ##TODO THINK OF A FUNCTION OF TWO VARIABLES THAT IS more positive WHEN x is smaller than y
        ## AND more negative WHEN x is greater than y. AND the further the distance, the greater the
        ## value
        return lens[1] - lens[0] + .25*(sim.num_walls[1] - sim.num_walls[0])

    ##TODO tune probablilties
    def full_rollout(self): 
        sim = self.board.copy()
        moves = ["wa", "wd", "aw", "as", "sa", "sd", "dw", "ds"]
        while not sim.won:
            if (random.random() < self.rp or sim.num_walls[sim.turn] == 0):
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
        while not sim.won:
            if (random.random() < self.rp or sim.num_walls[sim.turn] == 0):
                if (random.random() > .6):
                    sim.move_num(sim.get_shortest_path_move())
                else:
                    sim.move(moves[random.randint(0,7)])
            else:
                tries = 20
                while tries > 0:
                    if (sim.wall(random.randint(0, 17*17 -1)) != -1):
                        break
                    tries -= 1
        #so that it returns -1 if p2 wins and 1 if p1 wins
        return ((sim.turn*-2) + 1)


    def best_child(self, c):
        max_uct = -1
        best_child = self.children[0]
        for child in self.children:
            if child.uct(c, self.n) > max_uct:
                best_child = child
                max_uct = child.uct(c, self.n)
        return best_child



    def backprop(self, won):
        self.w += won
        self.n += 1
        node = self.parent
        while node is not None:
            node.w += won
            node.n += 1
            node = node.parent
        return

    def generate_children(self):
        if (self.board.num_walls[self.board.turn] > 0):
            for i in range(17*17):
                newboard = self.board.copy()
                if (newboard.wall(i) != -1):
                    child = Node(newboard.copy(), self.rp)
                    child.parent = self
                    self.children.append(child)
                    if self.board == child.board:
                        print("LINE 125 board")
        moves = ["w", "a", "s", "d"]
        ws = ["wa", "wd"]
        ss = ["sa", "sd"]
        ehs = ["aw", "as"]
        ds = ["dw", "ds"]
        for move in moves:
            newboard = self.board.copy()
            if (newboard.move(move) == 1):
                child = Node(newboard.copy(), self.rp)
                child.parent = self
                self.children.append(child)
                if self.board == child.board:
                    print("LINE 138 board")
            elif move == "w":
                for w in ws:
                    new_other_board = self.board.copy()
                    if (new_other_board.move(w) == 1):
                        child = Node(new_other_board.copy(), self.rp)
                        child.parent = self
                        self.children.append(child)
                        if self.board == child.board:
                            print("LINE 147 board")
            elif move == "a":
                for a in ehs:
                    new_other_board = self.board.copy()
                    if (new_other_board.move(a) == 1):
                        child = Node(new_other_board.copy(), self.rp)
                        child.parent = self
                        self.children.append(child)
                        if self.board == child.board:
                            print("LINE 156 board")
            elif move == "d":
                for d in ds:
                    new_other_board = self.board.copy()
                    if (new_other_board.move(d) == 1):
                        child = Node(new_other_board.copy(), self.rp)
                        child.parent = self
                        self.children.append(child)
                        if self.board == child.board:
                            print("LINE 165 board")
            elif move == "s":
                for s in ss:
                    new_other_board = self.board.copy()
                    if (new_other_board.move(s) == 1):
                        child = Node(new_other_board.copy(), self.rp)
                        child.parent = self
                        self.children.append(child)
                        if self.board == child.board:
                            print("LINE 174 board")




    def generate_child_q(self):
        if (self.board.num_walls[self.board.turn] > 0):
            for i in range(17*17):
                newboard = self.board.copy()
                if (newboard.wall(i) != -1):
                    self.child_q.append(i)
        moves = ["w", "a", "s", "d"]
        ws = ["wa", "wd"]
        ss = ["sa", "sd"]
        ehs = ["aw", "as"]
        ds = ["dw", "ds"]
        for move in moves:
            newboard = self.board.copy()
            if (newboard.move(move) == 1):
                self.child_q.append(move)
            elif move == "w":
                for w in ws:
                    new_other_board = self.board.copy()
                    if (new_other_board.move(w) == 1):
                        self.child_q.append(w)
            elif move == "a":
                for a in ehs:
                    new_other_board = self.board.copy()
                    if (new_other_board.move(a) == 1):
                        self.child_q.append(a)
            elif move == "d":
                for d in ds:
                    new_other_board = self.board.copy()
                    if (new_other_board.move(d) == 1):
                        self.child_q.append(d)
            elif move == "s":
                for s in ss:
                    new_other_board = self.board.copy()
                    if (new_other_board.move(s) == 1):
                        self.child_q.append(s)
        ##shuffle queue
        for i in range(len(self.child_q)):
            temp = self.child_q[len(self.child_q) - 1] 
            choice = random.randint(0, len(self.child_q) - 1)
            self.child_q[len(self.child_q) - 1] = self.child_q[choice]
            self.child_q[choice] = temp;
                

