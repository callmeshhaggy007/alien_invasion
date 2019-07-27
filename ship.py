import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        #ai setting is added so that the ship has access to the settings panel for the ship

        """initializing the screen and setting its initial values"""

        super(Ship,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        #did this so that we can use it further as an attribute
        #load the image of the ship and get its rectangle
        self.image=pygame.image.load('images/ship.bmp')      #used to load the ship stored in the variable
        self.rect=self.image.get_rect()       #pygame let us treat the elements of the game as rectangle
        self.screen_rect=screen.get_rect()          #used to position the ship at the bottom center
        #starting each new ship at the bottom of the screen
        self.rect.centerx=self.screen_rect.centerx          #now we match the centerx attribute of the screens rect(it is x coord)
        self.rect.bottom=self.screen_rect.bottom            #we make this or provide this as the y coord
        #store a decimal value for the ships center
        self.center=float(self.rect.centerx)
        #this was done because we know that rect and centerx can hold interger values
        # only so we created a float variable to solve this problem further
        #moving the flag i.e. we will provide continous movement of the ship
        # until key pressed it lets the ship to move to one side only
        self.moving_right=False
        self.moving_left = False

    def update(self):
        """updates the ships position based on the movement flag which means until the key is pressed"""
        #update the ships position based on the value of the flagi.e. we are limiting
        # the position of the ship once it reaches the border of the screen
        # #updates the center value of the ship but not the rect
        if self.moving_right and self.rect.right<self.screen_rect.right:
            #until the upper condition is false ship has not reached the boundary
            self.center+=self.ai_settings.ship_speed_factor
            #now when the value is updated according to the factor passed in settings
            # the new ammount is stored in ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            # until the upper condition is false ship has not reached the boundary
            self.center-=self.ai_settings.ship_speed_factor
        #now updating the rect object from self.center.
        #we have used this now because this controls the position of the ship so it
        # will take only the integer values of self.center and stores it it in centerx
        self.rect.centerx=self.center

    def blitme(self):                                        #used to draw the image loaded on the screen at positin of the   "self.rect"
        """draw the ship at its current locstion"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """center the ship on the screen. by setting the ships center attribute equauls to the center of the screen"""
        self.center = self.screen_rect.centerx