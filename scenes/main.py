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
import scenes.introduction

class Main(configurable.Scene):
    def __init__(self, moonville):
        super(Main, self).__init__()

        self.font_title = {}

        ## Available configuration items
        def set_title_font_name(font_name):
            self.font_title['font_name'] = font_name
        self.set_title_font_name = set_title_font_name
        
        def set_title_font_size(font_size):
            font_size = self._parse_int(font_size)
            if font_size:
                self.font_title['font_size'] = font_size
        self.set_title_font_size = set_title_font_size

        def set_title_color(color):
            color = self._parse_color(color)
            if color:
                self.font_title['color'] = color
        self.set_title_color = set_title_color

        def set_title_bold(bold):
            bold = self._parse_bool(bold)
            if bold:
                self.font_title['bold'] = bold
        self.set_title_bold = set_title_bold
        
        def set_title_italic(italic):
            italic = self._parse_bool(italic)
            if italic:
                self.font_title['italic'] = italic
        self.set_title_italic = set_title_italic

        self.load_configurations(moonville, MAIN)

        # Moon overlay
        moon = cocos.sprite.Sprite("moon_overlay.png")
        moon.position = (700, 100)
        
        self.add(cocos.layer.ColorLayer(0, 0, 0, 255), z = 0)
        self.add(moon, z = 1)
        self.add(MainMenu(moonville, self.font_title), z = 2)

class MainMenu(cocos.menu.Menu):
    def __init__(self, moonville, _font_title):
        super(MainMenu, self).__init__(moonville.game)

        # Update configuration items
        self.font_title.update(_font_title)

        self.moonville = moonville
        self.game = moonville.game

        self.items = [cocos.menu.MenuItem("PLAY", self.on_play),
                      cocos.menu.MenuItem("QUIT", self.on_quit)]

        self.create_menu(self.items,
                         cocos.actions.ScaleTo(1.2, duration = 0.1),
                         cocos.actions.ScaleTo(1.0, duration = 0.1))

    def on_play(self):
        intro = scenes.introduction.Introduction(self.moonville)
        cocos.director.director.replace(cocos.scenes.transitions.ZoomTransition(intro, duration = 2))
        
    def on_quit(self):
        pyglet.app.exit()
