#alright it's big brain time
class directory:

	def __init__(self, name, parent):
		self.name = name #should be a string
		self.parent = parent #should also be a directory, or None
		self.children = {} #a dict of directories
		self.files = [] #only store the sizes (ints)

	def add_child(self, child):
		self.children[child.name] = child

	def add_file(self, file):
		self.files.append(file)
	
	def children_names(self):
		alos = []
		for i in self.children.values():
			alos.append(i.name)
		return alos

	#not going to keep the sizes auto updated because fuck that
	#even though it would make sense to in a prod setting
	def files_size(self): #just size of files in this directory
		size = 0
		for i in self.files:
			size += i
		return size

	def total_size(self): #size of files + children
		size = self.files_size()
		for i in self.children.values():
			size += i.total_size()
		return size

	def print_tree(self, pad=''): #this is just for debugging
		print(pad + self.name + ' ' + str(self.total_size()))
		for i in self.children.values():
			i.print_tree(pad=pad + ' ')

	def sum_sizes_ltn(self, n): #sum all directory sizes below this one with size n or less (can include files multiple times)
		sum_sizes = 0
		for child in self.children.values():
			dsize = child.total_size() #just so it only calculates once in case it takes a long time
			if dsize <= n:
				sum_sizes += dsize
			sum_sizes += child.sum_sizes_ltn(n)
		return sum_sizes

	def smallest_dir_to_delete(self, dsn): #get smallest directory greater than some value
		sdtd_size = self.total_size()
		for child in self.children.values(): #check all the children
			child_dtd_size = child.smallest_dir_to_delete(dsn)
			if dsn < child_dtd_size < sdtd_size:
				sdtd_size = child_dtd_size
		return sdtd_size


#build the directory tree
home_dir = directory('/', None)
active_dir = home_dir

with open('./input.txt', 'r') as f:
	for line in f:
		line = line.strip()
		if line[0] == '$': #couldn't quickly think of a better way to do this
			if line == '$ cd /':
				active_dir = home_dir
			elif line == '$ cd ..':
				active_dir = active_dir.parent
			elif line[:4] == '$ cd':
				if line.split()[-1] in active_dir.children_names(): #directory already exists, so just move into it (just in case it goes into the same directory more than once)
					active_dir = active_dir[line.split()[-1]]
				else: #otherwise have to make the directory
					new_dir = directory(line.split()[-1], active_dir)
					active_dir.add_child(new_dir)
					active_dir = new_dir
			elif line == '$ ls': #can just skip this
				continue
		else:
			if line.split()[0] == 'dir': #directories are all made when you cd into them
				continue
			else: #is a file
				active_dir.add_file(int(line.split()[0]))

#part 1
print(home_dir.sum_sizes_ltn(100000))
#home_dir.print_tree() #debugging

#part 2
total_size = 70000000
unused_space_needed = 30000000
deleted_space_needed = unused_space_needed - total_size + home_dir.total_size()

print(home_dir.smallest_dir_to_delete(deleted_space_needed))