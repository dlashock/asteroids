import pygame
import random
from circleshape import *
from player import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            (255, 255, 255),
            self.position, 
            self.radius,
            2
        )
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        dir1 = self.position.rotate(angle)
        dir2 = self.position.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(
            self.position[0], 
            self.position[1], 
            new_radius)
        asteroid2 = Asteroid(
            self.position[0], 
            self.position[1], 
            new_radius)
        
        asteroid1.velocity = dir1 * 1.2
        asteroid2.velocity = dir2 * 1.2