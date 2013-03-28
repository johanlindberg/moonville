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

import copy

# Platform imports
import cocos
import pyglet

# Moonville imports
from constants import *

class Main(cocos.menu.Menu):
    def __init__(self, games):
        super(Main, self).__init__(NAME)

        self.menu_anchor_y = "CENTER"
        self.menu_anchor_x = "CENTER"

        items = []
        for game in games:
            attr = "on_play_%s" % (game.lower())
            self.__dict__[attr] = self._make_game_callback(game)
            
            items.append(cocos.menu.MenuItem("PLAY %s:%s" % (NAME, game), self.__dict__[attr]))

        items.append(cocos.menu.MenuItem("QUIT", self.on_quit) )
        self.create_menu(items, cocos.menu.zoom_in(), cocos.menu.zoom_out())

    def _make_game_callback(self, game):
        def _temp():
            print "Play %s" % (game)
        return _temp
        
    def on_quit(self):
        pyglet.app.exit()
