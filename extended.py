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
        
