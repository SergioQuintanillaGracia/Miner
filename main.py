from ursina import *
from resource_spots import *
from mresource import *
from player import *

app = Ursina(borderless = False)
camera.orthographic = True

player1 = player(0, 0, "sergio", "#86B9CE")
test_spot = resource_spot(0, 0, 10, resource("iron"))
second_test_spot = resource_spot(20, 0, 1, resource("iron"))


def update():
    player1.update_movement()
    mouse_x = mouse.position[0] * 40 + camera.x
    mouse_y = mouse.position[1] * 40 + camera.y


def input(key):
    #NOTE: Does not work, because the camera is orthographic
    #Fix: Make every entity smaller and closer, changing their position in some way
    #if key == "scroll up":
    #    camera.z += 5
    #if key == "scroll down":
    #    camera.z -= 5
    
    pass


app.run()