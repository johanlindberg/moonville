#### Moonville

#### This work is licensed under the Creative Commons Attribution-ShareAlike 3.0
#### Unported License. To view a copy of this license, visit
#### http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to:
####
####  Creative Commons
####  444 Castro Street, Suite 900
####  Mountain View CA 94041
####  USA.

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
            item_image = pyglet.image.load(LVCS_RESOURCES + item_filename)
            item_sprite = extended.Sprite(item_image)

            item_frame.position = (x, y)
            item_sprite.position = (x, y)

            item_frame.opacity = 0
            item_sprite.opacity = 0

            self.add(item_frame, z = 3)
            self.add(item_sprite, z = 4)
            
            x += 68

            self.LVCS_sprites.append(copy.copy((item_frame, item_sprite, item_image)))

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
            frame, sprite, image = item
            
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
        if self.handle_LVCS_toggle(x, y):
            return
        
        if self.handle_select_item(x, y):
            return
        
        if self.handle_deploy_LVCS_item(x, y):
            return

    def handle_LVCS_toggle(self, x, y):
        # Check for LVCS toggle button press
        if self.scene.LVCS_button_in.opacity > 0 and \
           self.scene.LVCS_button_in.covers((x, y)):

            self.scene.show_LVCS(False)
            self.scene.moonville.model.selected_LVCS_item = None
            
            return True
            
        elif self.scene.LVCS_button_out.opacity > 0 and \
             self.scene.LVCS_button_out.covers((x, y)):
            
            self.scene.show_LVCS(True)
            return True

    def handle_select_item(self, x, y):
        for item in self.scene.LVCS_sprites:
            frame, sprite, image = item
            if sprite.covers((x, y)):
                if sprite.opacity == 255:
                    sprite.opacity = 192
                    self.scene.moonville.model.selected_LVCS_item = self.scene.LVCS_sprites.index(item)
                else:
                    sprite.opacity = 255
                    self.scene.moonville.model.selected_LVCS_item = None

                return True

    def handle_deploy_LVCS_item(self, x, y):
        if self.scene.moonville.model.selected_LVCS_item:
            index = self.scene.moonville.model.selected_LVCS_item

            gx, gy = (x / 64), (y / 64)
            if self.scene.moonville.model.grid[gx][gy] != -1:
                return False
            
            _x = (gx * 64) + 32
            _y = (gy * 64) + 32

            _, sprite, image = self.scene.LVCS_sprites[index]
            gsprite = extended.Sprite(image)
            gsprite.position = (_x, _y)
            self.scene.add(gsprite, z = 5)

            self.scene.moonville.model.grid[gx][gy] = index

            sprite.opacity = 255
            self.scene.moonville.model.selected_LVCS_item = None

            return True
    
    def on_mouse_motion (self, x, y, dx, dy):
        pass
