#recursion bc why not I guess
def all_unique(string):
	if len(string) == 0:
		return True
	elif string[0] in string[1:]:
		return False
	else:
		return all_unique(string[1:])

#might as well make this all nice too
def find_first_unique(len_id):
	with open('./input.txt', 'r') as f:
		line = f.readline()

		i = len_id
		while i < len(line):
			if all_unique(line[i-len_id:i]):
				print(i)
				break
			i+= 1

#part 1
find_first_unique(4)

#part 2
find_first_unique(14)