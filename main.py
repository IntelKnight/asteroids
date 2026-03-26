import pygame 
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
print (f"Starting Asteroids with pygame version: {pygame.version.ver}")
print (f"Screen width: {SCREEN_WIDTH}")
print (f"Screen height: {SCREEN_HEIGHT}")
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def main():
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        # call this line last no matter what
        pygame.display.flip()

main()