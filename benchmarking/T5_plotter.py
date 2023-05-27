import matplotlib.pyplot as plt

file = open("DataT3refined.txt", "r")
i = 0
times = []
times1 = []
times2 = []
times3 = []
times4 = []
times5 = []
for line in file:

    l = line.split()
    times.append(float(l[2]))

for i in range(40):
    if i < 20:
        times1.append(times[i])
    # elif i < 40:
    #     times2.append(times[i])
    # elif i < 60:
    #     times3.append(times[i])
    # elif i < 80:
    #     times4.append(times[i])
    else:
        times2.append(times[i])

plt.plot(times1, label="MinBin")
plt.plot(times2, label="BaseLine")

plt.legend(loc="upper right")
plt.show()
