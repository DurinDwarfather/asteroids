import circleshape, constants, pygame, shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        PLAYER_SHOOT_SPEED = constants.PLAYER_SHOOT_SPEED
        
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            #print("A key has been pressed!")
            self.rotate(-dt) # nagative (counter clockwise) rotation
        if keys[pygame.K_d]:
            #print("D key has been pressed!")
            self.rotate(dt) # positive (clockwise) rotation
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def shoot(self):
        new_shot = shot.Shot(self.position.x, self.position.y, constants.SHOT_RADIUS)
        shot_direction = pygame.Vector2(0, 1)
        shot_direction = shot_direction.rotate(self.rotation)
        shot_direction = shot_direction * constants.PLAYER_SHOOT_SPEED
        new_shot.velocity = shot_direction
        