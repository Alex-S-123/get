import RPi.GPIO as gp

gp.setmode(gp.BCM)
gp.setup(24, gp.OUT)
pwm = gp.PWM(24, 100)
pwm.start(10)

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
        if n > 100:
            print("out of range")
            break
        if n < 0:
            print("number < 0")
            break
        print(round(n/100*3.3, 3))
        pwm.ChangeDutyCycle(n)
        
finally:
    gp.output(24, gp.LOW)      
    gp.cleanup()  