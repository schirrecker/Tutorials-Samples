import random
from random import randint

n = int(input("Nombre de Chifre: "))

for i in range(0, n):
  chifre = randint(0, 9)
  print("Voici un chifre: " + str(chifre))