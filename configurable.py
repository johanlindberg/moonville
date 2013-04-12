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

class Scene(cocos.scene.Scene):
    def __init__(self):
        super(Scene, self).__init__()

    def load_configurations(self, moonville, *args):
        self.game_dir = moonville.game_dir
        for arg in args:
            self._load_configuration(arg)

    def _load_configuration(self, configuration):
        try:
            conf = open(self.game_dir + "/" + configuration)
            for line in conf.readlines():
                line = line.strip()

                pair = self._parse(line)
                if pair is not None:
                    attr, value = pair
                    try:
                        self.__dict__["set_%s" % (attr)](value)
                    
                    except KeyError, e:
                        print "WARNING: In %s. '%s' is not an available configuration item." % (configuration, attr)
            
        finally:
            conf.close()

    def _parse(self, line):
        # remove comments
        pos = line.find("#")
        if pos != -1:
            line = line[:pos].strip()

        # parse attributes and values
        pair = None
        pos = line.find("=")
        if pos != -1:
            attr = line[:pos].strip()
            value = line[pos+1:].strip()
            pair = (attr, value)

        return pair

    def _parse_int(self, value):
        try:
            return int(value)
        
        except ValueError:
            print "WARNING: '%s' is not an int value. This item will be ignored!" % (value)

    def _parse_color(self, value):
        try:
            r, g, b, a = value.split(",")
            if r[0] == "(":
                r = r[1:]
            if a[-1] == ")":
                a = a[:-1]

            return (int(r), int(g), int(b), int(a))
                
        except ValueError:
            print "WARNING: '%s' is not a valid color value. This item will be ignored!" % (value)

    def _parse_bool(self, value):
        if value.lower() == "true":
            return True
        elif value.lower() == "false":
            return False
        else:
            return None
            
