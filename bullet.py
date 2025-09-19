from constants import *
from player import *
from circleshape import *
from asteroid import *


class Bullet(CircleShape):
    def __init__(self, x, y, radius, player_rotation):
        super().__init__(x, y, radius)
        self.rotation = player_rotation
    
    
    def draw(self, screen):
        pygame.draw.circle(screen, "#FFFFFF", self.position, self.radius)
    
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * BULLET_SPEED * dt
        
    
    def update(self, dt):
        self.move(dt)
        self.position += self.velocity * dt