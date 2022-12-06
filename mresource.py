from ursina import *

class resource():
    def __init__(self, material):
        self.material = material

        if self.material == "iron":
            self.color = color.white
        if self.material == "copper":
            self.color = color.orange