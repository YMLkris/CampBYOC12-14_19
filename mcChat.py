import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create("172.16.42.27",4711)
from time import sleep
chatMsg = input("Enter a message: ")

while chatMsg != "/exit":
    mc.postToChat("is this annoying?")
    #chatMsg = input("Enter a message: ")
    sleep(1)