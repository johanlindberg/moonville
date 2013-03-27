#### Moonville

import cocos
import pyglet

NAME = u"Moonville"
VERSION = u"0.1\u03B1"

HEADER = "%s %s" % (NAME, VERSION)

LICENSE = """Copyright (c) 2013 Johan Lindberg

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

class MainMenu(cocos.menu.Menu):
    def __init__(self):
        super(MainMenu, self).__init__(NAME)

        self.menu_anchor_y = "CENTER"
        self.menu_anchor_x = "CENTER"

        items = []

        items.append(cocos.menu.MenuItem('NEW GAME', self.on_new_game) )
        items.append(cocos.menu.MenuItem('QUIT', self.on_quit) )

        self.create_menu(items, cocos.menu.zoom_in(), cocos.menu.zoom_out())

    def on_new_game(self):
        print "NEW GAME"

    def on_quit(self):
        pyglet.app.exit()

if __name__ == "__main__":
    print HEADER
    print LICENSE

    moonville = cocos.director.director
    
    moonville.init(resizable = False, width = 800, height = 600)
    scene = cocos.scene.Scene()
    multiplex = cocos.layer.MultiplexLayer(MainMenu())
    scene.add(multiplex, z = 0)
    moonville.run(scene)
