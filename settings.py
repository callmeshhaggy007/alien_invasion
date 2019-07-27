#basic module to store the settings of the game using class
#REASON to create this was to aviod writing the code for settings again and again and
# we could directly change values from here if we want any of the changes in our code



class Settings():

    """A class to store all the setting of the game alien invasion"""

    def __init__(self):

        """initialize the game's static settings settings via options below"""

        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)

        """ship settings"""
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        """bullets settings"""
        self.bullet_speed_factor=3
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=60,60,60
        self.bullets_allowed=20
        #limits the players to a specific no. of bullets

        """alien settings"""
        self.alien_speed_factor=1
        #used to control the speed of the aliens
        self.fleet_drop_speed = 10
        #controls how quickly the fleet drops down the screen
        self.fleet_direction = 1
        # fleet direction of 1 represents righ and -1 represents left

        #how quickly the game speeds up
        self.speedup_scale = 1.1
        #it controls by how much value does the game speeds up each time
        self.score_scale = 1.5
        #when game gets harder aliens have more points
        self.initialize_dynamic_settings()
        #this is done so that we can make the
        # settings we wish to change throught the game

    def initialize_dynamic_settings(self):
        """initialize settings that changes throught
        the game by firstly setting the initial speeds"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor=1
        #fleet direcrion of 1 represents right,
        # and -1 represents left direction
        self.fleet_direction=1
        #scoring
        self.alien_points=50
        #set dynamically so that if any collision
        # takes place it updates the points

    def increase_speed(self):
        """increase speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *=self.speedup_scale
        #when we have provided speedup scale for each of the
        # variable it will keep on increasing the speed of
        # the game each and every time
        self.alien_points=int(self.alien_points*self.score_scale)
        #increases the points of each alien hit