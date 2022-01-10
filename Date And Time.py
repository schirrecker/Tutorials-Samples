import datetime
import random
from random import randint
from time import sleep

Random_Year = randint(0, 2018)

print("The First Day Of ", Random_Year)
print(datetime.date(Random_Year,1,1))
print("")

while True:
    
    
    print("Today Precise to the Microsecond: ", datetime.datetime.today())
##    print(datetime.datetime.today())
##    sleep(0.8635)
##    for i in range(1, 60):
##        print("")
