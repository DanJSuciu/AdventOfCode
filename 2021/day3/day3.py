import sys, os

with open('input', 'r') as f:
	raw_data = f.readlines()
	bits = len(raw_data[0].strip())

data = [ int(item.strip(), 2) for item in raw_data ]

# Part 1 
# bitcount = []
# for item in data:
# 	mask = 2048
# 	for i in range(bits):
# 		if item & mask:
# 			try:
# 				bitcount[i] += 1
# 			except IndexError:
# 				bitcount.append(1)
# 		else:
# 			try:
# 				bitcount[i]
# 			except IndexError:
# 				bitcount.append(0)
# 		mask >>= 1

# gamma = 0
# epsilon = 0
# mask = 2048
# for count in bitcount:
# 	if count >= (len(data)/2):
# 		gamma |= mask
# 	else:
# 		epsilon |= mask
# 	mask >>= 1

# print (f'gamma = {gamma}\nepsilon = {epsilon}\npower consumption = {gamma*epsilon}')

# Part 2
def filter_data(data, mask, mode):
	if len(data) == 1:
		return (data[0])
	else:
		pos_count = 0
		pos_data = []
		neg_data = []
		for item in data:
			if item & mask:
				pos_count += 1
				pos_data.append(item)
			else:
				neg_data.append(item)
		if pos_count >= (len(data)/2):
			if mode == 'oxygen':
				return(filter_data(pos_data, mask >> 1, mode))
			else:
				return(filter_data(neg_data, mask >> 1, mode))
		else:
			if mode == 'oxygen':
				return(filter_data(neg_data, mask >> 1, mode))
			else:
				return(filter_data(pos_data, mask >> 1, mode))


oxygen_rating = filter_data(data, 2048, 'oxygen')
co2_rating = filter_data(data, 2048, 'co2')

print (f'oxygen rating = {oxygen_rating}\nco2 rating = {co2_rating}\nlife support rating = {oxygen_rating*co2_rating}')

