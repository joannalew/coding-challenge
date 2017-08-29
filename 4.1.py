import itertools

# create powerset [1, 2, 3] --> [[1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
# taken from: https://stackoverflow.com/questions/1482308/whats-a-good-way-to-combinate-through-a-set
def powerset(s):
	x = len(s)
	masks = [1 << i for i in range(x)]
	for i in range(1 << x):
		yield [ss for mask, ss in zip(masks, s) if i & mask]


#floyd's algorithm: shortest path between all pairs of vertices (neg allowed)
#taken from: https://www.youtube.com/watch?v=4OQeCuLYj-4
def floyd(times):
	v = len(times)

	for k in range(v):
		for i in range(v):
			for j in range(v):
				if times[i][k] + times[k][j] < times[i][j]:
					times[i][j] = times[i][k] + times[k][j]

	return times

# save as many bunnies as possible w/in time limit
def get_opt_buns(floyd, time_limit):
	num_buns = len(floyd) - 2						# num_buns = total number of bunnies
	bun_ids = [x for x in range(num_buns)]			# bun_ids = [0, ..., total number of bunnies - 1]
	
	pset = powerset(bun_ids)						# get every combination of bunnies
	pset = sorted(pset)								# sort them so results return small index if size equal

	m_size = len(floyd)								# size of times matrix
	opt_buns = []

	for ss in pset:									# for every combination
		for p in itertools.permutations(ss):		# get permutation since len(ab) != len(ba)
			time = 0
			start = 0
			curr = m_size - 1

			for bunny in p:
				curr = bunny + 1					# convert bunny ID to matrix index
				time += floyd[start][curr]			# add path length to running total
				start = curr						# update current position

			time += floyd[start][m_size - 1]

			if time <= time_limit and len(ss) > len(opt_buns):
				opt_buns = ss
				if len(opt_buns) == num_buns:		# if got all bunnies, stop checking other paths
					break

	return opt_buns


def answer(times, time_limit):
	m_size = len(times)

	# no bunnies
	if (m_size < 3):
		return []

	# do floyd's alg on times
	times = floyd(times)

	# if path from a --> a is neg, there's a inf neg loop
	for x in range(m_size):
		if times[x][x] < 0:
			return [x for x in range(m_size - 2)]

	return get_opt_buns(times, time_limit)







#test case 1: [0, 1]		(default)
#times = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]
#time_limit = 3

#test case 2: [1, 2]   		(default)
times = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
time_limit = 1

#test case 3: [0, 1, 2]		(inf neg cycle)
#times = [[0, 2, 2, 2, -1], [9, 0, 2, 2, 0], [9, 3, 0, 2, 0], [9, 3, 2, 0, 0], [-1, 3, 2, 2, 0]]
#times = [[0, 1, 1, 1], [1, 0, 1, -1], [1, -1, 0, 1], [1, 1, -1, 0]]
#times = [[0, 1, 1, 1, 1, 1, -1], [1, 0, 1, 1, 1, -1, 1], [1, 1, 0, 1, -1, 1, 1], [-1, 1, 1, 0, 1, 1, 1], [1, 1, 1, -1, 0, 1, 1], [1, 1, -1, 1, 1, 0, 1], [1, -1, 1, 1, 1, 1, 0]]
#time_limit = -1

#test case 4: []			(max bunnies; none rescuable)
#times = [[0, 1, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 0]]
#time_limit = 1

#test case 5: [0]			(one bunny)
#times = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
#time_limit = 2

#test case 6: [0, 1] 		(mult revisits)
#times = [[0, 5, 11, 11, 1], [10, 0, 1, 5, 1], [10, 1, 0, 4, 0], [10, 1, 5, 0, 1], [10, 10, 10, 10, 0]]
#time_limit = 10

#test case 7: [0, 1]		(mult revisits 2)
#times = [[0, 10, 10, 10, 1], [0, 0, 10, 10, 10], [0, 10, 0, 10, 10], [0, 10, 10, 0, 10], [1, 1, 1, 1, 0]]
#time_limit = 5

#test case 8: [0, 1, 2]		(no time req)
#times = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
#time_limit = 0

#test case 9: []			(no bunnies)
#times = [[0, 2], [2, 0]]
#time_limit = 1

#test case 10: [0, 1, 2]	(backwards path)
#times = [[0, 10, 10, 1, 10], [10, 0, 10, 10, 1], [10, 1, 0, 10, 10], [10, 10, 1, 0, 10], [1, 10, 10, 10, 0]]
#time_limit = 6

print answer(times, time_limit)










	

