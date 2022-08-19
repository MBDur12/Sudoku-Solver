board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


# prints out current state of the board
def print_board(board):
    for i in range(len(board)):
        # prints horizontal bar at the start of each 3x3 square
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - ")
        for j in range(len(board[i])):
            # prints vertical line at the boundary of each 3x3 square
            if j % 3 == 0 and j != 0:
                print("|", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
            
# finds first empty square in board and returns tuple (x, y)
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i , j)

    return None

print(find_empty(board))
