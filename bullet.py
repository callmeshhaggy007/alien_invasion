import pygame
from pygame.sprite import Sprite
#sprite is used to group related elements in a game
#and acts together on all the grouped elements at once

class Bullet(Sprite):
    """a class which manages bullets fired frm the ship"""
    def __init__(self,ai_settings,screen,ship):
        """create a bullet object at the ships current position"""
        super(Bullet,self).__init__()
        self.screen=screen
        #create a bullet rect at (0,0) and then set correct position
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        #we have created the bullet from the scratch using the rect class
        self.rect.centerx=ship.rect.centerx
        #did this to fix the center of the bullet same as that of the ship
        self.rect.top=ship.rect.top
        #did this to make the bullet look that it is fired from the top of
        # the ship by setting its posi at the top of the ship image
        #store the bullets position as decimal values so that we can find
        # and make make adjustments to the bullet speed
        self.y=float(self.rect.y)
        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor
        #storing th bullets color and speed factor in the variables mentioned above

    def update(self):
        """move the bullets up the screen """
        #it updates the decimal position of the bullets
        self.y-=self.speed_factor
        #as the bullet is moving up on the screen the value of the y coord is
        # decreasing for which we do the substraction between the two
        #updates the rect position
        self.rect.y=self.y

    def draw_bullet(self):
        """draw the bullet to the screen """
        pygame.draw.rect(self.screen,self.color,self.rect)