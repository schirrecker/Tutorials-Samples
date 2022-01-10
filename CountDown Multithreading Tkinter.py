import time
import threading
from tkinter import Tk, Label, Canvas

def countDown(n):
    tk = Tk()
    canvas = Canvas(tk, width=50, height=25)
    canvas.pack()
    for i in reversed(range(0, n+1)):
        time.sleep(1)
        label = Label(tk, text=str(i))
        label.pack()
        tk.update()
        

n = 10
t = []

for i in range(0, n):
    t.append(threading.Thread(target = countDown, args = (5, )))

startTime = time.time()

for task in t:
    task.start()

endTime = time.time()
delta = endTime - startTime
print ("Time: ", int(delta), " sec.")


