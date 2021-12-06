import sys, os

with open('input', 'r') as f:
	data = f.readlines()

count = 0
length = len(data)

# Part 1
# last = 0
# for item in data:
# 	if last:
# 		if int(item) > last:
# 			count += 1
# 	last = int(item)

# Part 2
window1 = 0
window2 = 0
for i in range(length):
	if i < 3:
		continue
	else:
		window1 = int(data[i-3]) + int(data[i-2]) + int(data[i-1])
		window2 = int(data[i-2]) + int(data[i-1]) + int(data[i])
		if window1 < window2:
			count += 1

print(count)