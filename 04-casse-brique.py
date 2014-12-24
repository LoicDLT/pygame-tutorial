import pygame
import sys

# Definition de quelques couleurs
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0,   255)

# Hauteur et largeur de l'ecran
screen_width = 700
screen_height = 400

game_over = False

class Ball(pygame.Rect):
    def __init__(self, x=screen_width, y=screen_height/2, radius=10, speed_x=5,
            speed_y=5):

        pygame.Rect.__init__(self, x - radius, y - radius, 2*radius, 2*radius)
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y

    def bounce(self):
        self.speed_y = -self.speed_y

    # Gere le rebond
    def bounce_border(self):
        #---- A MODIFIER -----#
        if self.y + self.radius >= screen_height or self.y <= self.radius: 
            self.speed_y = -self.speed_y

        if self.x + self.radius >= screen_width  or self.x <= self.radius:
            self.speed_x = -self.speed_x
    
    def bounce_paddle(self):
        if ball.colliderect(paddle):
            ball.y = paddle.y - 2*ball.radius
            ball.bounce()

    def bounce_wall(self):
        for brick in wall.bricks:
            if ball.colliderect(brick):
                wall.bricks.remove(brick)
                ball.bounce()

    # Met a jour la position de la balle et la dessine
    def update(self):
        self.bounce_border()
        self.bounce_paddle()
        self.bounce_wall()
       
        self.x += self.speed_x
        self.y += self.speed_y

        pygame.draw.circle(screen, BLACK, [self.x, self.y], self.radius)

class Paddle(pygame.Rect):
    def __init__(self, x=20, y=0.8*screen_height, width=80, height=20, speed=30):
        pygame.Rect.__init__(self, x, y, width, height)
        self.speed = speed

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed

    def move_right(self):
        if self.x + self.width < screen_width:
            self.x += self.speed

    def update(self):
        pygame.draw.rect(screen, RED, self)


class Brick(pygame.Rect):
    def __init__(self, x, y, width, height):
        pygame.Rect.__init__(self, x, y, width, height)

    def draw(self):
        pygame.draw.rect(screen, BLUE, self)

class Wall:
    def __init__(self, nbX=10, nbY=5):
        self.nbX = nbX
        self.nbY = nbY
        offsetX = 10
        offsetY = 10

        brick_width = (screen_width - (self.nbX+1)*offsetX) / self.nbX
        brick_height = 0.3*screen_height / self.nbY
        
        self.bricks = []
        y = offsetY
        for i in range(self.nbY):
            x = offsetX
            for j in range(self.nbX):
                cur = Brick(x, y, brick_width, brick_height)
                self.bricks.append(cur)
                x += brick_width + offsetX
            y += brick_height + offsetY

    def draw(self):
        for x in self.bricks:
            x.draw()

def print_message(text):
    font = pygame.font.SysFont("comicsansms", 72)
    surf = font.render(text, False, BLACK)
    screen.blit(surf, (10, 20))

# Initialisation
pygame.init()

screen = pygame.display.set_mode([screen_width, screen_height])

# On cree la balle, la raquette et le mur de briques
ball = Ball()
paddle = Paddle()
wall = Wall()

clock = pygame.time.Clock()

pygame.key.set_repeat(50, 50)

# Tout le travail est fait ici
done = False
while not done:
    # Couleur de l'ecran
    screen.fill(WHITE)

    for event in pygame.event.get(): 
        # Quand on clique sur "exit", le programme s'arrete
        if event.type == pygame.QUIT: 
            done = True

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RIGHT: 
                paddle.move_right()
            if event.key == pygame.K_LEFT: 
                paddle.move_left()

    #game_over = True
    if game_over:
        print_message("You lost")
    else:
        # Mise a jour de la balle et de la raquette
        ball.update()
        paddle.update()
        wall.draw()

    # Mise a jour de l'ecran
    pygame.display.flip()

    # 20 frames par second
    clock.tick(50)
  
pygame.quit()
