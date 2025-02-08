import pygame
from constants import *
from player import Player # Don't need to import Circle Shape here since Player imports it already.

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets a screen object

    clock = pygame.time.Clock() # Sets a clock object
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # sets a player object from Player class


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt) ## update the players movement and rotation with a delay of dt ms

        screen.fill("black")

        for obj in drawable: # for every object that is in the drawable group, it draws it on the screen
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000 ## sets a delta variable at 60ms
        
        
            














if __name__ == "__main__":
    main()