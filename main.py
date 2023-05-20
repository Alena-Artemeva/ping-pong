from pygame import *
game = True
win_height = 500
win_weight = 500
mw = display.set_mode((500,500))
mw.fill((104, 237, 188))

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def resert(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

playr = Player('ff.png', 5, 100, 20, 100, 10)
player = Player('ff.png', 100, 100, 20, 100, 10)
  
while game: 
    for e in event.get(): 
        if e.type == QUIT: 
            game = False
    playr.update_l()
    playr.resert()

    playr.update_r()
    playr.resert()

    display.update()
    clock.tick(FPS)

