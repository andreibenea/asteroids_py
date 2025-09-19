import random

from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    
    def draw(self, screen):
        pygame.draw.circle(screen, "#FFFFFF", self.position, self.radius)
    
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            old_radius = self.radius
            random_angle = random.uniform(20, 50)
            asteroid_one = Asteroid(self.position[0], self.position[1], old_radius - ASTEROID_MIN_RADIUS)
            asteroid_two = Asteroid(self.position[0], self.position[1], old_radius - ASTEROID_MIN_RADIUS)
            asteroid_one.velocity = (self.velocity.rotate(random_angle)) * 1.2
            asteroid_two.velocity = (self.velocity.rotate(-random_angle)) * 1.2
            self.kill()
            
        
    
    def update(self, dt):
        self.position += self.velocity * dt