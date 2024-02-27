import random

list = []
for i in range(101):
    list.append(0)


for i in range(100000000):
    j = 0
    while j <= 100:
        temp = list[j]
        list[j] = temp + 1
        num = random.randint(1,20)
        j += num


for l in range(101):
    print(str(l) + ": " + str(list[l]) + " " + str(list[l]/list[0]*100) + "%")





