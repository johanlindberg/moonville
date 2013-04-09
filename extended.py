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

# Moonville imports
from constants import *

class Sprite(cocos.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(Sprite, self).__init__(*args, **kwargs)

    def covers(self, position):
        """Returns True is position is covered by Sprite, otherwise False."""
        left   = self.position[0] - (self.width / 2)
        right  = self.position[0] + (self.width / 2)
        top    = self.position[1] + (self.height / 2)
        bottom = self.position[1] - (self.height / 2)

        x, y = position
        if x > left and x < right and y < top and y > bottom:
            return True
        else:
            return False
        
