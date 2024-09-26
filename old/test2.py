import RPi.GPIO as gp
from time import sleep

gp.setmode(gp.BCM)
b = [6, 12, 5, 0, 1, 7, 11, 8]

for i in b:
    gp.setup(i, gp.OUT, initial=gp.LOW)
b.reverse()
for i in range(10):

    n = int(input())
    s = bin(n)[2:]
    print(s)
    for j in range(8):
        gp.output(b[j], gp.LOW)
    while len(s) < 8:
        s = "0" + s
    for j in range(8):
        if s[j] == "1":
            gp.output(b[j], gp.HIGH)
    