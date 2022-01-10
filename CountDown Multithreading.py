import time
import threading


def countDown(n):
    print ("Countdown from " + str(n))
    print ("")
    for i in reversed(range(0, n)):
        time.sleep(1)
    print ("Countdown from " + str(n) + " is over")
        

t1 = threading.Thread(target = countDown, args = (10, ))
t2 = threading.Thread(target = countDown, args = (15, ))
t3 = threading.Thread(target = countDown, args = (5, ))
t4 = threading.Thread(target = countDown, args = (20, ))

t1.start()
t2.start()
t3.start()
t4.start()

