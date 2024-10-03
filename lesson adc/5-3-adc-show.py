import RPi.GPIO as gp
from time import sleep

def adc_f(b):
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
    return k/255*7.1


def adc_s(b):
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
    return k/256*7.1

try:
    gp.setmode(gp.BCM)
    b = [6, 12, 5, 0, 1, 7, 11, 8]
    b.reverse()
    for i in b:
        gp.setup(i, gp.OUT, initial=gp.LOW)
    gp.setup(13, gp.OUT, initial=gp.HIGH)
    gp.setup(14, gp.IN)
    while True:
        k = adc_f(b)
        print(k)
        for j in range(8):
            gp.output(b[j], gp.LOW)
        for j in range(8):
            if k > j:
                gp.output(b[j], gp.HIGH)
        n = input()
        for j in range(8):
            gp.output(b[j], gp.LOW)
        if n == "q":
            break
except Exception as ex:
    print(ex)
finally:
    for j in range(8):
        gp.output(b[j], gp.LOW)
    gp.cleanup()  