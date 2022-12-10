#i'm being naughty here and using globals

with open('./input.txt', 'r') as f:
	lines = f.readlines()

X = 1
cycle = 1
important_cycles = [20, 60, 100, 140, 180, 220]
important_X_sum = 0
CRT = ''

def is_pixel_on():
	global CRT
	if abs(X-((cycle-1)%40)) <= 1: #a bit of a mess but it finds the X position of the CRT correctly
		CRT += '#'
	else:
		CRT += '.'
	if cycle%40 == 0: 
		CRT += '\n'

def check_cycle():
	global important_X_sum
	is_pixel_on()
	if cycle in important_cycles:
		important_X_sum += X*cycle

i = 0
while i < len(lines):
	check_cycle()
	if lines[i].strip() == 'noop':
		cycle += 1
		i += 1
	else:
		cycle += 1
		check_cycle()
		cycle += 1
		X += int(lines[i].strip().split()[-1])
		i += 1

#part 1
print(important_X_sum)

#part 2
print(CRT.strip()) #silly 