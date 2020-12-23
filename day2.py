with open("data/day2.txt", "r") as f:
    data = f.read().split("\n")

acc = 0
for put in data:
    conditional, password = put.split(": ")
    letter = conditional[-1]
    ranger = conditional.split(" ")[0]
    start, stop = ranger.split("-")
    start = int(start) - 1
    stop = int(stop) - 1
    num = password.count(letter)
    if (password[start] == letter) != (password[stop] == letter):
        acc += 1

print(acc)
