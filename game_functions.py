import sys
from time import sleep
#sleep function is imported to pause the game
import pygame
from bullet import Bullet
from alien import Alien



def fire_bullet(ai_settings,screen,ship,bullets):
    """fires a bullet if the limit not reached yet"""
    """create a new bullet and add it to the bullet group""" """whenever a new method/bullet is created we add it to the bullets group"""
    if len(bullets) < ai_settings.bullets_allowed:
        """this condition is used to limit the bullets on the screen so that player dont waste bullets"""
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """it will respond to the keypresses along with the bullets group as we have passed the bullet argument in it also"""
    if event.key == pygame.K_RIGHT:  # detects if the key pressed is the right key
        # will move the ship to right
        ship.moving_right = True  # used for modifying the value rathr than changing the ships position we change it directlty to true
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key==pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key==pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
        """it will respond to the key release"""
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False


def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    """it will respond to keypress and mouse events."""
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:    #detects wheteher a key is pressed or not
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type==pygame.KEYUP:      #new block to rsspond to the keyup event when the user releases the key
            check_keyup_events(event,ship)
                #it will move the ship to right
        elif event.type==pygame.MOUSEBUTTONDOWN:
            #detects a mouse down event occouring anywhere on the screen
            mouse_x,mouse_y=pygame.mouse.get_pos()
            #did this to obtain position of mouse click
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)
            #passes the tuples of the mouse click
            # to the event which are checked further

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    """starts a new game when the player clicks play"""
    #play button has access to all the variables
    # stored in the play button attribute
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
    #this is done to avoid starting the game is a click is made
    # by mistake in the region of the button
    #now the game will start if button clicked and game not currently active
    if button_clicked and not stats.game_active:
        #it checks that the colliding point of the mouse
        # tuple and that of the image rect are same
        #hides the mouse cursor.
        ai_settings.initialize_dynamic_settings()
        #reset the game settings dynamically
        # i.e. it will increase the speed once the
        # complete flr=eet of the aliens has been shot down
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        #this is done to provide user with 3 new
        # ships to play with once the game restarts
        stats.game_active=True
        #when set true game begins

        # calling done to reset the scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        #empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        #create new fleet and center the ship
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()


def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    """basic use was to refactor the basic developed code once again"""
    """updates images on the screen and flips to a new screen."""
    #redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    #redraw all the bullets behind ship and aliens.
    #also the bullets are redrawn on the screen
    #bullet.sprite return the list of all sprite in group of bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        # used to draw the bullets on the screen
    ship.blitme()
    #make the most recently drawn screen visible
    aliens.draw(screen)

    #draw the score information
    sb.show_score()

    #draws the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()
    #draws each element at the position defined by the rect attribute
    pygame.display.flip()


def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """update the position of bullets and get rid of old bullets"""
    #update bullet positions
    bullets.update()
    # this group automatically updates each sprite i.i each time wen we fire a bullet
    for bullet in bullets.copy():
        """copy method is used so that we can modify the bullets inside the loop"""
        if bullet.rect.bottom <= 0:
            """checking if the bullets crossed the top of the screen"""
            bullets.remove(bullet)
    #check for any bullet that has hit aliens
    #if so then get rid of the bullet and the alien
    check_bullet_alien_collision(ai_settings,screen,stats,sb,ship,aliens,bullets)
    #all attributes are passed in the called function

def check_bullet_alien_collision(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """it responds to alien bullet collision"""
    #removes the alien along with the bullet that have collided
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        #to check if the collisions have taken place
        for aliens in collisions.values():
            #looping to avoid variations in the score
            #earlier if multiple bullets hir a single
            # alien score was to be updates acc.
            stats.score += ai_settings.alien_points * len(aliens)
            # increases the score image
            sb.prep_score()
            #updates the increased score image
        check_high_score(stats,sb)
    if len(aliens)==0:
        # destroy existing bullets and create a new fleet
        #checking whether the group of aliens is empty
        bullets.empty()
        #if group of aliens is empty, empty() fn. removes the bullets
        # from the screen or we can say it removes remaining sprites from a group
        ai_settings.increase_speed()
        #it will increase the speed of the new fleet created
        #if entire fleet gets destroyed it will increase the level
        stats.level+=1
        sb.prep_level()
        #call made to make sure new level is displayed correctly
        create_fleet(ai_settings,screen,ship,aliens)
        #it fills the screen again with aliens

def get_number_aliens_x(ai_settings,alien_width):
    """determining the number of aliens that fit in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    # calculating the horizontal space available for aliens
    number_aliens_x = int(available_space_x/(2*alien_width))
    # finding th number of aliens that can fit in this space
    # int is used so that we dont get partial aliens also range
    # requires int var.
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    """determine the number of rows of aliens that fit on the screen"""
    available_space_y=(ai_settings.screen_height-(3*alien_height)-ship_height)
    number_rows = int(available_space_y/(2 * alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """create an alien and place it in a row. also used give a look at the numbers of aliens from 0"""
    alien=Alien(ai_settings,screen)
    #create a new alien and set its x coord value to place in the row
    alien_width=alien.rect.width
    # we get the aliens width from its rect attribute
    alien.x=alien_width + 2 * alien_width * alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings,screen,ship,aliens):
    """create a full fleet of aliens"""
    #create an element and finding its number in the row
    #Spacing between each alien is equal to one alien width
    alien=Alien(ai_settings,screen)
    #created a demo alien which will not be the part of the
    # fleet and wont be added in group aliens
    number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)



    #create the fleet of aliens
    for row_number in range(number_rows):
        #nested looping to create multiple rows on the screen
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
            #helpful in creating new rows and create an entire fleet

def check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """check if any aliens have reached the botom of the screen."""
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            #an alien is considered to reach bottom when ts rect bottom value is greater than or equal to screen rect bottom value
            ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
            # treat this the same way as the ship got hit
            break


def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """checks if the fleet is at an edge, and then update
    the position of all the aliens in a fleet"""
    #update aliens contains the parameters so that it can
    # pass them to the call ship_hit in this block
    check_fleet_edges(ai_settings,aliens)
    """updates the position of all the aliens in a fleet"""
    aliens.update()
    #look for alien ship collision
    if pygame.sprite.spritecollideany(ship,aliens):
        #provides the output i.e. the alien and the print statement once the alien hits the ship
        #if no collision takes place it return none and the if block does not execute
        ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
        #passing sb to ship hit
    #look for the aliens hitting the bottom of the screen
    check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets)
    #it is called after updating the position of the aliens and looking for the collisions and has access to the scoreboard object

def check_fleet_edges(ai_settings, aliens):
    """respond appropriately if any aliens have reached an edge"""
    for alien in aliens.sprites():
        #looping through each of the fleet and callng check edges on each alien
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            #used to make the change in the direction of the fleet
            break

def change_fleet_direction(ai_settings,aliens):
    """drop the entire fleet and change the fleets direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
        #looping through each of the alien in the fleet and dropping the
        # aliens down using the fleet_drop_soeed
    ai_settings.fleet_direction *= -1
    #it is used to change the fleets direction by multiplying it
    # with -1 representing change in the direction

def ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """respond to ship being hit by alien"""
    if stats.ships_left>0:
        # decrement ships_left i.e. we reduce the no. of ships left for the player
        stats.ships_left -= 1
        #update scoreboard i.e. the no. of ships left
        sb.prep_ships()
        #called to display the updated ships left on the screen
        # emptying the list of aliens and bullets
        aliens.empty()
        bullets.empty()
        # creating new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # pause i.e. it will pause the game for time provided once the alien hits the ship
        sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)

def check_high_score(stats,sb):
    """checks to see if there is new high score"""
    #stats used to track the current score and the high score
    #sb used to modify the high score
    if stats.score>stats.high_score:
        #checking if the current score is greater than high score
        stats.high_score=stats.score
        #updateing the value of current score as high score
        sb.prep_high_score()
        #calling this function to update the image of high score
