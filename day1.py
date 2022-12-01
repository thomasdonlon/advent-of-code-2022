filename = '/home/donlon/Desktop/code/advent-of-code-2022/day1_input.txt'

cal_list = []
cal = 0
with open(filename, 'r') as f:
	for line in f:
		if line != '\n':
			cal += int(line)
		else:
			cal_list.append(cal)
			cal = 0

#part 1
print(max(cal_list))

#part 2
cal_list.sort()
print(cal_list[-1] + cal_list[-2] + cal_list[-3])