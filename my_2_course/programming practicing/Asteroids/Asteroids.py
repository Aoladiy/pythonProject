import pygame
import random

pygame.init()

# Определение констант
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
ASTEROID_SPEED = 3

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroids")

background_image = pygame.transform.scale(pygame.image.load("background.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
player_image = pygame.transform.scale(pygame.image.load("ship.png").convert_alpha(), (64, 64))
bullet_image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("bullet.png").convert_alpha(), (64, 24)), 90)
asteroid_images = [
    pygame.transform.scale(pygame.image.load("asteroid0.png").convert_alpha(), (64, 64)),
    # pygame.transform.scale(pygame.image.load("asteroid2.png").convert_alpha(), (64, 64)),
    # pygame.transform.scale(pygame.image.load("asteroid3.png").convert_alpha(), (64, 64)),
]

all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
asteroid_group = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        # if keys[pygame.K_LEFT] and self.rect.left > 0:
        #     pygame.transform.rotate(self.image, 270)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(random.choice(asteroid_images), (random.randint(30, 45), random.randint(30, 45)))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, abs(SCREEN_WIDTH - self.rect.width))
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(ASTEROID_SPEED - 2, ASTEROID_SPEED)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


player = Player()
all_sprites.add(player)
player_group.add(player)

clock = pygame.time.Clock()
running = True
while running:
    if random.randint(0, 100) in range(2):
        asteroid = Asteroid()
        all_sprites.add(asteroid)
        asteroid_group.add(asteroid)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullet_group.add(bullet)
    keys = pygame.key.get_pressed()

    player.update(keys)

    bullet_group.update()

    asteroid_group.update()

    hits = pygame.sprite.groupcollide(bullet_group, asteroid_group, True, True)
    for hit in hits:
        asteroid = Asteroid()
        all_sprites.add(asteroid)
        asteroid_group.add(asteroid)

    hits = pygame.sprite.spritecollide(player, asteroid_group, True)
    if hits:
        running = False

    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

# Завершение Pygame
pygame.quit()
