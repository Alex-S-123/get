import RPi.GPIO as gp
import time


gp.setmode(gp.BCM)

for i in [2, 3, 4, 17, 27, 22, 10, 9]:
    gp.setup(i, gp.OUT, initial=gp.LOW)



a = [2, 3, 4, 17, 27, 22, 10, 9]
b = [21, 20, 26, 16, 19, 25, 23, 24]
for i in b:
    gp.setup(i, gp.IN, pull_up_down=gp.PUD_DOWN)
while True:
    for j in range(len(a)):
        if (gp.input(b[j])):
            gp.output(a[j], gp.LOW)
        else:
            gp.output(a[j], gp.HIGH)
    time.sleep(0.1)
gp.cleanup()


