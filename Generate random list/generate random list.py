import random

randomlist = []
for i in range(0,5):
    n = random.randint(1,30)
    randomlist.append(n)
print(randomlist)
save = open("random_list.txt", "x")

