class Board:
    def __init__(self, locs=[0*17 + 8, 16*17 + 8], num_walls=[10,10], walls=set(), turn=0, won=False, plays=[], playstack=[]):
        ##Check that set and array copy are deep copies
        self.locs = [locs[0], locs[1]]
        self.num_walls = [num_walls[0], num_walls[1]]
        self.walls = set(walls)
        self.won = won
        self.turn = turn
        self.plays = list(plays)
        self.playstack = list(playstack)

    def __eq__(self, other):
        return self.locs[0] == other.locs[0] and self.locs[0] == other.locs[0] and \
                self.walls == other.walls and self.turn == other.turn

    def copy(self):
        return Board(self.locs, self.num_walls, self.walls, self.turn, self.won, self.plays, self.playstack)
    
    def path_lens(self):
        visited = set()
        queue = []
        idx = 0
        one_path_length = float('inf')
        queue.append((self.locs[0], 0))
        while queue:
            try:
                if queue[idx][0] >= 16*17:
                    one_path_length = queue[idx][1]
                    break
            except:
                print(len(queue))
                print(idx)
                self.printboard()
                print(self.plays)
                print(self.locs)
                print(self.walls)
                print(self.num_walls)
                print(self.turn)
                for i in range(len(self.playstack)):
                    print(self.playstack[i])
            visited.add(queue[idx][0])
            curr = queue[idx][0]
            if curr > 17 and curr - 17 not in self.walls and curr - 34 not in visited:
                queue.append((curr - 34, queue[idx][1]+1))
            if curr < 17*16 and curr + 17 not in self.walls and curr + 34 not in visited:
                queue.append((curr + 34, queue[idx][1]+1))
            if curr % 17 > 1 and curr - 1 not in self.walls and curr - 2 not in visited:
                queue.append((curr - 2, queue[idx][1]+1))
            if curr % 17 < 16 and curr + 1 not in self.walls and curr + 2 not in visited:
                queue.append((curr + 2, queue[idx][1]+1))
            idx += 1
        visited = set()
        queue = []
        idx = 0
        two_path_length = float('inf')
        queue.append((self.locs[1], 0))
        while queue:
            try:
                if queue[idx][0] < 17:
                    two_path_length = queue[idx][1]
                    break
            except:
                print(len(queue))
                print(idx)
                self.printboard()
                print(self.plays)
                print(self.locs)
                print(self.walls)
                print(self.num_walls)
                print(self.turn)
                for i in range(len(self.playstack)):
                    print(self.playstack[i])
            visited.add(queue[idx][0])
            curr = queue[idx][0]
            if curr > 17 and curr - 17 not in self.walls and curr - 34 not in visited:
                queue.append((curr - 34, queue[idx][1]+1))
            if curr < 17*16 and curr + 17 not in self.walls and curr + 34 not in visited:
                queue.append((curr + 34, queue[idx][1]+1))
            if curr % 17 > 1 and curr - 1 not in self.walls and curr - 2 not in visited:
                queue.append((curr - 2, queue[idx][1]+1))
            if curr % 17 < 16 and curr + 1 not in self.walls and curr + 2 not in visited:
                queue.append((curr + 2, queue[idx][1]+1))
            idx += 1
        return (one_path_length, two_path_length)
                
    def get_shortest_path_move(self):
        visited = set()
        queue = []
        idx = 0
        one_path_length = float('inf')
        queue.append((self.locs[self.turn], 0, None))
        goal = lambda x: x >= 16*17
        if self.turn == 1:
            goal = lambda x: x < 17
        while queue:
            if goal(queue[idx][0]):
                one_path_length = queue[idx][1]
                break
            visited.add(queue[idx][0])
            curr = queue[idx][0]
            ## TODO can fix this to be pointers instead cus this is wasteful
            if curr > 17 and curr - 17 not in self.walls and curr - 34 not in visited:
                queue.append((curr - 34, queue[idx][1]+1, queue[idx]))
            if curr < 17*16 and curr + 17 not in self.walls and curr + 34 not in visited:
                queue.append((curr + 34, queue[idx][1]+1, queue[idx]))
            if curr % 17 > 1 and curr - 1 not in self.walls and curr - 2 not in visited:
                queue.append((curr - 2, queue[idx][1]+1, queue[idx]))
            if curr % 17 < 16 and curr + 1 not in self.walls and curr + 2 not in visited:
                queue.append((curr + 2, queue[idx][1]+1, queue[idx]))
            idx += 1
        part = queue[idx]
        while part[2] is not None:
            if part[2][2] == None:
                return part[0]
            part = part[2]
        return part[0]

    def canWin(self):
        visited = set()
        one_done = False
        stack = []
        stack.append(self.locs[0])
        while (not one_done) and len(stack) != 0:
            curr = stack.pop()
            if curr >= 16*17:
                one_done = True
                break
            visited.add(curr)
            if curr > 17 and curr - 17 not in self.walls and curr - 34 not in visited:
                stack.append(curr - 34)
            if curr < 17*16 and curr + 17 not in self.walls and curr + 34 not in visited:
                stack.append(curr + 34)
            if curr % 17 > 1 and curr - 1 not in self.walls and curr - 2 not in visited:
                stack.append(curr - 2)
            if curr % 17 < 16 and curr + 1 not in self.walls and curr + 2 not in visited:
                stack.append(curr + 2)
        
        visited = set()
        two_done = False
        stack = []
        stack.append(self.locs[1])
        while (not two_done) and len(stack) != 0:
            curr = stack.pop()
            if curr < 17:
                two_done = True
                break
            visited.add(curr)
            if curr > 17 and curr - 17 not in self.walls and curr - 34 not in visited:
                stack.append(curr - 34)
            if curr < 17*16 and curr + 17 not in self.walls and curr + 34 not in visited:
                stack.append(curr + 34)
            if curr % 17 > 1 and curr - 1 not in self.walls and curr - 2 not in visited:
                stack.append(curr - 2)
            if curr % 17 < 16 and curr + 1 not in self.walls and curr + 2 not in visited:
                stack.append(curr + 2)
        return two_done and one_done

    def checkWon(self):
        if self.won:
            return
        if self.locs[0] >= 16*17:
            #print("red wins!")
            self.won = True
        if self.locs[1] < 17:
            #print("blue wins!")
            self.won = True

    def wall(self, k):
        if self.won:
            return -1
        if self.num_walls[self.turn] < 1:
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
                self.plays.append(self.canWin())
                if not self.canWin():
                    self.plays.pop()
                    self.walls.remove(k)
                    self.walls.remove(k + 1)
                    self.walls.remove(k + 2)
                    return -1
                self.num_walls[self.turn] -= 1
                self.turn = (self.turn ^ 1)
                return 1
        elif ((k % 17) % 2) and not (k//17 % 2):
            if ((k in self.walls) or ((k + 17) in self.walls) or ((k + 34) in self.walls)):
                #print("wall placement conflict")
                return -1
            else:
                self.walls.add(k)
                self.walls.add(k + 17)
                self.walls.add(k + 34)
                self.plays.append(self.canWin())
                if not self.canWin():
                    self.plays.pop()
                    self.walls.remove(k)
                    self.walls.remove(k + 17)
                    self.walls.remove(k + 34)
                    return -1
                self.num_walls[self.turn] -= 1
                self.turn = (self.turn ^ 1)
                return 1
        return -1

    def move_num(self, num):
        if self.won:
            return
        self.locs[self.turn] = num
        self.checkWon()
        self.turn = self.turn ^ 1


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
                if (self.locs[self.turn] + 68 < 17*17) and (self.locs[self.turn] + 51) not in self.walls:
                    self.locs[self.turn] += 68
                    self.checkWon()
                    self.turn = (self.turn ^ 1)
                    return 1
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
                if ((self.locs[self.turn]%17) + 4 < 17) and (self.locs[self.turn] + 3) not in self.walls:
                    self.locs[self.turn] += 4
                    self.checkWon()
                    self.turn = (self.turn ^ 1)
                    return 1
                elif (len(direction) > 1 and direction[1] == "w"):
                    if (self.locs[self.turn] - 34 < 0):
                        #print("out of bounds")
                        return -1
                    elif (self.locs[self.turn] -15) in self.walls:
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
                    elif (self.locs[self.turn] + 19) in self.walls:
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
                if (((self.locs[self.turn]) % 17) - 4 > 0) and (self.locs[self.turn] - 3) not in self.walls:
                    self.locs[self.turn] -= 4
                    self.checkWon()
                    self.turn = (self.turn ^ 1)
                    return 1
                elif (len(direction) > 1 and direction[1] == "w"):
                    if (self.locs[self.turn] - 34 < 0):
                        #print("out of bounds")
                        return -1
                    elif (self.locs[self.turn] - 19) in self.walls:
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
                    elif (self.locs[self.turn] + 15) in self.walls:
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
        boardstr = "*  1     2     3     4     5     6     7     8     9\n1 "
        for r in range(17):
            for c in range(17):
                if (r*17 + c) in self.walls:
                    if (r % 2 == 0):
                        boardstr += "\033[93m \u2016 \033[0m"
                    elif (c % 2 == 0):
                        boardstr += "\033[93m===\033[0m"
                    elif (c % 1 == 0):
                        boardstr += "\033[93m * \033[0m"
                elif (r*17 + c) == self.locs[0]:
                    boardstr += "\033[91m \u25C9 \033[0m"
                elif (r*17 + c) == self.locs[1]:
                    boardstr += "\033[96m \u25D9 \033[0m"
                else:
                    if (r % 2 == 0):
                        if (c % 2 == 1):
                            boardstr += " | "
                        else:
                            boardstr += "   "
                    else:
                        if (c % 2 == 1):
                            boardstr += "   "
                        else:
                            boardstr += "---"
            boardstr += "\n"
            if (r % 2 == 1):
                boardstr += str(r//2 + 2) + " "
            else:
                boardstr += "  "
        print(boardstr)

    def to_str(self):
        boardstr = "*  1     2     3     4     5     6     7     8     9\n1 "
        for r in range(17):
            for c in range(17):
                if (r*17 + c) in self.walls:
                    if (r % 2 == 0):
                        boardstr += "\033[93m \u2016 \033[0m"
                    elif (c % 2 == 0):
                        boardstr += "\033[93m===\033[0m"
                    elif (c % 1 == 0):
                        boardstr += "\033[93m * \033[0m"
                elif (r*17 + c) == self.locs[0]:
                    boardstr += "\033[91m \u25C9 \033[0m"
                elif (r*17 + c) == self.locs[1]:
                    boardstr += "\033[96m \u25D9 \033[0m"
                else:
                    if (r % 2 == 0):
                        if (c % 2 == 1):
                            boardstr += " | "
                        else:
                            boardstr += "   "
                    else:
                        if (c % 2 == 1):
                            boardstr += "   "
                        else:
                            boardstr += "---"
            boardstr += "\n"
            if (r % 2 == 1):
                boardstr += str(r//2 + 2) + " "
            else:
                boardstr += "  "
        return boardstr
        
    def play(self):
        self.printboard()
        while (not self.won):
            self.prompt()
    
    def prompt(self):
        players =["Red", "Blue"]
        choice = input(players[self.turn] + "'s turn, move or wall? (type move/wall or m/w)")
        if (choice == "m" or choice == "move"):
            choice = input("w/a/s/d?")
            self.move(choice)
            self.printboard()
        elif (choice == "w" or choice == "wall"):
            hv = input("horizontal or vertical (h/v)?")
            if (hv == "v"):
                r = input("which row is the top part of the wall at?")
                r = int(r)
                cr = input("which column is to the right of wall?")
                cr = int(cr)
                choice = (r - 1)*2*17 + (cr - 1)*2 - 1
                print(choice)
            else:
                c = input("which column is the left part of the wall at?")
                c = int(c)
                ra = input("which row is above the wall?")
                ra = int(ra)
                choice = (((ra -1)*2) + 1)*17 + (c - 1)*2

            self.wall(choice)
            self.printboard()


if __name__ == "__main__":
    board = Board()
    board.play()
