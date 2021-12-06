import sys, os

with open('input', 'r') as f:
	data = f.readlines()

x = 0
y = 0

# Part 1
# for item in data:
# 	head = item.split()[0]
# 	dist = int(item.split()[1])
# 	if head == 'forward':
# 		x += dist
# 	elif head == 'up':
# 		y -= dist
# 	elif head == 'down':
# 		y += dist

# Part 2
aim = 0
for item in data:
	head = item.split()[0]
	dist = int(item.split()[1])
	if head == 'forward':
		x += dist
		y += dist*aim
	elif head == 'up':
		aim -= dist
	elif head == 'down':
		aim += dist

print(f'final coordinates: {x},{y}\nresult: {x*y}')