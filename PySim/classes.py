class Board:
    def __init__(self):
        self.locs = [0*17 + 8, 16*17 + 8]
        self.num_walls = [10, 10]
        self.walls = set()
        self.turn = 0
        self.won = False

    def checkWon(self):
        if self.won:
            return
        if self.locs[0] >= 16*17:
            self.won = True
        if self.locs[1] < 17:
            self.won = True

    def wall(self, k):
        if self.won:
            return
        if ((k % 17) > 15) or (k > 17*16):
            return "wall placement out of bounds"
        if (k//17 % 2) and  not ((k % 17) % 2):
            if ((k in self.walls) or ((k + 1) in self.walls) or ((k + 2) in self.walls)):
                return "wall placement conflict"
            else:
                self.walls.add(k)
                self.walls.add(k + 1)
                self.walls.add(k + 2)
                self.num_walls[self.turn] -= 1
                self.turn = (self.turn ^ 1)
        elif ((k % 17) % 2):
            if ((k in self.walls) or ((k + 17) in self.walls) or ((k + 34) in self.walls)):
                return "wall placement conflict"
            else:
                self.walls.add(k)
                self.walls.add(k + 17)
                self.walls.add(k + 34)
                self.num_walls[self.turn] -= 1
                self.turn = (self.turn ^ 1)
        return "uknown error"

    def move(self, direction):
        if self.won:
            return
        if (direction[0] == "w"):
            if (self.locs[self.turn] - 34 < 0):
                return "out of bounds"
            elif (self.locs[self.turn] - 17) in self.walls:
                return "wall in the way"
            ##CODE FOR HANDLING JUMP RULE
            elif (self.locs[self.turn] - 34 == self.locs[self.turn^1]):
                if (self.locs[self.turn] - 68 > 0) and (self.locs[self.turn] - 51) not in self.walls:
                    self.locs[self.turn] -= 68
                    self.checkWon()
                    self.turn = (self.turn ^ 1)
                    return
                elif (len(direction) > 1 and direction[1] == "d"):
                    if (self.locs[self.turn] % 17 > 15):
                        return "out of bounds"
                    elif (self.locs[self.turn] - 33) in self.walls:
                        return "wall in the way"
                    else: 
                        self.locs[self.turn] -= 32
                        self.checkWon()
                        self.turn = (self.turn ^ 1)
                elif (len(direction) > 1 and direction[1] == "a"):
                    if (self.locs[self.turn] % 17 < 2):
                        return "out of bounds"
                    elif (self.locs[self.turn] - 35) in self.walls:
                        return "wall in the way"
                    else: 
                        self.locs[self.turn] -= 36
                        self.checkWon()
                        self.turn = (self.turn ^ 1)
                        return
            ##END CODE FOR HANDLING JUMP RULE
            else: 
                self.locs[self.turn] -= 34
                self.checkWon()
                self.turn = (self.turn ^ 1)
                return
        if (direction[0] == "s"):
            if (self.locs[self.turn] + 34 >= 17*17):
                return "out of bounds"
            elif (self.locs[self.turn] + 17) in self.walls:
                return "wall in the way"
            ##CODE FOR HANDLING JUMP RULE
            elif (self.locs[self.turn] + 34 == self.locs[self.turn^1]):
                if (self.locs[self.turn] + 68 > 0) and (self.locs[self.turn] + 51) not in self.walls:
                    self.locs[self.turn] += 68
                    self.checkWon()
                    self.turn = (self.turn ^ 1)
                    return
                elif (len(direction) > 1 and direction[1] == "d"):
                    if (self.locs[self.turn] % 17 > 15):
                        return "out of bounds"
                    elif (self.locs[self.turn] + 35) in self.walls:
                        return "wall in the way"
                    else: 
                        self.locs[self.turn] += 36
                        self.checkWon()
                        self.turn = (self.turn ^ 1)
                elif (len(direction) > 1 and direction[1] == "a"):
                    if (self.locs[self.turn] % 17 < 2):
                        return "out of bounds"
                    elif (self.locs[self.turn] + 33) in self.walls:
                        return "wall in the way"
                    else: 
                        self.locs[self.turn] += 32
                        self.checkWon()
                        self.turn = (self.turn ^ 1)
                        return
            ##END CODE FOR HANDLING JUMP RULE
            else: 
                self.locs[self.turn] += 34
                self.checkWon()
                self.turn = (self.turn ^ 1)
                return
        if (direction[0] == "d"):
            if (self.locs[self.turn] % 17 > 15):
                return "out of bounds"
            elif (self.locs[self.turn] + 1) in self.walls:
                return "wall in the way"
            ##CODE FOR HANDLING JUMP RULE
            elif (self.locs[self.turn] + 2 == self.locs[self.turn^1]):
                if (self.locs[self.turn] + 4 > 0) and (self.locs[self.turn] + 3) not in self.walls:
                    self.locs[self.turn] += 4
                    self.checkWon()
                    self.turn = (self.turn ^ 1)
                    return
                elif (len(direction) > 1 and direction[1] == "w"):
                    if (self.locs[self.turn] - 34 < 0):
                        return "out of bounds"
                    elif (self.locs[self.turn] -33) in self.walls:
                        return "wall in the way"
                    else: 
                        self.locs[self.turn] -= 32
                        self.checkWon()
                        self.turn = (self.turn ^ 1)
                elif (len(direction) > 1 and direction[1] == "s"):
                    if (self.locs[self.turn] + 34 >= 17*17):
                        return "out of bounds"
                    elif (self.locs[self.turn] + 35) in self.walls:
                        return "wall in the way"
                    else: 
                        self.locs[self.turn] += 36
                        self.checkWon()
                        self.turn = (self.turn ^ 1)
                        return
            ##END CODE FOR HANDLING JUMP RULE
            else: 
                self.locs[self.turn] += 2
                self.checkWon()
                self.turn = (self.turn ^ 1)
                return
        if (direction[0] == "a"):
            if (self.locs[self.turn] % 17 < 2):
                return "out of bounds"
            elif (self.locs[self.turn] - 1) in self.walls:
                return "wall in the way"
            ##CODE FOR HANDLING JUMP RULE
            elif (self.locs[self.turn] - 2 == self.locs[self.turn^1]):
                if (self.locs[self.turn] - 4 > 0) and (self.locs[self.turn] - 3) not in self.walls:
                    self.locs[self.turn] -= 4
                    self.checkWon()
                    self.turn = (self.turn ^ 1)
                    return
                elif (len(direction) > 1 and direction[1] == "w"):
                    if (self.locs[self.turn] - 34 < 0):
                        return "out of bounds"
                    elif (self.locs[self.turn] - 35) in self.walls:
                        return "wall in the way"
                    else: 
                        self.locs[self.turn] -= 36
                        self.checkWon()
                        self.turn = (self.turn ^ 1)
                elif (len(direction) > 1 and direction[1] == "s"):
                    if (self.locs[self.turn] + 34 >= 17*17):
                        return "out of bounds"
                    elif (self.locs[self.turn] + 33) in self.walls:
                        return "wall in the way"
                    else: 
                        self.locs[self.turn] += 32
                        self.checkWon()
                        self.turn = (self.turn ^ 1)
                        return
            ##END CODE FOR HANDLING JUMP RULE
            else: 
                self.locs[self.turn] -= 2
                self.checkWon()
                self.turn = (self.turn ^ 1)
                return
        return "invalid direction"

    def printboard(self):
        boardstr = ""
        for r in range(17):
            for c in range(17):
                if (r*17 + c) in self.walls:
                    boardstr += "\033[93m\u25A0\033[0m "
                elif (r*17 + c) == self.locs[0]:
                    boardstr += "\033[91m\u25C9\033[0m "
                elif (r*17 + c) == self.locs[1]:
                    boardstr += "\033[96m\u25D9\033[0m "
                else:
                    boardstr += "\u25A0 "
            boardstr += "\n"
        print(boardstr)

    def play(self):
        while (True):
            choice = input("Player " + str(self.turn + 1) + "'s turn, move or wall? (type move/wall or m/w)")
            if (choice == "m" or choice == "move"):
                choice = input("w/a/s/d?")
                self.move(choice)
                self.printboard()
            elif (choice == "w" or choice == "wall"):
                choice = input("where would you like to place the wall?")
                choice = int(choice)
                self.wall(choice)
                self.printboard()

board = Board()
board.play()
