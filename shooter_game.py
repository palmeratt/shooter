from pygame import *

win_width = 700
win_height = 700
window = display.set_mode(
    (win_width, win_height)
)
display.set_caption("шутер")
background = transform.scale(
    image.load("galaxy.jpg"), 
    (win_height, win_width)
)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0, 0))
    display.update()
    clock = time.Clock()
    FPS = 60
    clock.tick(FPS)

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

hero_height = 500
hero_weight = 0 

image.load("rocket.png")

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def result(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed
        if keys_pressed[K_LEFT]:
            x1 -= 30
        if keys_pressed[K_RIGHT]:
            x2 -= 30

class Enemy():
    monsters = sprite.Group()



