import math
import random

import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
ASTEROID_SPEED = 3
LIVES = 3

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroids")

background_image = pygame.transform.scale(pygame.image.load("background.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
player_image = pygame.transform.scale(pygame.image.load("ship.png").convert_alpha(), (64, 64))
bullet_image = pygame.transform.rotate(
    pygame.transform.scale(pygame.image.load("bullet.png").convert_alpha(), (64, 24)), 90)
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
        self.original_image = player_image
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 5
        self.angle = 0

    def update(self, keys):
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.rect.left > 0:
            self.rect.x -= self.speed
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and self.rect.top > 0:
            self.rect.y -= self.speed
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed
        if keys[pygame.K_q] or keys[pygame.K_x]:
            self.angle += 5
            self.image = pygame.transform.rotate(self.original_image, self.angle)
        if keys[pygame.K_e] or keys[pygame.K_c]:
            self.angle -= 5
            self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.original_image = bullet_image
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y + 85
        self.speed = 10
        self.angle = angle

    def update(self):
        self.rect.x -= self.speed * math.sin(math.radians(self.angle))
        self.rect.y -= self.speed * math.cos(math.radians(self.angle))
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        if self.rect.bottom < 0:
            self.kill()


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(random.choice(asteroid_images),
                                            (random.randint(30, 45), random.randint(30, 45)))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        self.speed = random.randint(1, 4)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
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
                bullet = Bullet(player.rect.centerx, player.rect.top, player.angle)
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
        LIVES -= 1
        if LIVES <= 0:
            running = False

    screen.blit(background_image, (0, 0))

    font = pygame.font.Font(None, 36)

    text = font.render(f"Lives: {LIVES}", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.topright = (SCREEN_WIDTH - 10, 10)

    screen.blit(text, text_rect)

    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
