# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, constants, circleshape
import player
screen_width = constants.SCREEN_WIDTH
screen_height = constants.SCREEN_HEIGHT
game_on = True
dt = 0
refresh_rate = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
x = constants.SCREEN_WIDTH / 2
y = constants.SCREEN_HEIGHT / 2
player_object = player.Player(x, y)


def game_loop():
    global dt
    while game_on == True:
        dt = clock.tick(60) / 1000.0 # convert miliseconds to seconds
        
        screen.fill("black") # fills screen with black background
        player_object.draw(screen) # draws the player on the background
        player_object.update(dt) # allows the player to rorate left and right
        pygame.display.flip() # refreshes the game screen

        for event in pygame.event.get(): # In the event pygame.event.get is called
            if event.type == pygame.QUIT: # and the event.type is pygame.quit - quit the game
                return


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {screen_width}")
    print(f"Screen height: {screen_height}")
    # Initiate game loop
    pygame.init()
    game_loop()
        
    



if __name__ == "__main__":
    main()