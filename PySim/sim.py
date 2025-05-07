def from_rc(r, c):
    return r*11 + c

## Initialize board
board = []
for i in range(11*11):
    board.append([])
for i in range(11*11):
    board[i].append(0)

## set values so that the board is properly connected
for r in range(11):
    for c in range(11):
        if (r < 10):
            board[from_rc(r, c)][from_rc(r+1, c)] = 
