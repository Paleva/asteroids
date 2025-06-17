import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide(shot):
                    shot.kill()
                    asteroid.split()
                    break
            if not asteroid.collide(player):
                continue
            player.kill()
        
            print("Game Over!")
            sys.exit(0)

        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()