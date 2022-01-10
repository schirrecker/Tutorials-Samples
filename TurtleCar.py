from tkinter import *
import time
from time import sleep
import turtle

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_rectangle(50, 50, 100, 100)


# basic, fast, and truck are the three choices
carType = 'fast'

car = turtle.Pen()

def action(event):
    global car, carType
    
    if event.keysym == 'Up':
        if carType == 'basic':
            car.forward(3)
            canvas.move (1, 0, -3)
        elif carType == 'fast':
            car.forward(8)
        elif carType == 'truck':
            car.forward(4)
            sleep(0.02)
            
    elif event.keysym == 'Down':
        if carType == 'basic':
            car.backward(2)
        elif carType == 'fast':
            car.backward(3)
        elif carType == 'truck':
            car.backward(2)
            sleep(0.02)

    elif event.keysym == 'Right':
        if carType == 'basic':
            car.right(4)
        elif carType == 'fast':
            car.backward(2)
        elif carType == 'truck':
            car.right(4)
            
    elif event.keysym == 'Left':
        if carType == 'basic':
            car.left(4)
        elif carType == 'fast':
            car.left(2)
        elif carType == 'truck':
            car.left(4)
            
    elif event.keysym == 'Space':
        if carType == 'basic':
            car.forward(400)
            car.forward(-400)
        elif carType == 'fast':
            car.forward(400)
            car.forward(-400)
        elif carType == 'truck':
            car.forward(400)
            car.forward(-400)
            
canvas.bind_all('<KeyPress-Up>', action)
canvas.bind_all('<KeyPress-Down>', action)
canvas.bind_all('<KeyPress-Right>', action)
canvas.bind_all('<KeyPress-Left>', action)
canvas.bind_all('<KeyPress-Space>', action)
