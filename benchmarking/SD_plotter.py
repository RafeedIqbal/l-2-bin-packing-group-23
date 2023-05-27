import matplotlib.pyplot as plt

file1 = open("constantbaseline.kpi", "r")
file2 = open("minbin.kpi", "r")

bins = []
sd = []


for line in file1:
    l = line.split()
    bins.append(float(l[1]))
print(bins)
plt.plot(bins, label="ConstantBaseline")
bins = []
for line in file2:
    l = line.split()
    bins.append(float(l[1]))
print(bins)
plt.plot(bins, label="MinBin")

plt.legend(loc="upper right")
plt.show()
