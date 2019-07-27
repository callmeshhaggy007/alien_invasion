import sys
import pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from pygame.sprite import Group
from scoreboard import Scoreboard
from alien import Alien
import game_functions as gf


def run_game():
    """used this to create a pyhton game window and respond to user interface"""
    # initialize game and create a screen object
    pygame.init()
    ai_settings=Settings()

    #earlier we passed the dimensions of the screen size directly but now we will pass the dimensions variable
    # in which the dimension is stored in another file

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button=Button(ai_settings,screen,"Play")
    #we create a play button and pass it further to update screen

    #create an instance to store game statistics.
    stats=GameStats(ai_settings)
    #creating an instance to store game statistics and create a scoreboard
    sb=Scoreboard(ai_settings,screen,stats)

    bg_color=(230,230,230)

    #making a ship
    ship=Ship(ai_settings,screen)

    #make a group to store bullets in. it is masde outside the loop
    # so that each time new group is not created and the program does
    # not becomes slow
    bullets=Group()

    #make a group of aliens
    aliens=Group()
    #create a fleet of aliens.
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #earlier we passed the value of the color from here directly but now we have created a variable for that
    # which store the color in it in the file settings
    #makes the ALIENS
    alien = Alien(ai_settings, screen)
    # start main loop for the game


    while True:
        # earlier the watch for mouse and key events was from here but
        # now we have created another module for that

        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)

        if stats.game_active:
            #this loop is used when we want the code to run only when
            # game is active i.e. the user has ships remaining with him
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            # did above code to make main file minimalistic
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
            # updating the position of each alien along with passing the
            # parameter for finding it the alien is at the edge
            # all the arguments in the update_aliens above will be used to
            # track the no. of ships left with the player once alien hits the ship

        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
        #it contains the attributes which will be updated along with the screen


        #redraws the screen through each pass through of the loop
        #meaning it will fill the screen using the function used in the next line of code
        #we have now passed the variable for the color rather than passing the color

        screen.fill(ai_settings.bg_color)

        ship.blitme()
        #used to draw the loaded ship on the foreground once the background has been drawn
        alien.blitme()
        #used to draw the loaded alien on the foreground once the background has been loaded
        # make the most recently drawn screen visible.
        pygame.display.flip()


run_game()