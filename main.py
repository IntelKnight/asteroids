import pygame 
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

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

    # we need to add the class to it's container (group) before we make an instance of it
    Player.containers = (updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
   
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

        # call this line last no matter what (it renders the screen)
        pygame.display.flip()

main()