import matplotlib.pyplot as plt

file1 = open("benchmarking/worstpossible.kpi", "r")
file2 = open("benchmarking/firstfitrefined.kpi", "r")
file3 = open("benchmarking/firstfit.kpi", "r")
file4 = open("benchmarking/bestfit.kpi", "r")
file5 = open("benchmarking/worstfit.kpi", "r")
bins = []
sd = []


for line in file1:
    l = line.split()
    bins.append(float(l[0]))

plt.plot(bins, label="WorstPossible")
bins = []
for line in file2:
    l = line.split()
    bins.append(float(l[0]))

plt.plot(bins, label="FirstFitRefined")
bins = []
for line in file3:
    l = line.split()
    bins.append(float(l[0]))

plt.plot(bins, label="Firstfit")
bins = []
for line in file4:
    l = line.split()
    bins.append(float(l[0]))

plt.plot(bins, label="BestFit")
bins = []
for line in file5:
    l = line.split()
    bins.append(float(l[0]))

plt.plot(bins, label="Worstfit")
plt.legend(loc="upper right")
plt.show()
