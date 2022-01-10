import time
from time import sleep

# Usefull Functions:
def pindent(s):
    for i in range(0, s):
        print()

def percent(i,s):
    return i*(s/100)

def lscan(l):
    for i in l:
        sleep(0.5)
        print("Item: "+str(i)+" ")
        print("Type: value")
        pindent(1)


# Variables:
l = [1, 3, "a", 1, "A", 5]


lscan(l)
pindent(1)
print(str(percent(100,76))+"%")
