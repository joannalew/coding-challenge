def answer(n):
    # convert string to int
    n = int(n)
    
    # some easy base cases
    table = [1, 0, 1, 2, 2]
    
    
    def getMoves(table, index):									# get number of moves for index = n; table with easy base cases
    	if (index < 5):											# if n is already in the table, return answer
    		return table[index]
    	
    	else:													# otherwise, recursively find answer
    		if (index % 2 == 0):								# if n is even, divide in half
    			return getMoves(table, index / 2) + 1
    		else:												# if n is odd, add 1 or subtract 1
    			left = index - 1								# depending on which neighbor is divisible by 4
    			right = index + 1
    			if (left % 4 == 0):
    				return getMoves(table, left / 2) + 2
    			else:
    				return getMoves(table, right / 2) + 2
    
    
    return getMoves(table, n)


