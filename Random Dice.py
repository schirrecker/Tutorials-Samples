'''
Virtual Die

Proggramed by Alois
___________________
'''

import random
import time
from time import sleep


def One():
  print(" _______")
  print("|       |")
  print("|   O   |")
  print("|_______|")
  
def Two():
  print(" _______")
  print("| O     |")
  print("|       |")
  print("|_____O_|")

def Three():
  print(" _______")
  print("| O     |")
  print("|   O   |")
  print("|_____O_|")

def Four():
  print(" _______")
  print("| O   O |")
  print("|       |")
  print("|_O___O_|")
  
def Five():
  print(" _______")
  print("| O   O |")
  print("|   O   |")
  print("|_O___O_|")
  
def Six():
  print(" _______")
  print("| O   O |")
  print("| O   O |")
  print("|_O___O_|")
  
def Roll():
  rolled = random.choice(['One','Two','Three','Four','Five','Six'])
  return rolled

sleep(0.5)

while True:
  
  roll = str(Roll())
  
  if roll == 'One':
    One()
  
  if roll == 'Two':
    Two()
  
  if roll == 'Three':
    Three()
  
  if roll == 'Four':
    Four()
  
  if roll == 'Five':
    Five()
    
  if roll == 'Six':
    Six()
  print("")
  print("")
  
  
  sleep(3.5)
