file1 = open("data3.txt", "r")
lines = filter(None, (line.rstrip() for line in file1))

for line in lines:
    l = line.split()
    print(l[1], l[0], l[6])
