import circleshape, constants, pygame

class Shot(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", (self.position.x, self.position.y), constants.SHOT_RADIUS, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        print(f"Shot position: {self.position}, velocity: {self.velocity}, delta_time: {dt}")   