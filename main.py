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

class Ball:
    MAX_VEL=5
    COLOR=(247, 2, 162)

    def __init__(self, x, y, r) -> None:
        self.x=self.original_x=x
        self.y=self.original_y=y
        self.r=r
        self.x_vel=self.MAX_VEL
        self.y_vel=0
    
    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x,self.y),self.r)

    def move(self):
        self.x +=self.x_vel
        self.y +=self.y_vel

    def reset():
        self.x=self.original_x
        self.y=self.original_y
        self.x_vel=0
        self.y_vel*=-1


def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y -left_paddle.VEL >=5:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y +left_paddle.VEL+left_paddle.h <=HEIGHT-5:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y -right_paddle.VEL >=5:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y +right_paddle.VEL+right_paddle.h <= HEIGHT-5:
        right_paddle.move(up=False)
    



pygame.init()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong♥")

def draw():
    WINDOW.fill(BLACK)
    
    w,h=4, 50
    x,y=WIDTH//2-w//2, 5
    for i in range(10, HEIGHT, HEIGHT//20):
        pygame.draw.rect(WINDOW, WHITE,(x,y,w,h))
        y=y+h+10

    font=pygame.font.SysFont("comicsans", 50)
    left=font.render(str(left_score), 1, WHITE)
    WINDOW.blit(left, (WIDTH//4-left.get_width()//2, 20))
    right=font.render(str(left_score), 1, WHITE)
    WINDOW.blit(right, (WIDTH*(3/4)+right.get_width()//2, 20))


    ball.draw(WINDOW)
    right_paddle.draw(WINDOW)
    left_paddle.draw(WINDOW)
    
    pygame.display.update()

def collision(ball, right_paddle, left_paddle):
    if(ball.y+ ball.r>=HEIGHT):
        ball.y_vel*=-1
    elif(ball.y- ball.r<=0):
        ball.y_vel*=-1
    
    if(ball.x_vel<0):
        if (ball.y>=left_paddle.y and ball.y<=left_paddle.y+left_paddle.h):
            if(ball.x-ball.r<=left_paddle.x + left_paddle.w):
                ball.x_vel*=-1
                middle_y=left_paddle.y + left_paddle.h//2
                difference_y=middle_y-ball.y
                reduction_factor=(left_paddle.h//2)/ball.MAX_VEL
                y_vel= difference_y/reduction_factor
                ball.y_vel=y_vel*-1
    else:
        if (ball.y>=right_paddle.y and ball.y<=right_paddle.y+right_paddle.h):
            if(ball.x+ball.r>=right_paddle.x):
                ball.x_vel*=-1

                middle_y=right_paddle.y + right_paddle.h//2
                difference_y=middle_y-ball.y
                reduction_factor=(right_paddle.h//2)/ball.MAX_VEL
                y_vel= difference_y/reduction_factor
                ball.y_vel=y_vel*-1





if __name__=='__main__':
    run = True
    clock=pygame.time.Clock()
    
    left_score=0
    right_score=0
    left_paddle=Paddle(10, HEIGHT//2-PADDEL_HEIGHT//2, PADDEL_WIDTH, PADDEL_HEIGHT)
    right_paddle=Paddle(WIDTH-10-PADDEL_WIDTH, HEIGHT//2-PADDEL_HEIGHT//2, PADDEL_WIDTH, PADDEL_HEIGHT)
    ball=Ball(WIDTH//2,HEIGHT//2, BALL_RADIUS)
    draw()


    while run:
        clock.tick(FPS)
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys= pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        ball.move()
        collision(ball, right_paddle, left_paddle)
        if ball.x<0:
            right_score+=1
        elif ball.x>WIDTH:
            left_score+=1


    pygame.quit()