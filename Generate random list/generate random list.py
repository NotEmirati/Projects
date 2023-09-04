import random

random_list = []
for i in range(0,5):
	n = random.randint(1,30)
	random_list.append(n)
	print(random_list)

file = open('items.txt', 'w')
for item in random_list:
	file.write(str(item) + ' ')
file.close()

append_list = []
for i in range(0,5):
	p = random.randint(100,1000)
	append_list.append(p)
	print(append_list)

add_file = open('items.txt', 'a')
for i in append_list:
	add_file.write(str(i) + ' ')
add_file.close()
