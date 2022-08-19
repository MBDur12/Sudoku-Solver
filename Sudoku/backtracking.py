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

# uses backtracking to solve the given board
def solve_board(board):
    #  basecase - no empty square found
    pos = find_empty(board)
    if pos == None:
        return True
    else:
        row, col = pos

    # iterates across value range
    for num in range(1, 10):
        # apply value if it satisfies constraints
        if  is_valid(board, (row, col), num):
            board[row][col] = num
            # recurse on that (currently) valid decision
            if solve_board(board):
                return True
            # otherwise, backtrack from that decision
            board[row][col] = 0
        
    return False

    


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


# checks if a number can be validly placed in a given cell
def is_valid(board, coords, num):
    # checks inclusion along target row (x coord)
    if num in board[coords[0]]:
        return False
    # checks if value is already in target column
    for i in range(len(board)):
        if board[i][coords[1]] == num:
            return False

    # checks inclusion in 3x3 square
    square_x = coords[0] // 3
    square_y = coords[1] // 3

    for i in range(square_x * 3, square_x * 3 + 3):
        for j in range(square_y * 3, square_y * 3 + 3):
            if board[i][j] == num:
                return False

    return True



