from tkinter import *
import time
from time import sleep
# from mcpi.minecraft import Minecraft

'''
mc = Minecraft.create()
pos = mc.player.getPos()

#change world immutable to True
mc.setting("world_immutable", False)

# Blocks used
'''

def hello():
    print("hello world")

# tkinter
tk = Tk()

btn = Button(tk, text="click me!", command=hello)
btn.pack()
