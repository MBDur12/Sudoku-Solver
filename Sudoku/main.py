import pygame

pygame.init()

# DEFINE CONSTANT PARAMETERS
WIDTH, HEIGHT= 600, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)




def main():
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku Solver")

    run = True
    while run:
        for event in pygame.event.get():
            print(event)
            # exit on quit
            if event.type == pygame.QUIT:
                print("wanting to exit")
                run = False
                pygame.quit()

    

if __name__ == "__main__":
    main()