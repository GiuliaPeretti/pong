import pygame
from settings import *

class Paddle:

    COLOR=WHITE
    VEL=4

    def __init__(self, x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.w, self.h))
    
    def move(self, up=True):
        if up:
            self.y-=self.VEL
        else:
            self.y+=self.VEL
        draw()





def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y -left_paddle.VEL >=5:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y +left_paddle.VEL+left_paddle.h <=HEIGHT-5:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y -right_paddle.VEL >=5:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and left_right_paddlepaddle.y +right_paddle.VEL+right_paddle.h <= HEIGHT-5:
        right_paddle.move(up=False)


pygame.init()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong♥")

def draw():
    WINDOW.fill(BLACK)
    
    w,h=10, 60
    x,y=WIDTH//2-w//2, 10
    for i in range(10, HEIGHT, HEIGHT//20):
        pygame.draw.rect(WINDOW, WHITE,(x,y,w,h))
        y=y+h+10


    right_paddle.draw(WINDOW)
    left_paddle.draw(WINDOW)
    pygame.display.update()



if __name__=='__main__':
    run = True
    clock=pygame.time.Clock()
    

    left_paddle=Paddle(10, HEIGHT//2-PADDEL_HEIGHT//2, PADDEL_WIDTH, PADDEL_HEIGHT)
    right_paddle=Paddle(WIDTH-10-PADDEL_WIDTH, HEIGHT//2-PADDEL_HEIGHT//2, PADDEL_WIDTH, PADDEL_HEIGHT)
    
    draw()


    while run:
        clock.tick(FPS )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys= pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)
    pygame.quit()