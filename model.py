#### Moonville

#### This work is licensed under the Creative Commons Attribution-ShareAlike 3.0
#### Unported License. To view a copy of this license, visit
#### http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to:
####
####  Creative Commons
####  444 Castro Street, Suite 900
####  Mountain View CA 94041
####  USA.


## Class structure for the various objects used in Moonville

## Lunar Village Construction Set (LVCS)
class LVCS(object):
    def __init__(self):
        pass

class Robonaut(LVCS):
    def __init__(self):
        pass

class Energy(LVCS):
    def __init__(self):
        pass

class Tool(LVCS):
    def __init__(self):
        pass

## Materials
class Material(object):
    def __init__(self):
        pass

class Regolith(Material):
    def __init__(self):
        pass

class Plastic(Material):
    def __init__(self):
        pass

class Aluminum(Material):
    def __init__(self):
        pass

## Mix-ins representing various capabilities
class Makeable(object):
    def __init__(self):
        pass

class Reusable(object):
    def __init__(self):
        pass
        

class PartI(object):
    def __init__(self):
        self.selected_LVCS_item = None
        self.grid = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]

    def score(self):
        """Returns the current score."""
        pass

    def use(self, objects):
        """Make use of <objs>."""

    
        

    

        

