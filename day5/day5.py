#set up crate array
def get_stacks(f, n_stacks=9):
	stacks = [list() for i in range(n_stacks)] #avoid aliasing

	line = f.readline()
	while line[1] != '1': #don't read in the numbers line
		line = line[1::4] #only grabs letters in the boxes
		for i, item in enumerate(line):
			if item != ' ':
				stacks[i].append(item)
		line = f.readline()

	#have to reverse every list to put in correct order
	for i in range(len(stacks)):
		stacks[i].reverse()

	return stacks

#part 1
with open('./input.txt', 'r') as f:
	stacks = get_stacks(f)

	#now read in all the instructions
	f.readline() #remove blank line

	for line in f:

		#parse each instruction
		line = line.split()
		n_move = int(line[1])
		mv_from = int(line[3])-1 #the -1 just corrects for indexing from 0
		mv_to = int(line[5])-1

		#then do all the actual moving
		for i in range(n_move):
			item = stacks[mv_from].pop()
			stacks[mv_to].append(item)

answer = ''
for item in stacks:
	answer += item[-1]
print(answer)

#part 2
with open('./input.txt', 'r') as f:
	stacks = get_stacks(f)

	#now read in all the instructions
	f.readline() #remove blank line

	for line in f:

		#parse each instruction
		line = line.split()
		n_move = int(line[1])
		mv_from = int(line[3])-1 #the -1 just corrects for indexing from 0
		mv_to = int(line[5])-1

		#then do all the actual moving
		item = stacks[mv_from][-n_move:]
		stacks[mv_from] = stacks[mv_from][:-n_move]
		stacks[mv_to] += item

answer = ''
for item in stacks:
	answer += item[-1]
print(answer)