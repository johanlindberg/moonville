#### Moonville

#### This work is licensed under the Creative Commons Attribution-ShareAlike 3.0
#### Unported License. To view a copy of this license, visit
#### http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to:
####
####  Creative Commons
####  444 Castro Street, Suite 900
####  Mountain View CA 94041
####  USA.

NAME = u"Moonville"
VERSION = u"0.2 \u03B1"

HEADER = u"%s %s" % (NAME, VERSION)

## Info
USAGE = """%s

USAGE: To start a game, run `python moonville.py <game>` on the command line.
NOTE! <game> must be the name of a directory located in /moonville/games.
""" % (HEADER)

# Moonville uses the MIT License
LICENSE = """This work is licensed under the Creative Commons Attribution-ShareAlike 3.0
Unported License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to:

 Creative Commons
 444 Castro Street, Suite 900
 Mountain View CA 94041
 USA."""

import os

## Directories
GAMES_DIR = os.getcwd() + "/games"
LOCATIONS_DIR = "/locations"
RESOURCES = "resources"
MAIN_MENU_RESOURCES = "resources/MainMenu"
POPUP_MENU_RESOURCES = "resources/PopupMenus"
LVCS_RESOURCES = "resources/LVCS"

## Configurations
COMMON = "common.conf"
MAIN = "main.conf"
INTRODUCTION = "introduction.conf"

## Window size
WIDTH = 800
HEIGHT = 600

# Text
LINE_HEIGHT = 25

# Lunar Village Construction Set
LVCS = ["Nickel-Iron Battery", "Solar Cell",
        "Industrial Robot", "3D-printer", "Aluminum Extractor",
        "Plastic Extruder", "Drilling Rig", "Induction Furnace", "Press Forge",
        "Bulldozer"]
