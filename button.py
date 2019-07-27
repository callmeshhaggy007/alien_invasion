import pygame.font
#lets pygame render the text on the screen

class Button():
    def __init__(self,ai_settings,screen,msg):
        """initiaalize button attriibute.   contains the parameters which will contain the text in the button"""
        self.screen=screen
        self.screen_rect=screen.get_rect()

        #set the dimensions and properties of button.
        self.width = 200
        self.height=50
        #set the button dimensions
        self.button_color=(0,255,0)
        #set the button color
        self.text_color=(255,255,255)
        #set the buttons text color
        self.font=pygame.font.SysFont(None,48)
        #prepares font attribute for rendering text on the screen
        #none attribute tells it to use default font
        #48 tells the size of the font that should be used in it

        #build the buttons rect object and place it at the center.
        self.rect =pygame.Rect(0, 0, self.width, self.height)
        self.rect.center=self.screen_rect.center

        #the button message needs to be preaped only once.
        self.prep_msg(msg)
        """pygame works as text/string by converting it in the form of image"""
        #we call the function prep msg which tells which text needs to be printed on the screen

    def prep_msg(self,msg):
        """turns message into a rendered image and centers the text on the button"""
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        #the font.render function converts the text into an image which is stord in the following variable
        #a method called the antialiasing method which works to make the edge of text
        # smoother is also passed along with this in the form of the boolean operator
        self.msg_image_rect = self.msg_image.get_rect()
        #used to center the text image on the button.
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #draws blank button.
        self.screen.fill(self.button_color,self.rect)
        #draws the message image in the blank button
        self.screen.blit(self.msg_image,self.msg_image_rect)