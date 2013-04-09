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
import os.path

# Platform imports
import cocos
import cocos.actions
import cocos.layer
import cocos.sprite
import cocos.tiles
import pyglet

# Moonville imports
from constants import *
import configurable

class Build(configurable.Scene):
    def __init__(self, moonville):
        super(Build, self).__init__()
        self.moonville = moonville

        # XXX This needs to go! You should split out the rocks from the tilemap
        # and randomly generate a location instead! (JL 2013-04-09)
        scrolling_manager = cocos.layer.ScrollingManager()
        surface = cocos.tiles.load(self.moonville.locations_dir + "/Sea of tranquility.tmx")["surface"]
        scrolling_manager.add(surface)

        self.LVCS_sprites = []
        self.load_LVCS()
        self.showing_LVCS = False

        self.add(cocos.layer.ColorLayer(132, 146, 119, 255), z = 0)
        self.add(scrolling_manager, z = 1)

        self.add(MouseClickLayer(self.moonville, self), z = 2)

    def load_LVCS(self):
        x, y = 40, 40
        for item in ["Nickel-Iron Battery", "Solar Cell", "Industrial Robot"]:
            item_frame = cocos.sprite.Sprite(RESOURCES + "/LVCS_Item_Frame.png")
            item_filename = "/%s_64x64.png" % (item.replace(" ", "-"))
            item_sprite = cocos.sprite.Sprite(RESOURCES + item_filename)

            item_frame.position = (x, y)
            item_sprite.position = (x, y)

            item_frame.opacity = 0
            item_sprite.opacity = 0

            self.add(item_frame, z = 3)
            self.add(item_sprite, z = 4)
            
            x += 68

            self.LVCS_sprites.append(copy.copy((item_frame, item_sprite)))

    def show_LVCS(self, show = True):
        if self.showing_LVCS == show:
            return

        self.showing_LVCS = show
        delay = 0.2
        for items in self.LVCS_sprites:
            frame, sprite = items
            
            if show:
                action = cocos.actions.FadeIn(1)
            else:
                action = cocos.actions.FadeOut(1)
                
            frame.do(cocos.actions.Delay(delay) + action)
            sprite.do(cocos.actions.Delay(delay) + action)

            delay += 0.1

class MouseClickLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self, moonville, scene):
        super(MouseClickLayer, self).__init__()
        self.moonville = moonville
        self.scene = scene

    def on_mouse_press(self, x, y, buttons, modifiers):
        self.scene.show_LVCS(False)
        
    def on_mouse_motion (self, x, y, dx, dy):
        # Check for activation of LVCS menu (bottom 20px of window)
        if y < 20:
            self.scene.show_LVCS(True)
