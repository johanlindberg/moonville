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
import extended
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

        self.add(MouseClickLayer(self), z = 2)

    def load_LVCS(self):
        self.LVCS_button_out = extended.Sprite(POPUP_MENU_RESOURCES + "/LVCS_Button_Out.png")
        
        self.LVCS_button_in = extended.Sprite(POPUP_MENU_RESOURCES + "/LVCS_Button_In.png")
        self.LVCS_button_in.opacity = 0

        self.LVCS_button_out.position = (16, 40)
        self.LVCS_button_in.position = (16, 40)
        
        self.add(self.LVCS_button_out, z = 4)
        self.add(self.LVCS_button_in, z = 4)

        x, y = 68, 40
        for item in LVCS:
            item_frame = extended.Sprite(POPUP_MENU_RESOURCES + "/LVCS_Item_Frame.png")
            item_filename = "/%s_64x64.png" % (item.replace(" ", "-"))
            item_sprite = extended.Sprite(LVCS_RESOURCES + item_filename)

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

        # Toggle the LVCS button
        if show:
            self.LVCS_button_in.do(cocos.actions.FadeIn(0.25))
            self.LVCS_button_out.do(cocos.actions.FadeOut(0.25))
        else:
            self.LVCS_button_in.do(cocos.actions.FadeOut(0.25))
            self.LVCS_button_out.do(cocos.actions.FadeIn(0.25))

        self.showing_LVCS = show
        delay = 0.1

        # Reverse the "animation" when hiding
        items = self.LVCS_sprites
        if self.showing_LVCS == False:
            items = reversed(items)
            
        for item in items:
            frame, sprite = item
            
            if show:
                action = cocos.actions.FadeIn(1)
            else:
                action = cocos.actions.FadeOut(1)
                
            frame.do(cocos.actions.Delay(delay) + action)
            sprite.do(cocos.actions.Delay(delay) + action)

            delay += 0.05

class MouseClickLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self, scene):
        super(MouseClickLayer, self).__init__()
        self.scene = scene

    def on_mouse_press(self, x, y, buttons, modifiers):
        self.handle_LVCS_toggle(x, y)
        self.handle_select_item(x, y)

    def handle_LVCS_toggle(self, x, y):
        # Check for LVCS toggle button press
        if self.scene.LVCS_button_in.opacity > 0 and \
           self.scene.LVCS_button_in.covers((x, y)):

            self.scene.show_LVCS(False)
            
        elif self.scene.LVCS_button_out.opacity > 0 and \
             self.scene.LVCS_button_out.covers((x, y)):
            
            self.scene.show_LVCS(True)

    def handle_select_item(self, x, y):
        items = self.scene.LVCS_sprites
        for item in items:
            frame, sprite = item
            if sprite.covers((x, y)):
                if sprite.opacity == 255:
                    sprite.opacity = 192
                else:
                    sprite.opacity = 255
        
    def on_mouse_motion (self, x, y, dx, dy):
        pass
