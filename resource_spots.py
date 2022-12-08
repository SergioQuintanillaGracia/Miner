from ursina import *

resource_spot_count = 0

class resource_spot():
    def __init__(self, x, y, size, resource):
        global resource_spot_count
        
        self.x = x
        self.y = y
        self.size = size
        self.resource = resource
        self.entity = Entity(model = "circle", scale = size, position = (self.x, self.y, 10), color = resource.color, tag = f"resource_spot_{resource_spot_count}")
        resource_spot_count += 1
        self.entity.collider = "sphere"

    def get_entity(self):
        return self.entity