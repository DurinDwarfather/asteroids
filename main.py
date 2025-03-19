# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, constants
screen_width = constants.SCREEN_WIDTH
screen_height = constants.SCREEN_HEIGHT
game_on = True
dt = 0
refresh_rate = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
def game_loop():
    while game_on == True:
        pygame.display.flip() # builds the game screen

        for event in pygame.event.get(): # In the event pygame.event.get is called
            if event.type == pygame.QUIT: # and the event.type is pygame.quit - quit the game
                return

        clock.tick(60)


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {screen_width}")
    print(f"Screen height: {screen_height}")
    pygame.init()
    clock
    game_loop()
        
    



if __name__ == "__main__":
    main()