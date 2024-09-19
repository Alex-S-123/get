import RPi.GPIO as gp
from time import sleep

gp.setmode(gp.BCM)

for i in [2, 3, 4, 17, 27, 22, 10, 9]:
    gp.setup(i, gp.OUT, initial=gp.LOW)

a = [2, 3, 4, 17, 27, 22, 10, 9]
b = [6, 12, 5, 0, 1, 7, 11, 8]

for i in b:
    gp.setup(i, gp.OUT, initial=gp.LOW)


for i in range(10):
    for j in range(8):
        gp.output(a[j-1], 0)
        gp.output(a[j], 1)
        gp.output(b[j-1], 0)
        gp.output(b[j], 1)
        sleep(0.1)