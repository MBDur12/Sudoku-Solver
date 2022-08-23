import pygame
from backtracking import is_valid, solve_board

pygame.font.init()


# DEFINE CONSTANT PARAMETERS
WIDTH, HEIGHT = 540, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)

GAMEOVER_FONT = pygame.font.SysFont("arial", 80)


win = pygame.display.set_mode((WIDTH, HEIGHT))
win.fill((WHITE))
pygame.display.set_caption("Sudoku Solver")

INCREMENT_TIMER = pygame.USEREVENT + 1
GAME_OVER = pygame.USEREVENT + 2

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
        self.can_user_click = True

        self.cells = [[Cell(i, j, self.width, self.height, self.board[i][j]) for j in range(cols)] for i in range(rows)]
        self.focused_cell = None

    def update_board(self, pos, val):
        self.board[pos[0]][pos[1]] = val

    def clear_focused_cell(self):
        if self.focused_cell and self.focused_cell.editable:
            self.focused_cell.set_temp_value(0)
            self.focused_cell.set_value(0)
            self.update_board(
                (self.focused_cell.row, self.focused_cell.col)
                ,0
                )
                  
                    

    def get_coords_from_mouse_position(self, position):
        row, col = int(position[1] / 60), int(position[0] / 60)
        return (row, col)

    def draw_grid(self, win):
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
                    self.cells[i][j].draw(win)
    # returns true if mouse position on click occurs within the grid
    def is_valid_position(self, mouse_pos):
        if mouse_pos[0] < self.width and mouse_pos[1] < self.height:
            return True
        return False

    def handleClick(self, mouse_pos):
        if self.can_user_click:
            # translates mouse position to corresponding cell indices
            row, col = self.get_coords_from_mouse_position(mouse_pos)
            # removes focus from currently focused cell
            if self.focused_cell:
                self.focused_cell.remove_focus()

            self.focused_cell = self.cells[row][col]
            self.focused_cell.set_focus()

    def draw_note(self, key_val):
        self.focused_cell.set_temp_value(key_val)

    
    def place_num(self):
        row = self.focused_cell.row
        col = self.focused_cell.col
        val = self.focused_cell.temp_value
        self.update_board((row, col), val)
        if is_valid(self.board, (row,col), val) and solve_board(self.board):
            print(self.board)
            self.focused_cell.set_value(val)         
            return True

        self.update_board((row, col), 0)
        self.clear_focused_cell()
        return False
    
    def is_filled(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cells[i][j].value == 0:
                    return False
        return True
    
    
    def solve_grid(self):
        solve_board(self.board)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cells[i][j].value == 0:
                    self.cells[i][j].set_value(self.board[i][j])
                print(self.cells[i][j].value)
        self.stop_clicks()

    def stop_clicks(self):
        self.can_user_click = False
        



class Cell:
    def __init__(self, row, col, width, height, value):
        self.row = row
        self.col = col
        # initial cell values on board creation should not be edited
        self.editable = False if value > 0 else True
        self.width = width
        self.height = height
        self.value = value
        self.temp_value = 0
        self.focused = False

    def remove_focus(self):
        self.focused = False
    def set_focus(self):
        self.focused = True

    def set_temp_value(self, val):
        self.temp_value = val
    def set_value(self, val):
        self.value = val

    # draws cell based on width/height and position in board array
    def draw(self, win):
        # define position of number (with offset)
        interval = self.width / 9
        x_pos = (self.col * interval) + 20
        y_pos = (self.row * interval) + 10
        

        # TODO: remove duplication: what idea are you trying to capture?
        if self.temp_value != 0 and self.value == 0:
            font = pygame.font.SysFont("arial", 15)
            cell_value = font.render(str(self.temp_value), True, GREY)
            win.blit(cell_value, (x_pos, y_pos))
        elif self.value != 0: 
            font = pygame.font.SysFont("arial", 40) 
            cell_value = font.render(str(self.value), True, BLACK,)
            win.blit(cell_value, (x_pos, y_pos))
            
        
        if self.focused:
            highlighted_sq = pygame.Rect(self.col*60, self.row*60, 60, 60)
            pygame.draw.rect(win, RED, highlighted_sq, 3)

        
def get_formatted_time(time):
    mins = time // 60
    secs = time % 60
    return f"{mins:02d}:{secs:02d}"

def display_game_over(win, text):
    game_over_text = GAMEOVER_FONT.render(text, True, BLACK)

    win.blit(game_over_text, 
        (WIDTH//2 - game_over_text.get_width()//2, 
        HEIGHT//2 - game_over_text.get_height()//2))
    
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.event.post(pygame.event.Event(GAME_OVER))

  
    
def redraw_window(win, grid, time, strikes):
    font = pygame.font.SysFont("arial", 30)
    timer_text = font.render("Time: "+ get_formatted_time(time), True, BLACK)
    strikes_text = font.render("X" * strikes, True, RED)

    win.fill(WHITE)
    grid.draw_grid(win)
    win.blit(timer_text, (10, HEIGHT - 50))
    win.blit(strikes_text, (WIDTH // 2, HEIGHT - 50))



def main():
    grid = Grid(9, 9, WIDTH, HEIGHT, board)
    pygame.time.set_timer(INCREMENT_TIMER, 1000)
    time = 0
    strikes = 0
    run = True
    while run:
        for event in pygame.event.get():
            # exit on quit
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == GAME_OVER:
                display_game_over()
                main()

            if event.type == INCREMENT_TIMER:
                time += 1
            
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

                if event.key == pygame.K_RETURN:
                    if grid.focused_cell:
                        if grid.place_num():
                            print("success")
                        else:
                            strikes += 1
                        key == None
                        
                        if strikes == 3:
                            display_game_over(win, "You Lost")
                        elif grid.is_filled():
                            display_game_over(win, "You Won")
                        

                if event.key == pygame.K_CLEAR or event.key == pygame.K_DELETE:
                    grid.clear_focused_cell()

                if event.key == pygame.K_SPACE:
                    grid.solve_grid()

               
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if grid.is_valid_position(position):
                    key = None
                    grid.handleClick(position)
        
        # Note down temporary value for focused cell
        if grid.focused_cell and key != None:
            grid.draw_note(key)
            
        
        
            

        redraw_window(win, grid, time, strikes)
        pygame.display.update()
        


if __name__ == "__main__":
    main()
