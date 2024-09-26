import RPi.GPIO as gp

gp.setmode(gp.BCM)

gp.setup(24, gp.IN, pull_up_down=gp.PUD_DOWN)

print(gp.input(24))