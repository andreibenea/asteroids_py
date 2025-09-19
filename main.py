import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
updatables = pygame.sprite.Group()
drawables = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
bullets = pygame.sprite.Group()

Player.containers = (updatables, drawables)
Asteroid.containers = (asteroids, updatables, drawables)
AsteroidField.containers = updatables
Bullet.containers = (bullets, updatables, drawables)


def main():
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    pygame.init()
    clock = pygame.time.Clock()
    player = Player(x, y)
    asteroid_field = AsteroidField()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color="#000000")
        for drawable in drawables:
            drawable.draw(screen)
        updatables.update(dt)
        for asteroid in asteroids:
            for bullet in bullets:
                if bullet.colliding(asteroid):
                    asteroid.split()
                    bullet.kill()
                    print("HIT!")
            if asteroid.colliding(player):
                raise SystemExit("Game Over!")
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
