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

        # load introduction text from file
        try:
            text_in = open(self.information['text'])
            text = cocos.text.RichLabel(text = "".join(text_in.readlines()), position = (10, 580))
            self.add(text, z = 1)

        finally:
            text_in.close()

        self.add(cocos.layer.ColorLayer(32, 32, 32, 255), z = 0)
        
