import pygame
import random
  
# Definition de quelques couleurs
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)

# Hauteur et largeur de l'ecran
screen_width = 700
screen_height = 400
 
class Ball(pygame.sprite.Sprite):
    """
    Cette classe represente la balle (qui est en fait un rectangle).
    """
    def __init__(self, color, width, height):
        """ Ici, on construit une balle definie par une couleurs,
        une hauteur et une largeur """
        # Appelle le parent pour construit une "sprite"
        super(Ball, self).__init__() 
 
        # On definit un rectangle avec une couleur ici
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
  
        self.rect = self.image.get_rect()
         
    def update(self):
        """ Mise à jour de l'ecran """

        # Deplace la balle vers le bas
        self.rect.y += 10
        
        # Si la basse sort de l'ecran, on la remet en haut
        if self.rect.y > screen_height:
            self.rect.y = 0
 
# Initialisation
pygame.init()
  
screen = pygame.display.set_mode([screen_width, screen_height])
  
ball = Ball(BLACK, 20, 15)
  
# On met la balle sur un emplacement au hasard
ball.rect.x = random.randrange(screen_width)
ball.rect.y = random.randrange(screen_height)
allsprites = pygame.sprite.RenderPlain(ball)

done = False
  
clock = pygame.time.Clock()
  
# Tout le travail est fait ici
while not done:
    for event in pygame.event.get(): 
        # Quand on clique sur "exit", le programme s'arrête
        if event.type == pygame.QUIT: 
            done = True 
  
    screen.fill(WHITE)
    ball.update()
    allsprites.draw(screen)
      
    # 20 frames par second
    clock.tick(20)
  
    # Mise à jour de l'ecran
    pygame.display.flip()
  
pygame.quit()
