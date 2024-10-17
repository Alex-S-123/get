import matplotlib.pyplot as plt

f = open("data.txt")
count = 93
a = []
b = []
for i in range(count):
    a1, b1 = f.readline().split()
    a.append(int(a1))
    b.append(float(b1))
plt.plot(a, b)
plt.show()