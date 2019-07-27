import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a class to represent a single alien in a fleet"""
    def __init__(self,ai_settings,screen):
        """initializes the alien and sets its initial position"""
        super(Alien,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings

        #load the alien image and setting its rectangular attribute
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()

        #start each new alien near the top left corner of the screen
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        #store the aliens exact position in x coord
        self.x=float(self.rect.x)

    def blitme(self):
        """draws the alien on the screen at the current location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """return true if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        #to find out if the alien is at the right edge and thus returning true if so
        elif self.rect.left<=0:
            return True
        #to find out if the alien is at the left edge and thus returning true if so

    def update(self):
        """move the alien right"""
        self.x+=(self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        #alien position is tracked using this attribute which stores the decimal values
        #now motion could be detected to both left and right as the speed factor id
        # multiplied by fleet dir value
        self.rect.x=self.x
        #we then use self.x value to update aliens rect

