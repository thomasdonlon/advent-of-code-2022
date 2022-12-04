#part 1

n_overlaps = 0

with open('./input.txt', 'r') as f:
	for line in f:
		line = line.strip().split(',')
		first = [int(x) for x in line[0].split('-')]
		second = [int(x) for x in line[1].split('-')]

		if (first[0] >= second[0] and first[1] <= second[1]) or (first[0] <= second[0] and first[1] >= second[1]):
			n_overlaps += 1

print(n_overlaps)

#part 2

n_overlaps = 0

with open('./input.txt', 'r') as f:
	for line in f:
		line = line.strip().split(',')
		first = [int(x) for x in line[0].split('-')]
		second = [int(x) for x in line[1].split('-')]

		#there's gotta be a more intelligent way to do this but whatever
		if (first[0] <= second[0] <= first[1]) or (first[0] <= second[1] <= first[1]) or \
		   (second[0] <= first[0] <= second[1]) or (second[0] <= first[1] <= second[1]):
			n_overlaps += 1

print(n_overlaps)