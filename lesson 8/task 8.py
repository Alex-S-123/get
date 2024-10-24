import matplotlib.pyplot as plt


f = open("data.txt")
#s = open("settings.txt")
#a, b = s.readline().split()
#ti = float(b)
#a, b = s.readline().split()
#count = int(ti//float(a))
count = 9
values = []
times = []
ma = 0
mat = 0
for i in range(count):
    a, b = map(float, f.readline().split())
    if b > ma:
        ma = b
        mat = a
    values.append(b)
    times.append(a)
plt.plot(times, values, marker='.', color="blue")
plt.title("Процесс заряда и разряда конденсатора в RC-цепочке")
plt.xlabel("Время, с")
plt.ylabel("Напряжение, В")
plt.minorticks_on()
plt.legend(["V(t)"])
plt.text(0.6*times[-1], 0.65*ma, "Время заряда = "+ str(mat))
plt.text(0.6*times[-1], 0.5*ma, "Время заряда = "+ str(times[-1]-mat))
plt.grid(which='major', color='#696969')
plt.grid(which='minor', alpha=0.75)
plt.savefig("output.svg")
f.close()
#s.close()
plt.show()

