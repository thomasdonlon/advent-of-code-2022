def compute(matchup_dict):

	tot_score = 0
	with open('./input.txt', 'r') as f:
		for line in f:
			first, second = line.strip().split()

			#assign points for the matchup + what we threw
			tot_score += matchup_dict[first + second]

	print(tot_score)

#part 1

#pre-calculated, maybe there's a more clever way to do this but eh
matchup_dict = {
				'AX':3+1,
				'AY':6+2,
				'AZ':0+3,
				'BX':0+1,
				'BY':3+2,
				'BZ':6+3,
				'CX':6+1,
				'CY':0+2,
				'CZ':3+3
               }

compute(matchup_dict)

#part 2

#same philosophy as before
matchup_dict = {
				'AX':3,
				'AY':1+3,
				'AZ':2+6,
				'BX':1,
				'BY':2+3,
				'BZ':3+6,
				'CX':2,
				'CY':3+3,
				'CZ':1+6
               }

compute(matchup_dict)