import pygame
from constants import *
from player import Player # Don't need to import Circle Shape here since Player imports it already.
from asteroidfield import AsteroidField 
from asteroid import Asteroid

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets a screen object

    clock = pygame.time.Clock() # Sets a clock object
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # sets a player object from Player class

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable 
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt) ## update the players movement and rotation with a delay of dt ms

        screen.fill("black")

        for obj in drawable: # for every object that is in the drawable group, it draws it on the screen
            
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000 ## sets a delta variable at 60ms
        
        
            














if __name__ == "__main__":
    main()