import sys, os, json

with open('input', 'r') as f:
	raw_data = f.readlines()

# turns raw map data into a list of drawn ints, and a
# list of boards, each of which contain a list of column ints
def process_input(data):
	drawings = [ int(item) for item in data.pop(0).strip().split(',') ]
	
	i,x = 0,0
	boards = []
	for line in data:
		x = 0
		if line.strip(): # fill out the i-th 2D array
			bingo_line = [ int(item) for item in line.split() ]
			for x,val in enumerate(bingo_line):
				boards[i][x].append(val)
		else: # instantiate the next 2D array
			boards.append([])
			i = len(boards) - 1
			for temp in range(5):
				boards[i].append([])

	return drawings,boards

# takes a drawn number and marks every value that matches
# by changing it from an int to a float, then checks the boards
# to see if they have a winning row or column. if they have,
# returns the winning map.
def mark_boards(draw, boards):
	for i,board in enumerate(boards):
		for x,x_list in enumerate(boards[i]):
			for y,val in enumerate(boards[i][x]):
				if val == draw and type(val) == int:
					boards[i][x][y] = float(boards[i][x][y])
			# check columns
			y_check = True
			for val in boards[i][x]:
				if type(val) == int:
					y_check = False
					break
			if y_check:
				return True,i
		# check rows
		for y in range(len(boards[i])):
			x_check = True
			for x in boards[i]:
				if type(x[y]) == int:
					x_check = False
					break
			if x_check:
				return True,i

	return False,0

def mark_boards_2(draw, boards, mark):
	if mark:
		for i,board in enumerate(boards):
			for x,x_list in enumerate(boards[i]):
				for y,val in enumerate(boards[i][x]):
					if val == draw and type(val) == int:
						boards[i][x][y] = float(boards[i][x][y])
	for i,board in enumerate(boards):
		for x,x_list in enumerate(boards[i]):
			# check columns
			y_check = True
			for val in boards[i][x]:
				if type(val) == int:
					y_check = False
					break
			if y_check:
				return True,boards.pop(i)
		# check rows
		for y in range(len(boards[i])):
			x_check = True
			for x in boards[i]:
				if type(x[y]) == int:
					x_check = False
					break
			if x_check:
				return True,boards.pop(i)
	return False,None

drawings,boards = process_input(raw_data)

# Part 1
# for draw in drawings:
# 	finished,i = mark_boards(draw, boards)
# 	if finished:
# 		unmarked = 0
# 		for x in boards[i]:
# 			for val in x:
# 				if type(val) == int:
# 					unmarked += val
# 		score = unmarked * draw
# 		break
# 
# print (f'winning board below...\n{json.dumps(boards[i], indent=4)}\nscore = {score}')

# Part 2
score = 0
unmarked = 0
for draw in drawings:
	finished,board = mark_boards_2(draw, boards, True)
	if finished:
		last_winner = board
		last_draw = draw
		while finished and len(boards) > 1:
			finished,board = mark_boards_2(draw, boards, False)
			last_winner = board
			last_draw = draw

if not score:
	for x in last_winner:
		for val in x:
			if type(val) == int:
				unmarked += val
	score = unmarked * last_draw

print (f'winning board below...\n{json.dumps(last_winner, indent=4)}\nscore = {score}')
