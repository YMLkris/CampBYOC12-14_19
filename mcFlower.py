import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create("172.16.42.27",4711)

import time

while True:
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z

    block = 38

    mc.setBlock(x,y,z, block)

    time.sleep(0.2)