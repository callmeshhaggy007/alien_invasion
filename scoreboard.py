import pygame.font
#importing has been done to display the
# code in the text as it imports from python
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """a class to sccore scoreing information"""
    def __init__(self,ai_settings,screen,stats):
        """initialize scorekeeping attributes"""
        #parameters are passed as an attributes to what we are tracking.
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.ai_settings=ai_settings
        self.stats=stats

        """font setting for scoring"""
        self.text_color=(30,30,30)
        #passing a text color
        self.font=pygame.font.SysFont(None,48)
        # prepares font attribute for rendering text on the screen.
        # none attribute tells it to use default font.
        # 48 tells the size of the font that should be used in it.

        #prepare the initial score image.
        self.prep_score()
        #prepare the high score image.
        self.prep_high_score()
        #another method to display high score at another posi on the screen
        self.prep_level()
        #displays the current level below the current score
        self.prep_ships()
        #calling to display the ship as levels on the top


    def prep_score(self):
        """turn the score into a renderd image"""
        rounded_score=int(round(self.stats.score, -1))
        #tell pyhton to round the value at nearest 10
        # and stores it in the variables.
        score_str="{:,}".format(rounded_score)
        #tells to insert ',' in number while converting string to numeric values
        self.score_image=self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
        #it takes the values which or is helpful in
        # converting the string as a rendered image
        #to render the image clearly on the screen we
        # pass the screen background colors as well to
        # render along with the text color

        #display the score at the top right corner of the screen
        self.score_rect=self.score_image.get_rect()
        #it fixes the score on the top right corner of the screen
        self.score_rect.right=self.screen_rect.right - 20
        #seeting 20 px from the right edge of the screen
        self.score_rect.top=20
        #setting 20 px from the top to bottom of the screen

    def show_score(self):
        """draw score to the screen along with the level"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        #draws a level image on the screen
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """turn the high score into a rendered image"""
        high_score=int(round(self.stats.high_score, -1))
        #rounding the scores to the nearest 10.
        high_score_str="{:,}".format(high_score)
        #seperating the scores with commas.
        self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)
        #generates an image which i8s rendered on the screen
        #center the high score at the top of the screen
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.score_rect.top

    def prep_level(self):
        """turn the level into a rendered image"""
        self.level_image=self.font.render(str(self.stats.level),True,self.text_color,self.ai_settings.bg_color)
        #image to be rendered is created from this code
        #positioning the level below the score
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.score_rect.right
        # setting image right attribute same as that of the scores right attribute
        self.level_rect.top=self.score_rect.bottom+10
        #setting the top attribute of the level 10px beneath the score attribute

    def prep_ships(self):
        """show how many ships are left"""
        self.ships=Group()
        #empty group created to hold the ship instances
        for ship_number in range(self.stats.ships_left):
            #loop runs every time once for every ship left with the player
            ship=Ship(self.ai_settings,self.screen)
            ship.rect.x=10+ship_number*ship.rect.width
            #each time creating a ship appearing next to each other
            #along with 10px margin on the left side of the group
            ship.rect.y=10
            #set it as 10 so that the ship lines up along with the scoring image
            self.ships.add(ship)
            #adding each ship created to the Group ship