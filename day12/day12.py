#this runs in AWFUL time but it gets the job done
#probably could have copied a version of A* off the internet but where's the fun in that

#read in data
grid = [] 
with open('./input.txt', 'r') as f:
	for line in f:
		grid.append([ord(char) for char in line.strip()])

#turn the E into a value higher than z so we can always move up in numerical value when hill-climbing
#same with S but to 0
starting_i = 0
starting_j = 0

for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == 69: #nice
			grid[i][j] = 123
		if grid[i][j] == 83:
			grid[i][j] = 96
			starting_i = i #because of course you don't always start in the top-left corner
			starting_j = j

def get_max_nodes(nodes):
	max_vals = []
	for node in nodes:
		vals = [grid[n[0]][n[1]] for n in node]
		max_vals.append(max(vals))
	return max(max_vals)

#part 1

#run A* 
#(or some variation of it anyways, I'm just coding it from memory)
steps = 0
nodes = [[(starting_i, starting_j)]] 
checked_nodes = set((starting_i, starting_j))
while get_max_nodes(nodes) < 123: #checks if any node has E in it
	new_nodes = []
	for node in nodes:
		#apologies for index hell
		if node[-1][0] > 0: #up
			if grid[node[-1][0]-1][node[-1][1]] - grid[node[-1][0]][node[-1][1]] <= 1: #can only move max 1 up at a time
				if (node[-1][0]-1,node[-1][1]) not in checked_nodes:
					new_nodes.append(node + [(node[-1][0]-1, node[-1][1])])
					checked_nodes.add((node[-1][0]-1,node[-1][1]))
		if node[-1][0] < len(grid)-1: #down
			if grid[node[-1][0]+1][node[-1][1]] - grid[node[-1][0]][node[-1][1]] <= 1:
				if (node[-1][0]+1,node[-1][1]) not in checked_nodes:
					new_nodes.append(node + [(node[-1][0]+1, node[-1][1])])
					checked_nodes.add((node[-1][0]+1,node[-1][1]))
		if node[-1][1] > 0: #left
			if grid[node[-1][0]][node[-1][1]-1] - grid[node[-1][0]][node[-1][1]] <= 1:
				if (node[-1][0],node[-1][1]-1) not in checked_nodes:
					new_nodes.append(node + [(node[-1][0], node[-1][1]-1)])
					checked_nodes.add((node[-1][0],node[-1][1]-1))
		if node[-1][1] < len(grid[0])-1: #right
			if grid[node[-1][0]][node[-1][1]+1] - grid[node[-1][0]][node[-1][1]] <= 1:
				if (node[-1][0],node[-1][1]+1) not in checked_nodes:
					new_nodes.append(node + [(node[-1][0], node[-1][1]+1)])
					checked_nodes.add((node[-1][0],node[-1][1]+1))
	#nodes = prune_nodes(new_nodes)
	nodes = new_nodes
	steps += 1 #yes you could also grab the max len of nodes but this is easier on my brain

print(steps)


#part 2

min_steps = steps

for starting_i in range(len(grid)):
	for starting_j in range(len(grid[starting_i])):
		if grid[starting_i][starting_j] == 97:

			#run A* 
			#(or some variation of it anyways, I'm just coding it from memory)
			steps = 0
			nodes = [[(starting_i, starting_j)]]
			checked_nodes = set((starting_i, starting_j))
			while len(nodes) > 0 and get_max_nodes(nodes) < 123: #checks if any node has E in it
				new_nodes = []
				for node in nodes:
					#apologies for index hell
					if node[-1][0] > 0: #up
						if grid[node[-1][0]-1][node[-1][1]] - grid[node[-1][0]][node[-1][1]] <= 1: #can only move max 1 up at a time
							if (node[-1][0]-1,node[-1][1]) not in checked_nodes:
								new_nodes.append(node + [(node[-1][0]-1, node[-1][1])])
								checked_nodes.add((node[-1][0]-1,node[-1][1]))
					if node[-1][0] < len(grid)-1: #down
						if grid[node[-1][0]+1][node[-1][1]] - grid[node[-1][0]][node[-1][1]] <= 1:
							if (node[-1][0]+1,node[-1][1]) not in checked_nodes:
								new_nodes.append(node + [(node[-1][0]+1, node[-1][1])])
								checked_nodes.add((node[-1][0]+1,node[-1][1]))
					if node[-1][1] > 0: #left
						if grid[node[-1][0]][node[-1][1]-1] - grid[node[-1][0]][node[-1][1]] <= 1:
							if (node[-1][0],node[-1][1]-1) not in checked_nodes:
								new_nodes.append(node + [(node[-1][0], node[-1][1]-1)])
								checked_nodes.add((node[-1][0],node[-1][1]-1))
					if node[-1][1] < len(grid[0])-1: #right
						if grid[node[-1][0]][node[-1][1]+1] - grid[node[-1][0]][node[-1][1]] <= 1:
							if (node[-1][0],node[-1][1]+1) not in checked_nodes:
								new_nodes.append(node + [(node[-1][0], node[-1][1]+1)])
								checked_nodes.add((node[-1][0],node[-1][1]+1))
				#nodes = prune_nodes(new_nodes)
				nodes = new_nodes
				steps += 1 #yes you could also grab the max len of nodes but this is easier on my brain

				if len(nodes) == 0: #path doesn't connect to finish
					steps = 999999 #this just avoids it being considered in the overall paths

			if steps < min_steps:
				min_steps = steps

print(min_steps)