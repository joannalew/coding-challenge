def answer(M, F):
    M = int(M)
    F = int(F)
    
    count = 0      # number of steps to [1, 1]
    
    while (M != 1 or F != 1):
        # subtract out as many of the smaller one from bigger one as possible
        # increment count by 1
        # use division to speed up process
    	if (M < F):
    		divide = F / M
    		if (F % M == 0):
    			divide -= 1
    
    		F = F - (divide * M)
    		count += divide

    	if (F < M):
    		divide = M / F
    		if (M % F == 0):
    			divide -= 1
    
    		M = M - (divide * F)
    		count += divide
        
        # if they are ever equal, is impossible to complete (besides [1,1])
    	if (M == F and M != 1 and F != 1):
    		return "impossible"
    
    return str(count)






