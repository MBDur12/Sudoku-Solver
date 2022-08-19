import pygame

pygame.init()


# DEFINE CONSTANT PARAMETERS
WIDTH, HEIGHT= 540, 540
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Grid:
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
    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height    
        

    def draw_grid(self):
        interval  = self.width

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
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    win.fill((WHITE))
    pygame.display.set_caption("Sudoku Solver")

    run = True
    while run:
        for event in pygame.event.get():
            # exit on quit
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        

        pygame.display.update()

    

if __name__ == "__main__":
    main()