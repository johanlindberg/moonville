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

# Platform imports
import cocos
import pyglet

# Moonville imports
from constants import *


class Main(cocos.scene.Scene):
    def __init__(self, moonville):
        super(Main, self).__init__()
        self.add(cocos.layer.MultiplexLayer(MainMenu(moonville)), z = 0)

class MainMenu(cocos.menu.Menu):
    def __init__(self, moonville):
        super(MainMenu, self).__init__(moonville.game)

        self.game = moonville.game

        self.menu_anchor_y = "CENTER"
        self.menu_anchor_x = "CENTER"

        items = [cocos.menu.MenuItem("PLAY GAME", self.on_play_game),
                 cocos.menu.MenuItem("QUIT", self.on_quit)]
        
        self.create_menu(items, cocos.menu.zoom_in(), cocos.menu.zoom_out())

    def on_play_game(self):
        print "Play %s" % (self.game)
        
    def on_quit(self):
        pyglet.app.exit()
