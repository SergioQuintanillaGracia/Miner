from ursina import *

movement_speed = 20
camera_smoothing = 5

class player():
    def __init__(self, x, y, name, color):
        self.x = x
        self.y = y
        self.z = -10
        self.name = name
        self.color = color
        self.entity = Entity(model = "quad", scale = (2, 5), position = (self.x, self.y, self.z), color = self.color)
        self.text_square = Entity(model = "quad", scale = (0.75, 0.75), position = (self.x, self.y + 3, self.z + 1), color = "#3E3E3E")
        
        self.text_default_x = self.text_square.x / 40
        self.text_default_y = self.text_square.y / 40

        self.text = Text(text = name, position = (self.text_default_x, self.text_default_y), scale = 0.7)
        self.text.x -= self.text.width / 2
        self.text.y += self.text.height / 2
        self.text_square.scale_x = self.text.width * 40

    def get_entity(self):
        return self.entity

    def update_movement(self):
        movement = movement_speed * time.dt
        
        if held_keys["w"]:
            self.entity.y += movement

        if held_keys["a"]:
            self.entity.x -= movement

        if held_keys["s"]:
            self.entity.y -= movement

        if held_keys["d"]:
            self.entity.x += movement

        self.x, self.y = self.entity.x, self.entity.y
        self.text_square.x, self.text_square.y = self.x, self.y + 3

        camera_movement_x = (self.entity.x - camera.x) * time.dt * camera_smoothing
        camera_movement_y = (self.entity.y - camera.y) * time.dt * camera_smoothing
        camera.x += camera_movement_x if abs(camera_movement_x) > 0.01 else 0
        camera.y += camera_movement_y if abs(camera_movement_y) > 0.01 else 0

        self.text.x = self.text_default_x + (self.x - camera.x) / 40 - self.text.width / 2
        self.text.y = self.text_default_y + (self.y - camera.y) / 40 + self.text.height / 2