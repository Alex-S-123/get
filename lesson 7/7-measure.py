import RPi.GPIO as gp
from time import sleep
import time

def adc_f(b):
    s = ""
    for i in range(8):
        gp.output(b[i], gp.HIGH)
        sleep(0.01)
        if gp.input(14):
            gp.output(b[i], gp.LOW)
            s = s+"0"
        else:
            s = s+"1"
    k = int(s, 2)
    return k/255*3.3


def led_s(k, a):
    k = k/3.3*7.1
    for j in range(8):
        gp.output(a[j], gp.LOW)
    for j in range(8):
        if k > j:
            gp.output(a[j], gp.HIGH)


try:
    gp.setmode(gp.BCM)
    fi = open("data.txt", 'w')
    se = open("settings.txt", 'w')
    data = []
    times = []
    count = 0
    b = [6, 12, 5, 0, 1, 7, 11, 8]
    a = [2, 3, 4, 17, 27, 22, 10, 9]
    b.reverse()
    for i in b:
        gp.setup(i, gp.OUT, initial=gp.LOW)
    gp.setup(13, gp.OUT)
    gp.setup(a, gp.OUT)
    gp.setup(14, gp.IN)
    print("charge")
    timeb = time.time_ns()
    gp.output(13, gp.HIGH)
    k = 0
    while k < 2.0:
        k = adc_f(b)
        data.append(k)
        times.append(time.time_ns()-timeb)
        count += 1
        print(k)
        led_s(k, a)
        for j in range(8):
            gp.output(b[j], gp.LOW)
        sleep(0.05)
    print("charge comleted")
    gp.output(13, gp.LOW)
    while k > 1.7:
        k = adc_f(b)
        data.append(k)
        times.append(time.time_ns()-timeb)
        count += 1
        print(k)
        led_s(k, a)
        for j in range(8):
            gp.output(b[j], gp.LOW)
        sleep(0.05)
    timeexp = time.time_ns()-timeb
    sleep(0.1)
    print("end")
    print(count)
    st = "time "+str(timeexp/10**9) +"\n"
    se.write(st)
    st = "period "+str(timeexp/count/10**9)+"\n"
    se.write(st)
    st = "freq "+str(count/timeexp*10**9)+"\n"
    se.write(st)
    se.write("quant 0.0129")
    se.close()
    for i in range(count):
        st = str(times[i]) + " " + str(data[i]) + "\n"
        fi.write(st)
    fi.close()

except Exception as ex:
    
    print(ex)
finally:
    for j in range(8):
        gp.output(b[j], gp.LOW)
        gp.output(a[j], gp.LOW)
    gp.cleanup()  