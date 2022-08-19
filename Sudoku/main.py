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

class Cell:
    def __init__(self, row, col, width, height, value, window):
        self.row = row
        self.col = col
        # values determined by the size of the board / 9 for each square
        self.width = width
        self.height = height
        self.value = value

    # draws cell based on width/height and position in board array
    def draw(self):
        pass


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
