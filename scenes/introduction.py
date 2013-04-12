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
import scenes.location

class Introduction(configurable.Scene):
    def __init__(self, moonville):
        super(Introduction, self).__init__()
        self.moonville = moonville

        self.information = {}

        ## Available configuration items
        def set_information_text(filename):
            self.information['text'] = moonville.game_dir + "/" + filename
        self.set_information_text = set_information_text

        self.load_configurations(moonville, INTRODUCTION)

        index = 1
        for line in self.moonville.load_introduction(self.information):
            text = cocos.text.RichLabel(text = line,
                                        position = (20, HEIGHT - (LINE_HEIGHT * index) - 20),
                                        color = (255, 255, 255, 255))
            self.add(text, z = 1)
            index += 1

        self.add(cocos.layer.ColorLayer(32, 32, 32, 255), z = 0)

        # Moon overlay
        moon = cocos.sprite.Sprite(RESOURCES + "/moon_overlay.png")
        moon.position = (WIDTH - 100, 100)
        self.add(moon, z = 1)

        # Next arrow
        next = cocos.sprite.Sprite(RESOURCES + "/arrow_right.png")
        next.position = (WIDTH - 50, 50)
        self.add(next, z = 2)

        self.add(MouseClickLayer(self.moonville), z = 3)

class MouseClickLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self, moonville):
        super(MouseClickLayer, self).__init__()
        self.moonville = moonville

    def on_mouse_press(self, x, y, buttons, modifiers):
        if x > (WIDTH - 50) - 24 and \
           x < (WIDTH - 50) + 24 and \
           y > 50 - 24 and y < 50 + 24:
            location = scenes.location.Location(self.moonville)
            cocos.director.director.replace(cocos.scenes.transitions.ZoomTransition(location, duration = 2))
