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

class Menu(configurable.Scene):
    def __init__(self):
        super(Menu, self).__init__()

        ## Load the background image
        self.background_image = pyglet.image.load(MAIN_MENU_RESOURCES + "/background.png")
        self.background_sprite = cocos.sprite.Sprite(self.background_image)
        self.background_sprite.position = (400, 300)
        
        self.add(self.background_sprite, z = 0)

class Main_Menu(Menu):
    def __init__(self, moonville):
        super(Main_Menu, self).__init__()
        self.moonville = moonville

        ## dicts for images and sprites
        self.game_image,  self.game_sprite  = {}, {}

        ## Load the <game> menu option images
        self.games = self.moonville.load_games()
        x, y = 492, 440
        for game in self.games:
            img = self.moonville.games_dir + "/" + game + "/main_menu.png"
            self.game_image[game] = pyglet.image.load(img)
            self.game_sprite[game] = extended.Sprite(self.game_image[game])
            self.game_sprite[game].position = (x, y)
            
            self.add(self.game_sprite[game], z = 1)
            y -= 30

        self.add(MouseClickLayer(self), z = 2)

    def on_mouse_press(self, x, y, buttons, modifiers):
        for game in self.games:
            sprite = self.game_sprite[game]
            if sprite.opacity > 0 and \
               sprite.covers((x, y)):
                self.on_select(game)

    def on_select(self, game):
        sprite = self.game_sprite[game]
        x, y = sprite.position

        self.moonville.load_game(game)
        
        build = scenes.build.Build(self.moonville)
        cocos.director.director.replace(
            cocos.scenes.transitions.FadeDownTransition(build, duration = 1))

class MouseClickLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self, scene):
        super(MouseClickLayer, self).__init__()
        self.scene = scene

    def on_mouse_press(self, x, y, buttons, modifiers):
        self.scene.on_mouse_press(x, y, buttons, modifiers)
