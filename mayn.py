# Здесь будет мой код 
from pygame import *
 
class GameSprite(sprite.Sprite):
    def __init__(self, w , h, x, y, img, speed):
       super().__init__()
       self.image = transform.scale(image.load(img), (w ,h ))
       self.speed = speed
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update(self):
        k = key.get_pressed() # Получаем нажатую клавишу
        if k[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if k[K_s] and self.rect.y < w - 80:
            self.rect.y += self.speed

mixer.init()
mixer.music.load("Grim Delarosa — Tyga Type Beat - SWIZZY (Instrumental).mp3")
mixer.music.play()

font.init()
font1 = font.SysFont("Arial", 36)


 
w, h = 1200, 800
window = display.set_mode((w,h))
display.set_caption("Ping-Pong")
bg = transform.scale(image.load("razmetka_dlja_tennisnogo_korta1.jpg"), (w,h))
player1 = Player(80, 120, 100, 350, "oval-23967_1280.png", 10)

run = True
finish = False

while run :
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.blit(bg, (0,0))
        

        player1.update()
        player1.reset()

    display.update()
    time.delay(60)
