class Board:
    def __init__(self):
        self.locs = [0*17 + 8, 16*17 + 8]
        self.num_walls = [10, 10]
        self.walls = set()
        self.turn = 0
        self.won = False

    def __init__(self, locs, num_walls, walls, turn, won):
        ## Check that set and array copy are deep copies
        self.locs = [locs[0], locs[1]]
        self.num_walls = [num_walls[0], num_walls[1]]
        self.walls = set(walls)
        self.won = won


    def copy(self):
        return Board(self.locs, self.num_walls, self.walls, self.turn, self.won)

    def canWin(self):
        visited = set()
        one_done = False
        stack = []
        stack.append(self.locs[0])
        while not (one_done or len(stack) == 0):
            curr = stack.pop()
            if curr >= 16*17:
                two_done = True
            visited.add(curr)
            if curr > 17 and curr - 17 not in self.walls:
                stack.append(curr - 34)
            if curr < 17*16 and curr + 17 not in self.walls:
                stack.append(curr + 34)
            if curr % 17 > 1 and curr - 1 not in self.walls:
                stack.append(curr - 2)
            if curr % 17 < 16 and curr + 1 not in self.walls:
                stack.append(curr + 2)
        
        visited = set()
        two_done = False
        stack = []
        stack.append(self.locs[1])
        while not (two_done or len(stack) == 0):
            curr = stack.pop()
            if curr < 17:
                two_done = True
            visited.add(curr)
            if curr > 17 and curr - 17 not in self.walls:
                stack.append(curr - 34)
            if curr < 17*16 and curr + 17 not in self.walls:
                stack.append(curr + 34)
            if curr % 17 > 1 and curr - 1 not in self.walls:
                stack.append(curr - 2)
            if curr % 17 < 16 and curr + 1 not in self.walls:
                stack.append(curr + 2)
        return two_done and one_done

    def checkWon(self):
        if self.won:
            return
        if self.locs[0] >= 16*17:
            print("red wins!")
            self.won = True
        if self.locs[1] < 17:
            print("blue wins!")
            self.won = True

    def wall(self, k):
        if self.won:
            return -1
        if ((k % 17) > 15) or (k > 17*16):
            ##print("wall placement out of bounds")
            return -1
        if (k//17 % 2) and  not ((k % 17) % 2):
            if ((k in self.walls) or ((k + 1) in self.walls) or ((k + 2) in self.walls)):
                ##print("wall placement conflict")
                return -1
            else:
                self.walls.add(k)
                self.walls.add(k + 1)
                self.walls.add(k + 2)
                self.num_walls[self.turn] -= 1
                self.turn = (self.turn ^ 1)
                return 1
        elif ((k % 17) % 2):
            if ((k in self.walls) or ((k + 17) in self.walls) or ((k + 34) in self.walls)):
                #print("wall placement conflict")
                return -1
            else:
                self.walls.add(k)
                self.walls.add(k + 17)
                self.walls.add(k + 34)
                self.num_walls[self.turn] -= 1
                self.turn = (self.turn ^ 1)
                return 1
        return "-1"

    def move(self, direction):
        if self.won:
            return
        if (direction[0] == "w"):
            if (self.locs[self.turn] - 34 < 0):
                #print("out of bounds")
                return -1
            elif (self.locs[self.turn] - 17) in self.walls:
                #print("wall in the way")
                return -1
            ##CODE FOR HANDLING JUMP RULE
            elif (self.locs[self.turn] - 34 == self.locs[self.turn^1]):
                if (self.locs[self.turn] - 68 > 0) and (self.locs[self.turn] - 51) not in self.walls:
                    self.locs[self.turn] -= 68
                    self.checkWon()
                    self.turn = (self.turn ^ 1)
                    return 1
                elif (len(direction) > 1 and direction[1] == "d"):
                    if (self.locs[self.turn] % 17 > 15):
                        #print("out of bounds")
                        return -1
                    elif (self.locs[self.turn] - 33) in self.walls:
                        #print("wall in the way")
                        return -1
                    else: 
                        self.locs[self.turn] -= 32
                        self.checkWon()
                        self.turn = (self.turn ^ 1)
                elif (len(direction) > 1 and direction[1] == "a"):
                    if (self.locs[self.turn] % 17 < 2):
                        #print("out of bounds")
                        return -1
                    elif (self.locs[self.turn] - 35) in self.walls:
                        #print("wall in the way")
                        return -1
                    else: 
                        self.locs[self.turn] -= 36
                        self.checkWon()
                        self.turn = (self.turn ^ 1)
                        return 1
                else:
                    return -1
            ##END CODE FOR HANDLING JUMP RULE
            else: 
                self.locs[self.turn] -= 34
                self.checkWon()
                self.turn = (self.turn ^ 1)
                return 1
        if (direction[0] == "s"):
            if (self.locs[self.turn] + 34 >= 17*17):
                #print("out of bounds")
                return -1
            elif (self.locs[self.turn] + 17) in self.walls:
                #print("wall in the way")
                return -1
            ##CODE FOR HANDLING JUMP RULE
            elif (self.locs[self.turn] + 34 == self.locs[self.turn^1]):
                if (self.locs[self.turn] + 68 > 0) and (self.locs[self.turn] + 51) not in self.walls:
                    self.locs[self.turn] += 68
                    self.checkWon()
                    self.turn = (self.turn ^ 1)
                    return
                elif (len(direction) > 1 and direction[1] == "d"):
                    if (self.locs[self.turn] % 17 > 15):
                        #print("out of bounds")
                        return -1
                    elif (self.locs[self.turn] + 35) in self.walls:
                        #print("wall in the way")
                        return -1
                    else: 
                        self.locs[self.turn] += 36
                        self.checkWon()
                        self.turn = (self.turn ^ 1)
                elif (len(direction) > 1 and direction[1] == "a"):
                    if (self.locs[self.turn] % 17 < 2):
                        #print("out of bounds")
                        return -1
                    elif (self.locs[self.turn] + 33) in self.walls:
                        #print("wall in the way")
                        return -1
                    else: 
                        self.locs[self.turn] += 32
                        self.checkWon()
                        self.turn = (self.turn ^ 1)
                        return 1
                else:
                    return -1
            ##END CODE FOR HANDLING JUMP RULE
            else: 
                self.locs[self.turn] += 34
                self.checkWon()
                self.turn = (self.turn ^ 1)
                return 1
        if (direction[0] == "d"):
            if (self.locs[self.turn] % 17 > 15):
                #print("out of bounds")
                return -1
            elif (self.locs[self.turn] + 1) in self.walls:
                #print("wall in the way")
                return -1
            ##CODE FOR HANDLING JUMP RULE
            elif (self.locs[self.turn] + 2 == self.locs[self.turn^1]):
                if (self.locs[self.turn] + 4 > 0) and (self.locs[self.turn] + 3) not in self.walls:
                    self.locs[self.turn] += 4
                    self.checkWon()
                    self.turn = (self.turn ^ 1)
                    return
                elif (len(direction) > 1 and direction[1] == "w"):
                    if (self.locs[self.turn] - 34 < 0):
                        #print("out of bounds")
                        return -1
                    elif (self.locs[self.turn] -33) in self.walls:
                        #print("wall in the way")
                        return -1
                    else: 
                        self.locs[self.turn] -= 32
                        self.checkWon()
                        self.turn = (self.turn ^ 1)
                elif (len(direction) > 1 and direction[1] == "s"):
                    if (self.locs[self.turn] + 34 >= 17*17):
                        #print("out of bounds")
                        return -1
                    elif (self.locs[self.turn] + 35) in self.walls:
                        #print("wall in the way")
                        return -1
                    else: 
                        self.locs[self.turn] += 36
                        self.checkWon()
                        self.turn = (self.turn ^ 1)
                        return 1
                else:
                    return -1
            ##END CODE FOR HANDLING JUMP RULE
            else: 
                self.locs[self.turn] += 2
                self.checkWon()
                self.turn = (self.turn ^ 1)
                return 1
        if (direction[0] == "a"):
            if (self.locs[self.turn] % 17 < 2):
                #print("out of bounds")
                return -1
            elif (self.locs[self.turn] - 1) in self.walls:
                #print("wall in the way")
                return -1
            ##CODE FOR HANDLING JUMP RULE
            elif (self.locs[self.turn] - 2 == self.locs[self.turn^1]):
                if (self.locs[self.turn] - 4 > 0) and (self.locs[self.turn] - 3) not in self.walls:
                    self.locs[self.turn] -= 4
                    self.checkWon()
                    self.turn = (self.turn ^ 1)
                    return
                elif (len(direction) > 1 and direction[1] == "w"):
                    if (self.locs[self.turn] - 34 < 0):
                        #print("out of bounds")
                        return -1
                    elif (self.locs[self.turn] - 35) in self.walls:
                        #print("wall in the way")
                        return -1
                    else: 
                        self.locs[self.turn] -= 36
                        self.checkWon()
                        self.turn = (self.turn ^ 1)
                elif (len(direction) > 1 and direction[1] == "s"):
                    if (self.locs[self.turn] + 34 >= 17*17):
                        #print("out of bounds")
                        return -1
                    elif (self.locs[self.turn] + 33) in self.walls:
                        #print("wall in the way")
                        return -1
                    else: 
                        self.locs[self.turn] += 32
                        self.checkWon()
                        self.turn = (self.turn ^ 1)
                        return 1
                else:
                    return -1
            ##END CODE FOR HANDLING JUMP RULE
            else: 
                self.locs[self.turn] -= 2
                self.checkWon()
                self.turn = (self.turn ^ 1)
                return 1
        return -1

    def printboard_old(self):
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

    def printboard(self):
        boardstr = "* 1 2 3 4 5 6 7 8 9\n1 "
        for r in range(17):
            for c in range(17):
                if (r*17 + c) in self.walls:
                    if (r % 2 == 0):
                        boardstr += "\033[93m|\033[0m"
                    elif (c % 2 == 0):
                        boardstr += "\033[93m-\033[0m"
                    elif (c % 1 == 0):
                        boardstr += "\033[93m*\033[0m"
                elif (r*17 + c) == self.locs[0]:
                    boardstr += "\033[91m\u25C9\033[0m"
                elif (r*17 + c) == self.locs[1]:
                    boardstr += "\033[96m\u25D9\033[0m"
                else:
                    if (r % 2 == 0):
                        if (c % 2 == 1):
                            boardstr += "|"
                        else:
                            boardstr += " "
                    else:
                        if (c % 2 == 1):
                            boardstr += " "
                        else:
                            boardstr += "-"
            boardstr += "\n"
            if (r % 2 == 1):
                boardstr += str(r//2 + 2) + " "
            else:
                boardstr += "  "
        print(boardstr)
        
    def play(self):
        self.printboard()
        while (True and not self.won):
            choice = input("Player " + str(self.turn + 1) + "'s turn, move or wall? (type move/wall or m/w)")
            if (choice == "m" or choice == "move"):
                choice = input("w/a/s/d?")
                self.move(choice)
                self.printboard()
            elif (choice == "w" or choice == "wall"):
                hv = input("horizontal or vertical (h/v)?")
                rc = input("which row/column is the first part of the wall at?")
                rc = int(rc)
                if (hv == "v"):
                    rcl = input("which row/column is to the left of wall?")
                    rcr = input("which row/column is to the right of wall?")
                    rcr = int(rcr)
                    rcl = int(rcl)
                    choice = (rc - 1)*2*17 + (rcr - 1)*2
                else:
                    rcd = input("which row/column is below the wall?")
                    rcu = input("which row/column is above the wall?")
                    rcd = int(rcd)
                    rcu = int(rcu)
                    choice = (((rcu -1)*2) + 1)*17 + (rc - 1)*2

                self.wall(choice)
                self.printboard()
    


board = Board()
board.play()
