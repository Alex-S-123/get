import RPi.GPIO as gp
from time import sleep

try:
    gp.setmode(gp.BCM)
    b = [6, 12, 5, 0, 1, 7, 11, 8]

    for i in b:
        gp.setup(i, gp.OUT, initial=gp.LOW)
    b.reverse()
    gp.setup(13, gp.OUT, initial=gp.HIGH)
    gp.setup(14, gp.IN)
    while True:
        k = -1
        while gp.input(14) == 0:
            k += 1
            if k == 256:
                break
            s = bin(k)[2:]
            for j in range(8):
                gp.output(b[j], gp.LOW)
            while len(s) < 8:
                s = "0" + s
            for j in range(8):
                if s[j] == "1":
                    gp.output(b[j], gp.HIGH)
            sleep(0.01)
        print(round(k/256*3.3, 2))
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