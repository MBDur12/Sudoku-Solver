from pickle import TRUE
from tkinter.tix import CELL
import pygame

pygame.init()


# DEFINE CONSTANT PARAMETERS
WIDTH, HEIGHT = 540, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

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
        self.focused_cell = None

    def get_coords_from_mouse_position(self, position):
        row, col = int(position[1] / 60), int(position[0] / 60)
        return (row, col)

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
    # returns true if click occurs within the grid
    def is_valid_position(self, mouse_pos):
        if mouse_pos[0] < self.width and mouse_pos[1] < self.height:
            return True
        return False

    def handleClick(self, mouse_pos):
        # translates mouse position to corresponding cell indices
        row, col = self.get_coords_from_mouse_position(mouse_pos)
        if self.focused_cell:
            self.focused_cell.remove_focus()

        self.focused_cell = self.cells[row][col]
        self.focused_cell.set_focus()

class Cell:
    def __init__(self, row, col, width, height, value):
        self.row = row
        self.col = col
        # values determined by the size of the board / 9 for each square
        self.width = width
        self.height = height
        self.value = value
        self.focused = False

    def remove_focus(self):
        self.focused = False
    def set_focus(self):
        self.focused = True
    # draws cell based on width/height and position in board array
    def draw(self):
        font = pygame.font.SysFont("arial", 40)
        if (self.value == 0):
            cell_space = font.render("", True, BLACK)
        else:
            # create "image" of non-zero values in the board
            cell_space = font.render(str(self.value), True, BLACK)
        # define position of number (with offset)
        interval = self.width / 9
        x_pos = (self.col * interval) + 20
        y_pos = (self.row * interval) + 10

        if self.focused:
            highlighted_sq = pygame.Rect(self.col*60, self.row*60, 60, 60)
            pygame.draw.rect(win, RED, highlighted_sq, 2)

        win.blit(cell_space, (x_pos, y_pos))



def redraw_window(win, grid):
    win.fill(WHITE)
    grid.draw_grid()

def main():
    grid = Grid(9, 9, WIDTH, HEIGHT, board)
    run = True
    while run:
        for event in pygame.event.get():
            # exit on quit
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if grid.is_valid_position(position):
                    key = None
                    grid.handleClick(position)
        
        # 
            
        
        
            

        redraw_window(win, grid)
        pygame.display.update()


if __name__ == "__main__":
    main()
