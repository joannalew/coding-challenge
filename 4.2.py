from fractions import gcd

def isBad (num):
    testnum = 4
    while testnum < num:
        testnum *= 2
    return testnum == num

def check_inf(num1, num2):
    if num1 == num2:
        return False

    divide = gcd(num1, num2)
    num1 /= divide
    num2 /= divide
    return not isBad(num1 + num2)

def count_list(slist):
    counts = dict()
    for x in slist:
        for y in x:
            if y not in counts:
                counts[y] = 1
            else:
                counts[y] += 1
    return counts

def elim_tuples1(slist, num):
    lsize = len(slist)
    tups = []

    for i in range(lsize - 1, -1, -1):
        if num in slist[i]:
            if (slist[i][0] != num):
                tups.append(slist[i][0])
            else:
                tups.append(slist[i][1])
            del slist[i]

    return tups

def elim_tuples2(slist, num):
    lsize = len(slist)
    for i in range(lsize - 1, -1, -1):
        if num in slist[i]:
            del slist[i]

def answer(banana_list):
    res_list = []                           # infinite banana guards
    lsize = len(banana_list)                # number of guards
    banana_list.sort()                      # maybe not necessary?

    # put valid pairs in res_list
    for i in range(lsize):
        for j in range(i, lsize):
            if (check_inf(banana_list[i], banana_list[j])):
                res_list.append((banana_list[i], banana_list[j]))

    # pair them up until no valid pairs
    while (res_list):
        print res_list
        counts = count_list(res_list)               # get the number of pairs each gorilla has
        mintup = min(counts, key=counts.get)        # key with min value (gorilla with least pairs)
        minparts = elim_tuples1(res_list, mintup)   # list of gorilla's valid partners

        smallpart = 999999                          # some huge number of connections to compare

        for i in minparts:                          # find the partner with least # of connections
            if counts[i] < smallpart:
                smallpart = counts[i]
                partner = i

        elim_tuples2(res_list, i)                   # eliminate gorilla and partner
        print res_list
        lsize -= 2
    
    return lsize


#banana_list = [1, 1]
#banana_list = [1, 7, 3, 21, 13, 19]
banana_list = [1, 2, 1, 7, 3, 21, 13, 19]

print answer(banana_list)

