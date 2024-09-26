import RPi.GPIO as gp

gp.setmode(gp.BCM)
b = [6, 12, 5, 0, 1, 7, 11, 8]

for i in b:
    gp.setup(i, gp.OUT, initial=gp.LOW)
b.reverse()
try:
    while True:
        n = input()
        if n == 'q':
            break
        try:
            n = int(n)
        except Exception as e:
            print("not a number", e)
            break
        if n > 255:
            print("out of range")
            break
        if n < 0:
            print("number < 0")
            break
        print(round(n/255*3.3, 3))
        s = bin(n)[2:]
        print(s)
        for j in range(8):
            gp.output(b[j], gp.LOW)
        while len(s) < 8:
            s = "0" + s
        for j in range(8):
            if s[j] == "1":
                gp.output(b[j], gp.HIGH)
finally:
    for i in b:
        gp.output(i, gp.LOW)      
    gp.cleanup()  