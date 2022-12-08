from ursina import *
from random import randint
import resource_spots as respot
import mresource as res
import player as pl
import miner as min

app = Ursina(borderless = False)
camera.orthographic = True

player1 = pl.player(0, 0, "sergio", "#86B9CE")

for i in range(20):
    respot.resource_spot(randint(-50, 50), randint(-50, 50), randint(3, 10), res.resource("iron"))


def update():
    player1.update_movement()
    mouse_x = mouse.position[0] * 40 + camera.x
    mouse_y = mouse.position[1] * 40 + camera.y

    for i in min.miner_list:
        i.update()


def input(key):
    #NOTE: Does not work, because the camera is orthographic
    #Fix: Make every entity smaller and closer, changing their position in some way
    #if key == "scroll up":
    #    camera.z += 5
    #if key == "scroll down":
    #    camera.z -= 5
    
    if key == "m":
        global miner
        miner = min.miner()
        miner.to_cursor()

    if key == "left mouse down":
        try:
            miner.place()
        except:
            pass


app.run()