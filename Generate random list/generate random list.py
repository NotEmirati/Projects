import random

randomlist = []
for i in range(0,5):
    n = random.randint(1,30)
    randomlist.append(n)
print(randomlist)
save = open("random_list.txt", "w")
save.writelines(str(randomlist))
save.close()

appendlist = []
for i in range(0,5):
    p = random.randint(100,1000)
    appendlist.append(p)
print(appendlist)
save = open('random_list.txt', 'a')
save.writelines(str(appendlist))
save.close()
