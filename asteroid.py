import circleshape, constants, pygame

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "green", (self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        # Update position based on velocity and time
        self.position += self.velocity * dt