#### Moonville

#### This work is licensed under the Creative Commons Attribution-ShareAlike 3.0
#### Unported License. To view a copy of this license, visit
#### http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to:
####
####  Creative Commons
####  444 Castro Street, Suite 900
####  Mountain View CA 94041
####  USA.

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
import extended
import scenes.build

class Main(configurable.Scene):
    def __init__(self, moonville):
        super(Main, self).__init__()
        self.moonville = moonville

        # XXX You need to re-think what should be configurable
        # in this scene! (JL 2013-04-08)
        self.load_configurations(self.moonville, MAIN)

        background = cocos.sprite.Sprite(MAIN_MENU_RESOURCES + "/Main_Menu_Background.png")
        background.position = (400, 300)

        new_game_option = extended.Sprite(MAIN_MENU_RESOURCES + "/New_Game_Menu_Option.png")
        new_game_option.position = (180, 330)

        options_option = extended.Sprite(MAIN_MENU_RESOURCES + "/Options_Menu_Option.png")
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
            if sprite.covers((x, y)):
                callback()
