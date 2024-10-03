import RPi.GPIO as gp
from time import sleep

try:
    gp.setmode(gp.BCM)
    b = [6, 12, 5, 0, 1, 7, 11, 8]
    b.reverse()
    for i in b:
        gp.setup(i, gp.OUT, initial=gp.LOW)
    gp.setup(13, gp.OUT, initial=gp.HIGH)
    gp.setup(14, gp.IN)
    while True:
        s = ""
        for i in range(8):
            gp.output(b[i], gp.HIGH)
            sleep(0.05)
            if gp.input(14):
                gp.output(b[i], gp.LOW)
                s = s+"0"
            else:
                s = s+"1"
            sleep(0.05)
        k = int(s, 2)
        print(round(k/255*3.3, 2))
        for j in range(8):
                gp.output(b[j], gp.LOW)
        n = input()
        if n == "q":
            break
except Exception as ex:
    print(ex)
finally:
    for j in range(8):
        gp.output(b[j], gp.LOW)
    gp.cleanup()  