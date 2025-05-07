locs = [0*17 + 8, 16*17 + 8]
num_walls = (10, 10)
walls = set();
turn = 0;

def wall(k):
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
    if (direction == "w"):
        if (locs[turn] - 34 < 0):
            return "out of bounds"
        elif (locs_turn - 17) in walls:
            return "wall in the way"
        else: 
            locs[turn] -= 34
            turn = (turn ^ 1)
            return
    if (direction == "s"):
        if (locs[turn] + 34 >= 17*17):
            return "out of bounds"
        elif (locs_turn + 17) in walls:
            return "wall in the way"
        else: 
            locs[turn] += 34
            turn = (turn ^ 1)
            return
    if (direction == "d"):
        if (locs[turn] % 17 > 15):
            return "out of bounds"
        elif (locs_turn + 1) in walls:
            return "wall in the way"
        else: 
            locs[turn] += 2
            turn = (turn ^ 1)
            return
    if (direction == "a"):
        if (locs[turn] % 17 < 2):
            return "out of bounds"
        elif (locs_turn - 1) in walls:
            return "wall in the way"
        else: 
            locs[turn] -= 2
            turn = (turn ^ 1)
            return
    return "invalid direction"


