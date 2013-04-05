#### Moonville

#### Copyright (c) 2013 Johan Lindberg

#### Permission is hereby granted, free of charge, to any person obtaining a copy
#### of this software and associated documentation files (the "Software"), to deal
#### in the Software without restriction, including without limitation the rights
#### to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#### copies of the Software, and to permit persons to whom the Software is
#### furnished to do so, subject to the following conditions:

#### The above copyright notice and this permission notice shall be included in all
#### copies or substantial portions of the Software.

#### THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#### IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#### FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#### AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#### LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#### OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#### SOFTWARE.

import os
import os.path
import sys

# Platform imports
import cocos

# Moonville imports
from constants import *
import scenes.main

class Moonville(object):
    def __init__(self, game = None):
        if game is not None:
            self.load_game(game)
            self.start()
        
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

    def load_introduction(self, information):
        text = []
        try:
            text_in = open(information['text'])
            text = text_in.readlines()

        finally:
            text_in.close()

        return text

    def load_locations(self, game_dir):
        locations_dir = os.path.abspath(game_dir + LOCATIONS_DIR)
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
        self.main = scenes.main.Main(self)
        cocos.director.director.run(self.main)
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print USAGE
        sys.exit(1)

    game = sys.argv[1]
    moonville = Moonville(game)
