# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *
from asteroids import *
from asteroidfield import *
from shots import Shot

def main():
    # Initialize pygame
    pygame.init()
    
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # FPS control
    clock = pygame.time.Clock()
    dt = 0

    # Groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    Shot.containers = (shots, updatables, drawables)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatables.update(dt)

        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                return
            for shot in shots:
                if shot.check_collision(asteroid):
                    asteroid.kill()

           
        screen.fill(color="black")

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        # Loop FPS control
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
