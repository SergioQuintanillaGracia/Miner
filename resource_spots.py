from ursina import *

class resource_spot():
    def __init__(self, x, y, size, resource):
        self.x = x
        self.y = y
        self.size = size
        self.resource = resource
        self.entity = Entity(model = "circle", scale = size, position = (self.x, self.y, 10), color = resource.color)

    def get_entity(self):
        return self.entity