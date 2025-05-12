locs = [0*17 + 8, 16*17 + 8]
num_walls = [10, 10]
walls = set();
turn = 0;

def wall(k):
    global turn
    if ((k % 17) > 15) or (k > 17*16):
        return "wall placement out of bounds"
    if (k//17 % 2) and  not ((k % 17) % 2):
        if ((k in walls) or ((k + 1) in walls) or ((k + 2) in walls)):
            return "wall placement conflict"
        else:
            walls.add(k)
            walls.add(k + 1)
            walls.add(k + 2)
            num_walls[turn] -= 1
            turn = (turn ^ 1)
    elif ((k % 17) % 2):
        if ((k in walls) or ((k + 17) in walls) or ((k + 34) in walls)):
            return "wall placement conflict"
        else:
            walls.add(k)
            walls.add(k + 17)
            walls.add(k + 34)
            num_walls[turn] -= 1
            turn = (turn ^ 1)
    return "uknown error"

def move(direction):
    global turn
    if (direction[0] == "w"):
        if (locs[turn] - 34 < 0):
            return "out of bounds"
        elif (locs[turn] - 17) in walls:
            return "wall in the way"
        ##CODE FOR HANDLING JUMP RULE
        elif (locs[turn] - 34 == locs[turn^1]):
            if (locs[turn] - 68 > 0) and (locs[turn] - 51) not in walls:
                locs[turn] -= 68
                turn = (turn ^ 1)
                return
            elif (len(direction) > 1 and direction[1] == "d"):
                if (locs[turn] % 17 > 15):
                    return "out of bounds"
                elif (locs[turn] - 33) in walls:
                    return "wall in the way"
                else: 
                    locs[turn] -= 32
                    turn = (turn ^ 1)
            elif (len(direction) > 1 and direction[1] == "a"):
                if (locs[turn] % 17 < 2):
                    return "out of bounds"
                elif (locs[turn] - 35) in walls:
                    return "wall in the way"
                else: 
                    locs[turn] -= 36
                    turn = (turn ^ 1)
                    return
        ##END CODE FOR HANDLING JUMP RULE
        else: 
            locs[turn] -= 34
            turn = (turn ^ 1)
            return
    if (direction[0] == "s"):
        if (locs[turn] + 34 >= 17*17):
            return "out of bounds"
        elif (locs[turn] + 17) in walls:
            return "wall in the way"
        ##CODE FOR HANDLING JUMP RULE
        elif (locs[turn] + 34 == locs[turn^1]):
            if (locs[turn] + 68 > 0) and (locs[turn] + 51) not in walls:
                locs[turn] += 68
                turn = (turn ^ 1)
                return
            elif (len(direction) > 1 and direction[1] == "d"):
                if (locs[turn] % 17 > 15):
                    return "out of bounds"
                elif (locs[turn] + 35) in walls:
                    return "wall in the way"
                else: 
                    locs[turn] += 36
                    turn = (turn ^ 1)
            elif (len(direction) > 1 and direction[1] == "a"):
                if (locs[turn] % 17 < 2):
                    return "out of bounds"
                elif (locs[turn] + 33) in walls:
                    return "wall in the way"
                else: 
                    locs[turn] += 32
                    turn = (turn ^ 1)
                    return
        ##END CODE FOR HANDLING JUMP RULE
        else: 
            locs[turn] += 34
            turn = (turn ^ 1)
            return
    if (direction[0] == "d"):
        if (locs[turn] % 17 > 15):
            return "out of bounds"
        elif (locs[turn] + 1) in walls:
            return "wall in the way"
        ##CODE FOR HANDLING JUMP RULE
        elif (locs[turn] + 2 == locs[turn^1]):
            if (locs[turn] + 4 > 0) and (locs[turn] + 3) not in walls:
                locs[turn] += 4
                turn = (turn ^ 1)
                return
            elif (len(direction) > 1 and direction[1] == "w"):
                if (locs[turn] - 34 < 0):
                    return "out of bounds"
                elif (locs[turn] -33) in walls:
                    return "wall in the way"
                else: 
                    locs[turn] -= 32
                    turn = (turn ^ 1)
            elif (len(direction) > 1 and direction[1] == "s"):
                if (locs[turn] + 34 >= 17*17):
                    return "out of bounds"
                elif (locs[turn] + 35) in walls:
                    return "wall in the way"
                else: 
                    locs[turn] += 36
                    turn = (turn ^ 1)
                    return
        ##END CODE FOR HANDLING JUMP RULE
        else: 
            locs[turn] += 2
            turn = (turn ^ 1)
            return
    if (direction[0] == "a"):
        if (locs[turn] % 17 < 2):
            return "out of bounds"
        elif (locs[turn] - 1) in walls:
            return "wall in the way"
        ##CODE FOR HANDLING JUMP RULE
        elif (locs[turn] - 2 == locs[turn^1]):
            if (locs[turn] - 4 > 0) and (locs[turn] - 3) not in walls:
                locs[turn] -= 4
                turn = (turn ^ 1)
                return
            elif (len(direction) > 1 and direction[1] == "w"):
                if (locs[turn] - 34 < 0):
                    return "out of bounds"
                elif (locs[turn] - 35) in walls:
                    return "wall in the way"
                else: 
                    locs[turn] -= 36
                    turn = (turn ^ 1)
            elif (len(direction) > 1 and direction[1] == "s"):
                if (locs[turn] + 34 >= 17*17):
                    return "out of bounds"
                elif (locs[turn] + 33) in walls:
                    return "wall in the way"
                else: 
                    locs[turn] += 32
                    turn = (turn ^ 1)
                    return
        ##END CODE FOR HANDLING JUMP RULE
        else: 
            locs[turn] -= 2
            turn = (turn ^ 1)
            return
    return "invalid direction"

def printboard():
    boardstr = ""
    for r in range(17):
        for c in range(17):
            if (r*17 + c) in walls:
                boardstr += "\033[93m\u25A0\033[0m "
            elif (r*17 + c) == locs[0]:
                boardstr += "\033[91m\u25C9\033[0m "
            elif (r*17 + c) == locs[1]:
                boardstr += "\033[96m\u25D9\033[0m "
            else:
                boardstr += "\u25A0 "
        boardstr += "\n"
    print(boardstr)

while (True):
    choice = input("Player " + str(turn + 1) + "'s turn, move or wall? (type move/wall or m/w)")
    if (choice == "m" or choice == "move"):
        choice = input("w/a/s/d?")
        move(choice)
        printboard()
    elif (choice == "w" or choice == "wall"):
        choice = input("where would you like to place the wall?")
        choice = int(choice)
        wall(choice)
        printboard()
