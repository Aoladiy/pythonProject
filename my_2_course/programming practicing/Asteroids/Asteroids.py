import math
import random

import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
ASTEROID_SPEED = 3
LIVES = 30
MAX_ASTEROIDS = 20
MAX_BACKGROUND_ASTEROIDS = 5
MAX_SPEED = 10

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

background_asteroid_images = [
    pygame.transform.scale(pygame.image.load("asteroid1.png").convert_alpha(), (64, 64)),
]

all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
asteroid_group = pygame.sprite.Group()
background_group = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = player_image
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT // 2
        self.speed = 5
        self.max_speed = MAX_SPEED
        self.angle = 0
        self.vx = 0
        self.vy = 0

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_q] or keys[pygame.K_x]:
            self.angle += 5
            self.image = pygame.transform.rotate(self.original_image, self.angle)
        if keys[pygame.K_e] or keys[pygame.K_c]:
            self.angle -= 5
            self.image = pygame.transform.rotate(self.original_image, self.angle)
        if keys[pygame.K_w]:
            self.vx += -self.speed * math.sin(math.radians(self.angle)) * 0.05
            self.vy += -self.speed * math.cos(math.radians(self.angle)) * 0.05

        # затормаживание
        self.vx *= 0.99
        self.vy *= 0.99

        # ограничение на максимальную скорость
        speed = math.sqrt(self.vx ** 2 + self.vy ** 2)
        if speed > self.max_speed:
            factor = self.max_speed / speed
            self.vx *= factor
            self.vy *= factor

        self.rect.x += self.vx
        self.rect.y += self.vy
        self.rect = self.image.get_rect(center=self.rect.center)

        # проверяем выход за границы экрана
        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0
        elif self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT


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

        side = random.randint(1, 4)
        if side == 1:  # сверху
            self.rect.x = random.randint(0, SCREEN_WIDTH)
            self.rect.y = -self.rect.height
        elif side == 2:  # снизу
            self.rect.x = random.randint(0, SCREEN_WIDTH)
            self.rect.y = SCREEN_HEIGHT
        elif side == 3:  # справа
            self.rect.x = SCREEN_WIDTH
            self.rect.y = random.randint(0, SCREEN_HEIGHT)
        else:  # слева
            self.rect.x = -self.rect.width
            self.rect.y = random.randint(0, SCREEN_HEIGHT)

        # случайное направление движения
        self.direction = pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize()

        self.speed = random.randint(1, 4)

    def update(self):
        # перемещаем астероид в заданном направлении
        self.rect.move_ip(self.speed * self.direction.x, self.speed * self.direction.y)

        # проверяем выход за границы экрана
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT
        elif self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0


class AsteroidBackround(Asteroid):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(random.choice(background_asteroid_images),
                                            (random.randint(30, 45), random.randint(30, 45))).convert_alpha()
        self.image.set_alpha(148)
        self.speed = random.randint(1, 2)


player = Player()
all_sprites.add(player)
player_group.add(player)

clock = pygame.time.Clock()
running = True
while running:

    # фон
    screen.blit(background_image, (0, 0))

    # астероиды
    if len(background_group) < MAX_BACKGROUND_ASTEROIDS:
        if random.randint(0, 100) in range(4):
            asteroid = AsteroidBackround()
            all_sprites.add(asteroid)
            background_group.add(asteroid)
    if len(asteroid_group) < MAX_ASTEROIDS:
        if random.randint(0, 100) in range(4):
            asteroid = Asteroid()
            all_sprites.add(asteroid)
            asteroid_group.add(asteroid)

    # выстрелы
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx, player.rect.top, player.angle)
                all_sprites.add(bullet)
                bullet_group.add(bullet)

    # кнопки
    keys = pygame.key.get_pressed()

    # движение
    player.update(keys)

    bullet_group.update()

    asteroid_group.update()

    background_group.update()

    # столкновения
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

    # текст (сколько жизней)
    font = pygame.font.Font(None, 36)

    text = font.render(f"Lives: {LIVES}", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.topright = (SCREEN_WIDTH - 10, 10)

    screen.blit(text, text_rect)

    all_sprites.draw(screen)
    player_group.draw(screen)

    # Отображение
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
