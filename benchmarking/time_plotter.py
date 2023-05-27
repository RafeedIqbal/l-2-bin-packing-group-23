import matplotlib.pyplot as plt

file = open("DataT2refined.txt", "r")
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

for i in range(100):
    if i < 20:
        times1.append(times[i])
    elif i < 40:
        times2.append(times[i])
    elif i < 60:
        times3.append(times[i])
    elif i < 80:
        times4.append(times[i])
    else:
        times5.append(times[i])

plt.plot(times1, label="WorstPossible")
plt.plot(times2, label="FirstFit")
plt.plot(times3, label="BestFit")
plt.plot(times4, label="WorstFit")
plt.plot(times5, label="FirstFitRefined")

plt.legend(loc="upper right")
plt.show()
