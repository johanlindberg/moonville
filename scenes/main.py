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
import cocos.actions
import cocos.layer
import cocos.scenes.transitions
import cocos.sprite
import pyglet

# Moonville imports
from constants import *
import configurable
import scenes.build

class Main(configurable.Scene):
    def __init__(self, moonville):
        super(Main, self).__init__()
        self.moonville = moonville

        # XXX You need to re-think what should be configurable
        # in this scene! (JL 2013-04-08)
        self.load_configurations(self.moonville, MAIN)

        background = cocos.sprite.Sprite(RESOURCES + "/Main_Menu_Background.png")
        background.position = (400, 300)

        new_game_option = cocos.sprite.Sprite(RESOURCES + "/New_Game_Menu_Option.png")
        new_game_option.position = (180, 330)

        options_option = cocos.sprite.Sprite(RESOURCES + "/Options_Menu_Option.png")
        options_option.position = (180, 270)
        
        self.add(cocos.layer.ColorLayer(0, 0, 0, 255), z = 0)
        
        self.add(background, z = 1)
        self.add(new_game_option, z = 2)
        self.add(options_option, z = 2)

        self.add(MouseClickLayer(self.moonville, [(new_game_option, self.on_new_game),
                                                  (options_option, self.on_options), ]), z = 3)

    # Menu callbacks
    def on_new_game(self):
        build = scenes.build.Build(self.moonville)
        cocos.director.director.replace(cocos.scenes.transitions.ZoomTransition(build, duration = 2))
        
    def on_options(self):
        print "TBD!"
        
    def on_quit(self):
        pyglet.app.exit()


class MouseClickLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self, moonville, options):
        super(MouseClickLayer, self).__init__()
        self.moonville = moonville
        self.options = options

    def on_mouse_press(self, x, y, buttons, modifiers):
        for option in self.options:
            sprite, callback = option
            left, right = sprite.position[0] - (sprite.width / 2), sprite.position[0] + (sprite.width / 2)
            top, bottom = sprite.position[1] - (sprite.height / 2), sprite.position[1] + (sprite.height / 2)

            if x > left and x < right and y > top and y < bottom:
                callback()
