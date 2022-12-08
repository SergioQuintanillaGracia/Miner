from ursina import *

miner_list = []

class miner():
    def __init__(self):
        global miner_list
        self.state = "following_cursor"
        self.entity = Entity(model = "quad", texture = "assets/miner.png", scale = 4, position = (mouse.position[0] * 40 + camera.x, mouse.position[1] * 40 + camera.y, 8))
        self.entity.color = color.rgba(1, 1, 1, 0.5)
        miner_list.append(self)

    def to_cursor(self):
        mouse_pos_x = mouse.position[0] * 40 + camera.x
        mouse_pos_y = mouse.position[1] * 40 + camera.y

        self.entity.x = mouse_pos_x
        self.entity.y = mouse_pos_y

    def snap_to_resource_spot(self, x, y):
        self.state = "snapped"
        self.entity.x = x
        self.entity.y = y

    def place(self):
        if self.state == "snapped":
            spot = mouse.collision.entity

            self.state = "placed"
            self.entity.color = (1, 1, 1, 1)
            self.entity.x = spot.x
            self.entity.y = spot.y
            print("placed")

    def update(self):
        try:
            entity_collision = mouse.collision.entity
        except:
            entity_collision = None

        if self.state == "placed":
            pass  # (Mine in the future)
        
        else:
            try:
                if "resource_spot" in entity_collision.tag:
                    miner.snap_to_resource_spot(self, entity_collision.x, entity_collision.y)

                else:
                    self.to_cursor()
            except:
                self.to_cursor()
            