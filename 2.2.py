
#l = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
#l = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
part = []
tot = []

# break list of strings into list of list: 
# ['1.0', '2.1.1', ...] --> [[1, 0], [2, 1, 1], ...]
for x in l:
	# find all positions of '.'
	c = '.'
	foo = ([pos for pos, char in enumerate(x) if char == c])

	# break into lists: 1.2.1 --> [1, 2, 1]
	old = 0;
	for s in foo:
		part.append(int(x[old:s]))
		old = s + 1
	part.append(int(x[old:]))

	# make all same size: [2] --> [2, -1, -1]
	while (len(part) < 3):
		part.append(-1)

	# keep in 'tot' as list of list: [[1, -1, -1], [2, 0, 3], ...]
	tot.append(part)
	part = []

# sort by tertiary, then secondary, then primary
def getKey0(item):
	return item[0]

def getKey1(item):
	return item[1]

def getKey2(item):
	return item[2]

tot = sorted(tot, key=getKey2)
tot = sorted(tot, key=getKey1)
tot = sorted(tot, key=getKey0)

# convert list back to string: [1, 0, -1] --> '1.0'
def getString(numList):
	res = str(numList[0])
	if (numList[1] != -1):
		res = res + '.' + str(numList[1])
	if (numList[2] != -1):
		res = res + '.' + str(numList[2])

	return res

for x in tot:
	part.append(getString(x))

return part





	




