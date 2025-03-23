# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, constants, circleshape, player, asteroid, asteroidfield

#defines object grouping
updatable = pygame.sprite.Group()
drawables = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

#defines group membership
player.Player.containers = (updatable, drawables)
asteroidfield.AsteroidField.containers = (updatable,)
asteroid.Asteroid.containers = (asteroids, updatable, drawables)

game_on = True #creates the run condition for the while loop.
dt = 0 # creates the detla time variable to be used elseware. 
refresh_rate = 60 # sets the game clock refresh rate 
clock = pygame.time.Clock() #the game clock

#define objects that will appear on the screen
screen_width = constants.SCREEN_WIDTH
screen_height = constants.SCREEN_HEIGHT
screen = pygame.display.set_mode((screen_width, screen_height))
x = constants.SCREEN_WIDTH / 2
y = constants.SCREEN_HEIGHT / 2
player_object = player.Player(x, y)
asteroid_object = asteroidfield.AsteroidField()

def game_loop():
    global dt
    while game_on == True:
        dt = clock.tick(60) / 1000.0 # convert miliseconds to seconds

        screen.fill("black") # fills screen with black background
        for draw in drawables:
            draw.draw(screen) # draws the player on the background
        updatable.update(dt) # allows the player to rorate left and right
        
        for asteroid in asteroids:
            if player_object.collision_check(asteroid):
                print("Game over!")
                import sys
                sys.exit() # Ends the game
        
        pygame.display.flip() # refreshes the game screen

        for event in pygame.event.get(): # In the event pygame.event.get is called
            if event.type == pygame.QUIT: # and the event.type is pygame.quit - quit the game
                return


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {screen_width}")
    print(f"Screen height: {screen_height}")
    # Initiate game loop``
    pygame.init()
    game_loop()
        
    



if __name__ == "__main__":
    main()