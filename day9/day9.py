#record the positions of the head and the tail
H = [0, 0]
T = [0, 0]

#main loop that controls tail behavior
def update_tail(H, T):
	if max([abs(H[0] - T[0]),abs(H[1] - T[1])]) <= 1: #Hausdorff? distance is 1 or 0, do not update
		pass
	else:
		if abs(H[0] - T[0]) > 0: #update x position
			if H[0] > T[0]:
				T[0] += 1
			else:
				T[0] -= 1
		if abs(H[1] - T[1]) > 0: #update y position
			if H[1] > T[1]:
				T[1] += 1
			else:
				T[1] -= 1

#part 1
tail_pos = set() #track where the tail has been

with open('./input.txt', 'r') as f:
	for line in f:
		line = line.strip().split()
		#there's definitely a more intelligent way to do this loop 
		if line[0] == 'R':
			for i in range(int(line[1])):
				H[0] += 1
				update_tail(H, T)
				tail_pos.add(tuple(T))
		elif line[0] == 'L':
			for i in range(int(line[1])):
				H[0] -= 1
				update_tail(H, T)
				tail_pos.add(tuple(T))
		elif line[0] == 'U':
			for i in range(int(line[1])):
				H[1] += 1
				update_tail(H, T)
				tail_pos.add(tuple(T))
		else: #is D
			for i in range(int(line[1])):
				H[1] -= 1
				update_tail(H, T)
				tail_pos.add(tuple(T))

print(len(tail_pos))

#part 2
rope_len = 10
tail_pos = set() #track where the tail has been

#build un-aliased rope
rope = []
for i in range(rope_len):
	rope.append([0, 0])

#just update each "tail" for every segment
def update_rope(rope):
	i = 0
	while i < len(rope)-1:
		update_tail(rope[i], rope[i+1])
		i += 1

with open('./input.txt', 'r') as f:
	for line in f:
		line = line.strip().split()
		#there's definitely a more intelligent way to do this loop 
		if line[0] == 'R':
			for i in range(int(line[1])):
				rope[0][0] += 1
				update_rope(rope)
				tail_pos.add(tuple(rope[-1]))
		elif line[0] == 'L':
			for i in range(int(line[1])):
				rope[0][0] -= 1
				update_rope(rope)
				tail_pos.add(tuple(rope[-1]))
		elif line[0] == 'U':
			for i in range(int(line[1])):
				rope[0][1] += 1
				update_rope(rope)
				tail_pos.add(tuple(rope[-1]))
		else: #is D
			for i in range(int(line[1])):
				rope[0][1] -= 1
				update_rope(rope)
				tail_pos.add(tuple(rope[-1]))

print(len(tail_pos))


