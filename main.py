# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # create two groups
    updatable = pygame.sprite.Group() # all objects that can be updated
    drawable = pygame.sprite.Group() # all objects that can be drawn
    Player.containers = (updatable, drawable)

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # limit the framerate to 60 fps
        dt = clock.tick(60) / 1000

        # update all objects in updatable with fresh dt
        updatable.update(dt)

        # draw everything
        screen.fill((0,0,0))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        

if __name__ == "__main__":
    main()