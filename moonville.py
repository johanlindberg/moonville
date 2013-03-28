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

# Platform imports
import cocos
import pyglet

# Moonville imports
from constants import *
import scenes

class Moonville(object):
    def __init__(self):
        self.load_games()

    def load_games(self):
        """Initializes the list of available game configurations.

        XXX This implies that current working directory (cwd) is where
        moonville.py is located. Once we package this as an executable that
        might not be the case.
        """
        
        self.games = []
        cwd = os.path.abspath(os.getcwd())
        if os.path.exists(cwd + GAMES_DIR):
            for d in os.listdir(cwd + GAMES_DIR):
                if d[0] != "." and \
                   os.path.isdir(cwd + GAMES_DIR + "/" + d):
                    
                    self.games.append(d)

    def start(self):
        """Starts the Moonville platform."""
        
        cocos.director.director.init(resizable = False, width = 800, height = 600)
        scene = cocos.scene.Scene()

        main = scenes.Main(self.games)
        
        multiplex = cocos.layer.MultiplexLayer(main)
        scene.add(multiplex, z = 0)
        cocos.director.director.run(scene)
    
if __name__ == "__main__":
    print HEADER

    moonville = Moonville()
    moonville.start()
