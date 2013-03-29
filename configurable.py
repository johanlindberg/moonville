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
