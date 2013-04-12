#### Moonville

#### This work is licensed under the Creative Commons Attribution-ShareAlike 3.0
#### Unported License. To view a copy of this license, visit
#### http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to:
####
####  Creative Commons
####  444 Castro Street, Suite 900
####  Mountain View CA 94041
####  USA.

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
import scenes.build

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
        super(LocationMenu, self).__init__("Choose a location")

        self.moonville = moonville
        self.game = moonville.game

        self.items = []
        index = 0
        for location in self.moonville.locations:
            self.items.append(cocos.menu.MenuItem(location[:-5],
                                                  self.location_handler(index)))
            index += 1

        self.create_menu(self.items,
                         cocos.actions.ScaleTo(1.2, duration = 0.1),
                         cocos.actions.ScaleTo(1.0, duration = 0.1))

    def location_handler(self, index):
        i = index
        def _callback():
            self.moonville.location = index
            build = scenes.build.Build(self.moonville)
            cocos.director.director.replace(cocos.scenes.transitions.ZoomTransition(build, duration = 2))
        return _callback
