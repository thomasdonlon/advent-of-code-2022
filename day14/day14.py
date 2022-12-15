input_fn = './input.txt'

#part 0
#scan the data and figure out what the min and max values that are present in the data 
#(we only need to include +/- 1 from those for x, and up to max in y)

min_x = 500
max_x = 500
max_y = 0
with open(input_fn, 'r') as f:
	for line in f:
		line = line.strip().split(' -> ')
		for pair in line:
			pair = pair.split(',')
			if int(pair[0]) < min_x:
				min_x = int(pair[0])
			elif int(pair[0]) > max_x:
				max_x = int(pair[0])
			if int(pair[1]) > max_y:
				max_y = int(pair[1])

#this makes sure that sand can fall off the sides
min_x -= 1 
max_x += 1 

#part 1

#construct the grid
grid = []
for i in range(max_x - min_x + 1): #accounts for 0 index
	tmp = []
	for j in range(max_y+1): #accounts for y = 0
		tmp.append(0)
	grid.append(tmp)

#place the rocks in the correct spots
with open(input_fn, 'r') as f:
	for line in f:
		line = line.strip().split(' -> ')

		for i in range(len(line)-1):

			x1 = int(line[i].split(',')[0])
			x2 = int(line[i+1].split(',')[0])
			y1 = int(line[i].split(',')[1])
			y2 = int(line[i+1].split(',')[1])

			if x1 == x2:
				j = min(y1, y2) #mins and maxes bc we have to account for lines in either direction
				while j <= max(y1, y2):
					grid[x1-min_x][j] = 1
					j += 1
			else: #y's have to be equal
				j = min(x1,x2)
				while j <= max(x1,x2):
					grid[j-min_x][y1] = 1
					j += 1

#start the sand falling 
fell_through = False
n_sands = 0
while not fell_through:

	#place a sand and let it fall
	at_rest = False
	sand = [500-min_x, 0]
	while not at_rest:
		if sand[1] >= max_y:
			fell_through = True
			break
		if not grid[sand[0]][sand[1]+1]:
			sand[1] += 1
		elif not grid[sand[0]-1][sand[1]+1]:
			sand[0] -=1
			sand[1] += 1
		elif not grid[sand[0]+1][sand[1]+1]:
			sand[0] += 1
			sand[1] += 1
		else:
			at_rest = True
	
	if not fell_through:
		n_sands += 1
		grid[sand[0]][sand[1]] = 1

print(n_sands)
	
#part 2

min_x = 300
max_x = 700 #this should be enough hopefully
#I don't want to implement dynamic resizing of the grid

#construct the grid
grid = []
for i in range(max_x - min_x + 1): #accounts for 0 index
	tmp = []
	for j in range(max_y+3): #accounts for y = 0
		tmp.append(0)
	grid.append(tmp)

#make the floor
for i in range(len(grid)):
	grid[i][-1] = 1

#place the rocks in the correct spots
with open(input_fn, 'r') as f:
	for line in f:
		line = line.strip().split(' -> ')

		for i in range(len(line)-1):

			x1 = int(line[i].split(',')[0])
			x2 = int(line[i+1].split(',')[0])
			y1 = int(line[i].split(',')[1])
			y2 = int(line[i+1].split(',')[1])

			if x1 == x2:
				j = min(y1, y2) #mins and maxes bc we have to account for lines in either direction
				while j <= max(y1, y2):
					grid[x1-min_x][j] = 1
					j += 1
			else: #y's have to be equal
				j = min(x1,x2)
				while j <= max(x1,x2):
					grid[j-min_x][y1] = 1
					j += 1
					
#start the sand falling 
done = False
n_sands = 0
while not done:

	#place a sand and let it fall
	at_rest = False
	sand = [500-min_x, 0]
	while not at_rest:
		#print(sand)
		if not grid[sand[0]][sand[1]+1]:
			sand[1] += 1
		elif not grid[sand[0]-1][sand[1]+1]:
			sand[0] -=1
			sand[1] += 1
		elif not grid[sand[0]+1][sand[1]+1]:
			sand[0] += 1
			sand[1] += 1
		else:
			at_rest = True
	
	if not (sand[1] == 0):
		n_sands += 1
		grid[sand[0]][sand[1]] = 1
	else:
		n_sands += 1
		done = True

print(n_sands)