#this runs in absolutely horrendous time fyi

#there is zero chance this is the fastest way to do this but at least
#it's more intelligent than just scanning over a grid

check_row = 2000000 #10 for test input

def mh_dist(point1, point2):
	return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

#might be overkill but it was the first thing that came to mind
class SB: #sensor/beacon pair

	def __init__(self, sensor, beacon):
		#sensor and beacon are both tuples
		self.sensor = sensor
		self.beacon = beacon
		self.no_beacon_dist = mh_dist(self.sensor, self.beacon)

def beacon_is_allowed(SB, point):
	if mh_dist(SB.sensor, point) <= SB.no_beacon_dist:
		return 0
	return 1

def disallowed_tiles(SB, row):
	tile_set = set()

	i = SB.sensor[0] - SB.no_beacon_dist
	while i < SB.sensor[0] + SB.no_beacon_dist:
		if not beacon_is_allowed(SB, (i, row)):
			tile_set.add(i)	
		i += 1

	return tile_set

#part 1

#read in data
SB_list = []

with open('./input.txt', 'r') as f:
	for line in f:
		line = line.strip().split() #parsing the line is annoying
		sensor_x = int(line[2].lstrip('x=').rstrip(','))
		sensor_y = int(line[3].lstrip('y=').rstrip(':'))
		beacon_x = int(line[8].lstrip('x=').rstrip(','))
		beacon_y = int(line[9].lstrip('y='))
		SB_list.append(SB((sensor_x, sensor_y), (beacon_x, beacon_y)))

#compute all of the tiles that are not allowed
all_disallowed_tiles = set()
for SB in SB_list:
	tile_set = disallowed_tiles(SB, check_row)
	all_disallowed_tiles = all_disallowed_tiles.union(tile_set)

#subtract the number of beacons in the row
n_beacons = 0
beacon_set = set()
for SB in SB_list:
	beacon_set.add(SB.beacon)

for b in beacon_set:
	if b[1] == check_row:
		n_beacons += 1

print(len(all_disallowed_tiles) - n_beacons)

#part 2
#this part does scan over a grid. In only one direction at least.

minval = 0
maxval = 4000000 #20 for test input 

def range_disallowed(SB, row):
	min_x = SB.sensor[0] - (SB.no_beacon_dist - abs(SB.sensor[1] - row))
	max_x = SB.sensor[0] + (SB.no_beacon_dist - abs(SB.sensor[1] - row))
	if min_x < max_x:
		return [min_x, max_x]
	return None

#connects ranges into the smallest number of ranges possible
#(it actually only does this for the first one: it would need to be run recursively for the "correct" functionality)
#we get away with it here because only 1 position will be not in the range
def spanned_range(ranges):

	cr = ranges.copy()
	did_compress = True

	while len(ranges) > 1 and did_compress:
		did_compress = False

		i = 1
		while not did_compress and i < len(cr):
			if not (cr[i][0] > cr[0][1] + 1 or cr[i][1] < cr[0][0] - 1): #there is overlap
				c = cr.pop(i)
				cr[0][0] = min([cr[0][0], c[0]])
				cr[0][1] = max([cr[0][1], c[1]])
				did_compress = True
			i += 1

	return cr

for row in range(maxval):
	minx = minval
	maxx = maxval
	ranges = []
	for SB in SB_list:
		ranges.append(range_disallowed(SB, row))

	#remove Nones from ranges
	ranges = [x for x in ranges if x is not None]

	#print(ranges)
	sr = spanned_range(ranges)
	if len(sr) > 1:
		sr = [sr[0]] + spanned_range(sr[1:]) #guaranteed to compress down to two ranges
		missing_position = (min([sr[0][1], sr[1][1]])+1, row)

print(missing_position[0]*4000000 + missing_position[1])