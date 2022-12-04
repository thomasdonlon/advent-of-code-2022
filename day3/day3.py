import numpy as np #the allure was too strong

#part 1
sum_vals = 0

#turns a string into a list of numbers according to the format
def str_to_num_list(string):
	string = string.strip()
	vals = []
	for char in [*string]:
		if ord(char) - 96 < 0: #if less than 0, is uppercase
			vals.append(ord(char) - 64 + 26) #for uppercase, + 26 to go after the lowercase letters
		else:
			vals.append(ord(char) - 96) #for lowercase
	return np.array(vals)


with open('./input.txt', 'r') as f:

	for line in f:
		first = line[:len(line)//2]
		second = line[len(line)//2:]

		vals1 = str_to_num_list(first)
		vals2 = str_to_num_list(second)

		repeat = np.intersect1d(vals1, vals2)[0]

		sum_vals += repeat

print(sum_vals)

#part 2

sum_vals = 0

with open('./input.txt', 'r') as f:
	for line1 in f:
		line2 = f.readline()
		line3 = f.readline() #they all use the same iterator lol

		vals1 = str_to_num_list(line1.strip())
		vals2 = str_to_num_list(line2.strip())
		vals3 = str_to_num_list(line3.strip())

		repeat = np.intersect1d(np.intersect1d(vals1, vals2), vals3)[0] #nothing like the ol double np intersect

		sum_vals += repeat

print(sum_vals)
