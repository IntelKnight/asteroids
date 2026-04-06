import pygame 
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SHOT_RADIUS
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from pewpew import Shot

print (f"Starting Asteroids with pygame version: {pygame.version.ver}")
print (f"Screen width: {SCREEN_WIDTH}")
print (f"Screen height: {SCREEN_HEIGHT}")

def main():
    # we initiate the pygame module 
    pygame.init()

    # make time a thing so we can control the fps
    clock = pygame.time.Clock()
    dt = 0

    # we create some groups to avoid making the main loop too clutered
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # we need to add the classes to their containers (group) before we make an instance of em
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    AsteroidField1 = AsteroidField()
   
    while True:
        # this is just for the class
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for object in drawable:
            object.draw(screen)

        clock.tick(60)
        dt = clock.tick(60)/1000

        updatable.update(dt)

        for asteroid in asteroids:
            if player1.collide_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shots:
                if shot.collide_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()


        # call this line last no matter what (it renders the screen)
        pygame.display.flip()

main()