import numpy as np #gotta do it

#the y and x variables seem flipped bc we're doing array math rather than cartesian math
#but it's all arbitrary

#build the grid
grid = []
with open('./input.txt', 'r') as f:
	for line in f:
		line = [int(i) for i in line.strip()]
		grid.append(line)

grid = np.array(grid) #this makes it so much easier

#part 1
def is_visible(x, y, grid):
	if x == 0 or x == len(grid[y]) or y == 0 or y == len(grid): #check if tree is on boundary
		return 1
	else: #if not, check each line in the grid
		if np.all(grid[y, x] > grid[y, :x]) or np.all(grid[y, x] > grid[y, x+1:]) or np.all(grid[y, x] > grid[:y, x]) or np.all(grid[y, x] > grid[y+1:, x]):
			return 1
		else:
			return 0

num_vis = 0
for y in range(len(grid)):
	for x in range(len(grid[y])):
		num_vis += is_visible(x, y, grid)

print(num_vis)

#part 2

#helper function to find continuous number of trees with heights less than the given value
def cont_lt(arr, n): 
	if len(arr) == 0:
		return 0
	n_lt = 1
	i = 0
	while i < len(arr) - 1 and arr[i] < n:
		n_lt += 1
		i += 1
	return n_lt

def scenic_score(x, y, grid):
	n = grid[y, x]
	return cont_lt(np.flip(grid[y, :x]), n) * cont_lt(grid[y, x+1:], n) * cont_lt(np.flip(grid[:y, x]), n) * cont_lt(grid[y+1:, x], n)

best_ss = 0
for y in range(len(grid)):
	for x in range(len(grid[y])):
		ss = scenic_score(x, y, grid.copy())
		if ss > best_ss:
			best_ss = ss

print(best_ss)
