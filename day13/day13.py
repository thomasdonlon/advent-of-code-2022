with open('./input.txt', 'r') as f:
	lines = f.readlines()

#parsing
#this is a massive pain
#-----------------------------------
def find_bracket(line):
	level = 0
	for i in range(len(line)):
		if line[i] == '[':
			level += 1
		if line[i] == ']':
			if level == 1:
				return i 
			else:
				level -= 1

#recursive
def parse_line(line):
	out_list = []
	line = line[1:-1]

	i = 0
	while i < len(line):
		if line[i] == ',':
			i += 1
		elif line[i] == '[':
			endpoint = find_bracket(line[i:])
			out_list.append(parse_line(line[i:i+endpoint+1]))
			i += endpoint+1
		else: #is an int of some length
			try:
				endpoint = line[i:].index(',')
			except ValueError: #end of line
				endpoint = len(line)
			out_list.append(int(line[i:i+endpoint]))
			i += endpoint+1
	
	return out_list
#-----------------------------------

def in_order(pair):

	for i, j in zip(pair[0], pair[1]):

		#if both ints, actually compare
		if type(i) is int and type(j) is int:
			if i < j:
				return True
			elif i > j:
				return False
			else: 
				continue

		#otherwise, make sure i and j are lists
		else:
			if type(i) is int:
				left = [i]
			else:
				left = i
			if type(j) is int:
				right = [j]
			else:
				right = j

			#then compare
			tmp = in_order([left, right])
			if tmp is not None:
				return tmp

	#ran out of items in one of the lists
	if len(pair[0]) < len(pair[1]):
		return True
	elif len(pair[0]) > len(pair[1]):
		return False


#part 1

#gather the data into a single list
all_pairs = []
i = 0
while i < len(lines):
	left = parse_line(lines[i].strip())
	right = parse_line(lines[i+1].strip())
	all_pairs.append([left, right])

	i += 3

order_inds = []
for i, pair in enumerate(all_pairs):
	if in_order(pair):
		order_inds.append(i+1)

print(sum(order_inds))

#part 2

packets = []
for line in lines:
	if line != '\n':
		packets.append(parse_line(line.strip()))

#add in divider packets
packets.append([[2]])
packets.append([[6]])

#sort packets (insert sort)
ordered_packets = [packets[0]]
for packet in packets[1:]:
	i = 0
	while i < len(ordered_packets):
		if in_order([packet, ordered_packets[i]]):
			ordered_packets.insert(i, packet)
			break
		i += 1
	if i == len(ordered_packets):
		ordered_packets.append(packet)

index1 = ordered_packets.index([[2]])
index2 = ordered_packets.index([[6]])

print((index1+1)*(index2+1))
