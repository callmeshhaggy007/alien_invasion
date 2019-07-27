#now in this we will count how many times the ship has been
# hit and this will also be helpful for the scoring purpose

class GameStats():
    """track statistics for alien invasion"""

    def __init__(self,ai_settings):
        """initialize statistics."""
        self.ai_settings=ai_settings
        self.reset_stats()
        #it here call the reset stats whose work is to set the stats properly when firstly the gamestats is loaded
        #starts alien invasion in an active state
        #start the game in an inactive state
        self.game_active = False

        #high score should never be reset
        self.high_score=0
        #initialized in this because we dont want it o be reset


    def reset_stats(self):
        """initialize stats that can change through out the game."""
        self.ships_left=self.ai_settings.ship_limit
        self.score=0
        self.level=1
        #setting initial level as 1