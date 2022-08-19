import pygame

pygame.init()


# DEFINE CONSTANT PARAMETERS
WIDTH, HEIGHT = 540, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

win = pygame.display.set_mode((WIDTH, HEIGHT))
win.fill((WHITE))
pygame.display.set_caption("Sudoku Solver")

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


class Grid:

    def __init__(self, rows, cols, width, height, board):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height - (height - width)
        self.board = board

        self.cells = [[Cell(i, j, self.width, self.height, self.board[i][j]) for j in range(cols)] for i in range(rows)]
        
    def draw_grid(self):
        interval = self.width / self.rows

        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thickness = 4
            else:
                thickness = 1

            pygame.draw.line(win, BLACK, (0, i * interval), (self.width, i * interval), thickness)
            # vertical line
            pygame.draw.line(win, BLACK, (i * interval, 0), (i * interval, self.height), thickness)

            # draw in cell number (if non-zero)
            for i in range(self.rows):
                for j in range(self.cols):
                    self.cells[i][j].draw()

class Cell:
    def __init__(self, row, col, width, height, value):
        self.row = row
        self.col = col
        # values determined by the size of the board / 9 for each square
        self.width = width
        self.height = height
        self.value = value
        self.focused = False

    # draws cell based on width/height and position in board array
    def draw(self):
        font = pygame.font.SysFont("arial", 40)
        if (self.value == 0):
            return 
        # create "image" of non-zero values in the board
        cell_space = font.render(str(self.value), True, BLACK)
        # define position of number (with offset)
        interval = self.width / 9
        x_pos = (self.col * interval) + 20
        y_pos = (self.row * interval) + 10

        win.blit(cell_space, (x_pos, y_pos))




def main():
    grid = Grid(9, 9, WIDTH, HEIGHT, board)
    run = True
    while run:
        grid.draw_grid()
        for event in pygame.event.get():
            # exit on quit
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        pygame.display.update()


if __name__ == "__main__":
    main()
