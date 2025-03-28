import circleshape, constants, pygame, random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius, velocity = None):
        super().__init__(x, y, radius)
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        if velocity is not None:
            self.velocity = velocity
    def draw(self, screen):
        pygame.draw.circle(screen, "green", (self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        super().update(dt)
        self.rect.center = (self.position.x, self.position.y)
        # Update position based on velocity and time
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(
            self.position.x,
            self.position.y,
            radius = new_radius,
            velocity = new_velocity1 * 1.2)
        new_asteroid_2 = Asteroid(
            self.position.x,
            self.position.y,
            radius = new_radius,
            velocity = new_velocity2 * 1.2)