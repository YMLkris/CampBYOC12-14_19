import mcpi.minecraft as minecraft
from guizero import *


mc=minecraft.Minecraft.create()

block=4
air=0

def buildHouse():
    pos=mc.player.getPos()

    x=pos.x + 2
    y=pos.y
    z=pos.z + 2
    x2=x+float(length.value)
    y2=y+float(height.value)
    z2=z+float(width.value)

    mc.setBlocks(x,y,z,x2,y2,z2,block)
    mc.setBlocks(x+1, y+1, z+1, x2-1, y2-1,z2-1, air)
    mc.setBlocks(x+5,y+1,z,x+5,y+2,z, air)
    #mc.setBlocks(x+5,y+1,z,x+5,y+2,z, 64)

app = App(title='Build a House', width = 300, height = 300, layout='grid', bgcolor='lightblue')

length = TextBox(app, text='10', grid=[1,1])
width = TextBox(app, text='5', grid=[1,2])
height= TextBox(app, text='8', grid=[1,3])
makeHouse=PushButton(app, command=buildHouse, text='Build My House', grid=[1,5])