import pygame
import random
from circleshape import CircleShape
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        
        new_angle = random.uniform(20.0, 50.0)
        new_asteroid1_vector = self.velocity.rotate(new_angle)
        new_asteroid2_vector = self.velocity.rotate(-new_angle)
        NEW_RADIUS = self.radius - ASTEROID_MIN_RADIUS
        
        new_asteroid1 = Asteroid(self.position[0], self.position[1], NEW_RADIUS)
        new_asteroid1.velocity = new_asteroid1_vector * 1.2

        new_asteroid2 = Asteroid(self.position[0], self.position[1], NEW_RADIUS)
        new_asteroid2.velocity = new_asteroid2_vector * 1.2
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt