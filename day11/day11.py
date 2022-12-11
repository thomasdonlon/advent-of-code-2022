mod_list = [3, 13, 2, 11, 19, 17, 5, 7] #[23, 19, 13, 17] for testing data

#this only tracks the relevant modulo groups rather than enormous numbers
class mod_num:
	def __init__(self, n):
		self.mods = [n%m for m in mod_list]

	def add(self, n):
		self.mods = [(x+n)%m for x, m in zip(self.mods, mod_list)]
		return self #this returns for consistency with the non-mod behavior

	def mult(self, n):
		self.mods = [(x*n)%m for x, m in zip(self.mods, mod_list)]
		return self

	def square(self):
		self.mods = [(x**2)%m for x, m in zip(self.mods, mod_list)]
		return self

	def __eq__(self, item):
		return [m == item for m in self.mods]

	def __getitem__(self, i):
		return self.mods[i]

#this is short enough that we can hard-code the monkey list
class monkey():

	#this and set_monkeys have to be run before the monkey works
	def __init__(self, items, oper, inspect_oper, mod=False): #switch lets us work with easier non-modulo numbers for small inputs
		if mod:
			self.items = [mod_num(item) for item in items]
		else:
			self.items = items
		self.n_inspects = 0
		self.oper = oper
		self.inspect_oper = inspect_oper

	#can't be in init because you have to generate the first monkey somehow
	def set_monkeys(self, monkey_true, monkey_false):
		self.monkey_true = monkey_true
		self.monkey_false = monkey_false

	#monkey business
	def catch(self, item):
		self.items.append(item)

	def throw(self, monkey):
		item = self.items.pop(0)
		monkey.catch(item)

	def inspect(self):
		self.n_inspects += 1
		self.items[0] = self.oper(self.items[0])

		if self.inspect_oper(self.items[0]):
			self.throw(self.monkey_true)
		else:
			self.throw(self.monkey_false)

	def perform_round(self):
		for i in range(len(self.items)):
			self.inspect()

# #testing monkey dict
# monkeys = { 0 : monkey( [79, 98], 
# 	                    lambda x : (x * 19) // 3,
# 	                    lambda x : x % 23 == 0 ),
#             1 : monkey( [54, 65, 75, 74], 
# 	                    lambda x : (x + 6) // 3,
# 	                    lambda x : x % 19 == 0 ),
#             2 : monkey( [79, 60, 97], 
# 	                    lambda x : (x * x) // 3,
# 	                    lambda x : x % 13 == 0 ),
#             3 : monkey( [74], 
# 	                    lambda x : (x + 3) // 3,
# 	                    lambda x : x % 17 == 0 ),
#             }

# monkeys[0].set_monkeys(monkeys[2], monkeys[3])
# monkeys[1].set_monkeys(monkeys[2], monkeys[0])
# monkeys[2].set_monkeys(monkeys[1], monkeys[3])
# monkeys[3].set_monkeys(monkeys[0], monkeys[1])

#part 1 

#build monkey dict
monkeys = { 0 : monkey( [59, 65, 86, 56, 74, 57, 56], 
	                    lambda x : (x * 17) // 3,
	                    lambda x : x % 3 == 0 ),
            1 : monkey( [63, 83, 50, 63, 56], 
	                    lambda x : (x + 2) // 3,
	                    lambda x : x % 13 == 0 ),
            2 : monkey( [93, 79, 74, 55], 
	                    lambda x : (x + 1) // 3,
	                    lambda x : x % 2 == 0 ),
            3 : monkey( [86, 61, 67, 88, 94, 69, 56, 91], 
	                    lambda x : (x + 7) // 3,
	                    lambda x : x % 11 == 0 ),
            4 : monkey( [76, 50, 51], 
	                    lambda x : (x * x) // 3,
	                    lambda x : x % 19 == 0 ),
            5 : monkey( [77, 76], 
	                    lambda x : (x + 8) // 3,
	                    lambda x : x % 17 == 0 ),
            6 : monkey( [74], 
	                    lambda x : (x * 2) // 3,
	                    lambda x : x % 5 == 0 ),
            7 : monkey( [86, 85, 52, 86, 91, 95], 
	                    lambda x : (x + 6) // 3,
	                    lambda x : x % 7 == 0 ) 
            }

#set all the monkeys that each monkey throws to
monkeys[0].set_monkeys(monkeys[3], monkeys[6])
monkeys[1].set_monkeys(monkeys[3], monkeys[0])
monkeys[2].set_monkeys(monkeys[0], monkeys[1])
monkeys[3].set_monkeys(monkeys[6], monkeys[7])
monkeys[4].set_monkeys(monkeys[2], monkeys[5])
monkeys[5].set_monkeys(monkeys[2], monkeys[1])
monkeys[6].set_monkeys(monkeys[4], monkeys[7])
monkeys[7].set_monkeys(monkeys[4], monkeys[5])

#run simulation
for i in range(20):
	for j in range(len(monkeys.keys())):
		monkeys[j].perform_round()

#calculate monkey business
n_inspect_list = []
for j in range(len(monkeys.keys())):
	n_inspect_list.append(monkeys[j].n_inspects)

n_inspect_list.sort()
print(n_inspect_list[-1]*n_inspect_list[-2])

#part 2

#build monkey dict
monkeys = { 0 : monkey( [59, 65, 86, 56, 74, 57, 56], 
	                    lambda x : x.mult(17),
	                    lambda x : x[0] == 0,
	                    mod=True ),
            1 : monkey( [63, 83, 50, 63, 56], 
	                    lambda x : x.add(2),
	                    lambda x : x[1] == 0,
	                    mod=True ),
            2 : monkey( [93, 79, 74, 55], 
	                    lambda x : x.add(1),
	                    lambda x : x[2] == 0,
	                    mod=True ),
            3 : monkey( [86, 61, 67, 88, 94, 69, 56, 91], 
	                    lambda x : x.add(7),
	                    lambda x : x[3] == 0,
	                    mod=True ),
            4 : monkey( [76, 50, 51], 
	                    lambda x : x.square(),
	                    lambda x : x[4] == 0,
	                    mod=True ),
            5 : monkey( [77, 76], 
	                    lambda x : x.add(8),
	                    lambda x : x[5] == 0,
	                    mod=True ),
            6 : monkey( [74], 
	                    lambda x : x.mult(2),
	                    lambda x : x[6] == 0,
	                    mod=True ),
            7 : monkey( [86, 85, 52, 86, 91, 95], 
	                    lambda x : x.add(6),
	                    lambda x : x[7] == 0,
	                    mod=True )
            }

#set all the monkeys that each monkey throws to
monkeys[0].set_monkeys(monkeys[3], monkeys[6])
monkeys[1].set_monkeys(monkeys[3], monkeys[0])
monkeys[2].set_monkeys(monkeys[0], monkeys[1])
monkeys[3].set_monkeys(monkeys[6], monkeys[7])
monkeys[4].set_monkeys(monkeys[2], monkeys[5])
monkeys[5].set_monkeys(monkeys[2], monkeys[1])
monkeys[6].set_monkeys(monkeys[4], monkeys[7])
monkeys[7].set_monkeys(monkeys[4], monkeys[5])

# #testing monkey dict
# monkeys = { 0 : monkey( [79, 98], 
# 	                    lambda x : x.mult(19),
# 	                    lambda x : x[0] == 0,
# 	                    mod=True),
#             1 : monkey( [54, 65, 75, 74], 
# 	                    lambda x : x.add(6),
# 	                    lambda x : x[1] == 0,
# 	                    mod=True),
#             2 : monkey( [79, 60, 97], 
# 	                    lambda x : x.square(),
# 	                    lambda x : x[2] == 0,
# 	                    mod=True),
#             3 : monkey( [74], 
# 	                    lambda x : x.add(3),
# 	                    lambda x : x[3] == 0,
# 	                    mod=True),
#             }

# monkeys[0].set_monkeys(monkeys[2], monkeys[3])
# monkeys[1].set_monkeys(monkeys[2], monkeys[0])
# monkeys[2].set_monkeys(monkeys[1], monkeys[3])
# monkeys[3].set_monkeys(monkeys[0], monkeys[1])

#run simulation
for i in range(10000):
	for j in range(len(monkeys.keys())):
		monkeys[j].perform_round()

#calculate monkey business
n_inspect_list = []
for j in range(len(monkeys.keys())):
	n_inspect_list.append(monkeys[j].n_inspects)

n_inspect_list.sort()
print(n_inspect_list[-1]*n_inspect_list[-2])