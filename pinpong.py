
from pygame import *

font.init()
font = font.Font(None,70)
window = display.set_mode((1000, 800))
display.set_caption("trash")
fon = transform.scale(image.load("123.jpg"),(1000, 800))
class Gamer(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(Gamer):
    def Control_1(self):
        control = key.get_pressed()
        
        if control[K_w] and self.rect.y > 50:
            self.rect.y -= self.speed
        if control[K_s] and self.rect.y < 700:
            self.rect.y += self.speed
            
    def Control_2(self):
        control = key.get_pressed()
        
        if control[K_e] and self.rect.y > 50:
            self.rect.y -= self.speed
        if control[K_d] and self.rect.y < 700:
            self.rect.y += self.speed        
         
        

class Enemy(Gamer):
    def update(self):
        self.rect.y += self.speed
        global miss
        if self.rect.y >800:
            self.rect.x = randint(100,900)
            self.rect.y = 0
            miss +=1



game = True 
Finish = False
clock = time.Clock()
player1 = Player('levo.png',100,400,8)
player2= Player('pravo.png',900,400,8)
ball = Player('bs.jpg',500,400,0)
ball_x=2
ball_y=2
red = font.render('победа за красными', True,(255,0,0))
black = font.render('победа за черными', True,(255,0,0))




while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if Finish != True:
        window.blit(fon,(0,0))
        
        
        player1.reset()
        player1.Control_1()
        player2.reset()
        player2.Control_2()
        ball.reset()
        ball.rect.x +=ball_x
        ball.rect.y -=ball_y

        if sprite.collide_rect(player1,ball) or sprite.collide_rect(player2,ball):
            ball_x *= -1
            ball_y *= 1
        if ball.rect.y < 0 or ball.rect.y >600:
            ball_y *=-1
        if ball.rect.x < -50:
            finish = True
            window.blit(red,(300,400))
        if ball.rect.x > 1000:
            finish= True
            window.blit(black,(300,400))
            


        display.update()
    
        clock.tick(60)