import sys
import pygame
from constants import *
from player import *
from circleshape import *
from asteroidfield import *
from asteroid import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_HEIGHT/2, SCREEN_WIDTH/2)

    Asteroid.containers=(asteroids,updatable,drawable)

    AsteroidField.containers=(updatable)

    asteroidField = AsteroidField()

    Shot.containers = (shots,drawable,updatable)


    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for tmp in updatable:
            tmp.update(dt)

        for tmp in asteroids:
            if tmp.check_collision(player):
                sys.exit("Game over!")
            for bullet in shots:
                if tmp.check_collision(bullet):
                    tmp.split()
                    bullet.kill()

        screen.fill("black")

        for tmp in drawable:
            tmp.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
