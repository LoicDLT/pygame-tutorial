import pygame
import random

# Definition de quelques couleurs
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)

# Hauteur et largeur de l'ecran
screen_width = 700
screen_height = 400


class Ball(pygame.Rect):
    def __init__(self, x=screen_width, y=screen_height/2, radius=10, speed_x=5,
            speed_y=5):

        pygame.Rect.__init__(self, x - radius, y - radius, 2*radius, 2*radius)
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y

    def bounce(self):
        #---- A MODIFIER -----#

    # Gere le rebond
    def bounce_wall(self):
        #---- A MODIFIER -----#

    # Met a jour la position de la balle et la dessine
    def update(self):
        self.bounce_wall()

        if ball.colliderect(paddle):
        #---- A MODIFIER -----#

        pygame.draw.circle(screen, BLACK, [self.x, self.y], self.radius)

class Paddle(pygame.Rect):
    def __init__(self, x=20, y=0.8*screen_height, width=80, height=20, speed=30):
        pygame.Rect.__init__(self, x, y, width, height)
        self.speed = speed

    def move_left(self):
        #---- A MODIFIER -----#

    def move_right(self):
        #---- A MODIFIER -----#

    def update(self):
        pygame.draw.rect(screen, RED, self)


# Initialisation
pygame.init()

screen = pygame.display.set_mode([screen_width, screen_height])

# On met la balle sur un emplacement 
ball = Ball()

paddle = Paddle()

done = False

clock = pygame.time.Clock()

pygame.key.set_repeat(50, 50)

# Tout le travail est fait ici
while not done:
    for event in pygame.event.get(): 
        # Quand on clique sur "exit", le programme s'arrete
        if event.type == pygame.QUIT: 
            done = True 

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RIGHT: 
                paddle.move_right()
            if event.key == pygame.K_LEFT: 
                paddle.move_left()

    # Couleur de l'ecran
    screen.fill(WHITE)

    # Mise a jour de la balle et de la raquette
    ball.update()
    paddle.update()

    # Mise a jour de l'ecran
    pygame.display.flip()

    # 20 frames par second
    clock.tick(50)
  
  
pygame.quit()
