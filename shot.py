import circleshape, constants, pygame, player

class Shot(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", (self.position.x, self.position.y), constants.SHOT_RADIUS, 2)
    
    def update(self, dt):
        super().update(dt) 
        self.rect.center = (self.position.x, self.position.y)
        self.position += self.velocity * dt 