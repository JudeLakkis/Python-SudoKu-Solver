class Sudoku():
    def __init__(self):
        # Read in the puzzle
        with open('puzzle.txt', 'r') as f:
            self.board = [[int(j) for j in i.strip()] for i in f.readlines()]

    def display(self):
        [print(i) for i in self.board]

# Main 
puzzle = Sudoku()
puzzle.display()

