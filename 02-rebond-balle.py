import pygame
import random
  
# Definition de quelques couleurs
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
x_pos = screen_width/2
y_pos = screen_height/2
  
done = False
  
clock = pygame.time.Clock()

rect_width = 50
rect_height = 30

# Vitesse de la balle
#---- A MODIFIER -----#
speed_x = 0
speed_y = 10

# Tout le travail est fait ici
while not done:
    for event in pygame.event.get(): 
        # Quand on clique sur "exit", le programme s'arrete
        if event.type == pygame.QUIT: 
            done = True 
 
    # Couleur de l'ecran
    screen.fill(WHITE)

    # Deplace la balle vers le bas
    y_pos += speed_y
    x_pos += speed_x
    
    # Rebond en hauteur
    #---- A MODIFIER -----#
    if y_pos < 0 or y_pos + rect_height > screen_height:
        speed_y = - speed_y

    # Dessine le rectangle
    pygame.draw.rect(screen, BLACK, [x_pos, y_pos, rect_width, rect_height])
    # Mise a jour de l'ecran
    pygame.display.flip()

    # 20 frames par second
    clock.tick(20)
  
  
pygame.quit()
