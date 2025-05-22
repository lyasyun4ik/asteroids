# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # create groups
    updatable = pygame.sprite.Group() # all objects that can be updated
    drawable = pygame.sprite.Group() # all objects that can be drawn
    asteroids = pygame.sprite.Group() # all asteroids
    shots = pygame.sprite.Group() # all shots

    # assign objects to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # limit the framerate to 60 fps
        dt = clock.tick(60) / 1000

        # update all objects in updatable with fresh dt
        updatable.update(dt)

        # check for collisions
        for asteroid in asteroids:
            if asteroid.collision(player):
                sys.exit("Game over!")

        # draw everything
        screen.fill((0,0,0))
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        

if __name__ == "__main__":
    main()