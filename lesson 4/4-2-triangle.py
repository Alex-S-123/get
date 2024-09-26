import RPi.GPIO as gp
from time import sleep


def analog(n, b):
    s = bin(n)[2:]
    for j in range(8):
        gp.output(b[j], gp.LOW)
    while len(s) < 8:
        s = "0" + s
    for j in range(8):
        if s[j] == "1":
            gp.output(b[j], gp.HIGH)

gp.setmode(gp.BCM)
b = [6, 12, 5, 0, 1, 7, 11, 8]

for i in b:
    gp.setup(i, gp.OUT, initial=gp.LOW)
b.reverse()
n = int(input())
try:
    while True:
        for i in range(256):
            analog(i, b)
            sleep(n/512)
        for i in range(256):
            analog(255-i, b)
            sleep(n/512)
finally:
    for i in b:
        gp.output(i, gp.LOW)      
    gp.cleanup()  