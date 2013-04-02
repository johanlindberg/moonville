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

import os.path

# Platform imports
import cocos
import cocos.actions
import cocos.layer
import cocos.sprite
import cocos.text
import pyglet

# Moonville imports
from constants import *
import configurable

class Location(configurable.Scene):
    def __init__(self, moonville):
        super(Location, self).__init__()
        self.moonville = moonville

        # Moon overlay
        moon = cocos.sprite.Sprite(RESOURCES + "/moon_overlay.png")
        moon.position = (WIDTH - 100, 100)
        
        self.add(cocos.layer.ColorLayer(0, 0, 0, 255), z = 0)
        self.add(moon, z = 1)
        self.add(LocationMenu(moonville), z = 2)


class LocationMenu(cocos.menu.Menu):
    def __init__(self, moonville):
        super(LocationMenu, self).__init__(moonville.game)

        self.moonville = moonville
        self.game = moonville.game

        self.items = []
        index = 1
        for location in self.moonville.locations:
            self.items.append(cocos.menu.MenuItem("%s. %s" % (index, location[:-5]),
                                                  self.location_handler(index - 1)))
            index += 1

        self.create_menu(self.items,
                         cocos.actions.ScaleTo(1.2, duration = 0.1),
                         cocos.actions.ScaleTo(1.0, duration = 0.1))

    def location_handler(self, index):
        i = index
        def _callback():
            print "You clicked on ", self.moonville.locations[i]
        return _callback
