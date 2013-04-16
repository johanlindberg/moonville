#### Moonville

#### This work is licensed under the Creative Commons Attribution-ShareAlike 3.0
#### Unported License. To view a copy of this license, visit
#### http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to:
####
####  Creative Commons
####  444 Castro Street, Suite 900
####  Mountain View CA 94041
####  USA.

import os
import os.path
import sys

# Platform imports
import cocos

# Moonville imports
from constants import *
import scenes.menu
import model

class Moonville(object):
    def __init__(self):
        self.start()

    def load_games(self):
        """Returns a list of the available games in /games."""

        self.root_dir = os.path.abspath(".")
        self.games_dir = os.path.abspath(GAMES_DIR + "/")
        games = []
        for fname in os.listdir(self.games_dir):
            game_dir = self.games_dir + "/" + fname
            if os.path.isdir(game_dir) and \
               fname[0] != ".":
                games.append(fname)

        return games

    def load_levels(self, game):
        """Returns a list of the available levels for <game>."""

        levels_dir = os.path.abspath(GAMES_DIR + "/" + game + "/levels")
        levels = []
        for fname in os.listdir(levels_dir):
            level_dir = levels_dir + "/" + fname
            if os.path.isdir(level_dir) and \
               fname[0] != ".":
                levels.append(fname)

        return levels
        
        
    def load_game(self, game):
        """Initializes Moonville with <game>'s configuration.

        XXX This implies that current working directory (cwd) is where
        moonville.py is located. Once we package this as an executable that
        might not be the case.
        """
        game_dir = os.path.abspath(GAMES_DIR + "/" + game)
        if os.path.exists(game_dir) and \
           os.path.isdir(game_dir):
            self.game = game
            self.game_dir = game_dir

            self.locations = self.load_locations(game_dir)

            self.model = model.PartI()

    def load_locations(self, game_dir):
        """XXX Hard coded level easy! JL 2013-04-16"""
        locations_dir = os.path.abspath(game_dir + "/levels/easy/" + LOCATIONS_DIR)
        if os.path.exists(locations_dir) and \
           os.path.isdir(locations_dir):
            self.locations_dir = locations_dir
            locations = []
            for f in os.listdir(locations_dir):
                if f[-5:] == ".conf" and \
                   f[0] != "." and \
                   not os.path.isdir(locations_dir + "/" + f):
                    
                    locations.append(f)

            return locations
        
    def start(self):
        """Starts the Moonville platform."""
        
        cocos.director.director.init(resizable = False, width = WIDTH, height = HEIGHT)
        cocos.director.director.run(scenes.menu.Main_Menu(self))
    
if __name__ == "__main__":
    moonville = Moonville()
