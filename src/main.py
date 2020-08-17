# Load Puzzle
with open('puzzle.txt', 'r') as f:
    board = [[int(j) for j in i.strip()] for i in f.readlines()]


def print_board(board):
    # Deals with each row
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print('-----------------------')
        # Deals with number placement and seperation
        for num in range(len(board[0])):
            if num % 3 == 0 and num != 0:
                print(" | ", end="")
            if num == 8:
                print(board[row][num])
            else:
                print(str(board[row][num]) + " ", end="")

def solve(board):
    find = empty(board)
    if not find:
        # If there isn't any blanks to find, the board is solved
        return True
    row, col = find

    for i in range(1,10):
        # Fill in 1 - 9 in the current blank space
        if valid(board, i, (row, col)):
            board[row][col] = i
            # If the board is solved exit
            if solve(board):
                return True
            # Return space back to 0
            board[row][col] = 0

    return False

def valid(board, num, pos):
    # Check each row for any matches
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check each column for any matches
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

def empty(board):
    # Looks for any space in the board matrix which has a 0, denoting empty space
    for row in range(len(board)):
        for num in range(len(board[0])):
            if board[row][num] == 0:
                # Return coordinates of the most recent blank
                return (row, num)
    return None # Escape loop when board solved


# Main
print_board(board)
solve(board)
print('')
print_board(board)

# Test Puzzle
'''
780400120
600075009
000601078
007040260
001050930
904060005
070300012
120007400
049206007
'''
