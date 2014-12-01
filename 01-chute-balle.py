import pygame
import random
  
# Definition de quelques couleurs
#---- A MODIFIER -----#
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)

# Hauteur et largeur de l'ecran
screen_width = 700
screen_height = 400
 
 
# Initialisation
pygame.init()
  
screen = pygame.display.set_mode([screen_width, screen_height])

# On met la balle sur un emplacement au hasard
x_pos = random.randrange(screen_width)
y_pos = random.randrange(screen_height)
  
done = False
  
clock = pygame.time.Clock()
  
# Tout le travail est fait ici
while not done:
    for event in pygame.event.get(): 
        # Quand on clique sur "exit", le programme s'arrete
        if event.type == pygame.QUIT: 
            done = True 
 
    # Couleur de l'ecran
    #---- A MODIFIER -----#
    screen.fill(WHITE)

    # Deplace la balle vers le bas
    #---- A MODIFIER -----#
    y_pos += 10
    
    # Si la balle sort de l'ecran, on la remet en haut
    if y_pos > screen_height:
        y_pos = 0

    # Dessine le rectangle
    #---- A MODIFIER -----#
    pygame.draw.rect(screen, BLACK, [x_pos, y_pos, 50, 30])
    # Mise a jour de l'ecran
    pygame.display.flip()

    # 20 frames par second
    clock.tick(20)
  
  
pygame.quit()
