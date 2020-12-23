with open("data/day1.txt", "r") as f:
    data = f.read().split("\n")
for i in range(len(data)):
    data[i] = int(data[i])
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        for k in range(j + 1, len(data)):
            if data[i] + data[j] + data[k] == 2020:
                print(data[i] * data[j] * data[k])
                break