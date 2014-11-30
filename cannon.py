import pygame
import random
  
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)

# Set the height and width of the screen
screen_width = 700
screen_height = 400
 
class Ball(pygame.sprite.Sprite):
    """
    This class represents the ball        
    It derives from the "Sprite" class in Pygame
    """
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block, 
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super(Ball, self).__init__() 
  
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
  
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values 
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
         
    def update(self):
        """ Called each frame. """
 
        # Move block down one pixel
        self.rect.y += 10
         
        # If block is too far down, reset to top of screen.
        if self.rect.y > screen_height:
            self.rect.y = 0
 
# Initialize Pygame
pygame.init()
  
screen = pygame.display.set_mode([screen_width, screen_height])
  
#block_list = pygame.sprite.Group()
  
ball = Ball(BLACK, 20, 15)
  
# Set a random location for the block
ball.rect.x = random.randrange(screen_width)
ball.rect.y = random.randrange(screen_height)
allsprites = pygame.sprite.RenderPlain(ball)
      
#Loop until the user clicks the close button.
done = False
  
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
  
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        # If user clicked close
        if event.type == pygame.QUIT: 
            done = True 
  
    screen.fill(WHITE)
    ball.update()
    allsprites.draw(screen)
      
    # Limit to 20 frames per second
    clock.tick(20)
  
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
  
pygame.quit()
