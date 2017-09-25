from fractions import gcd


# if it's a "funky" number, it won't cycle
# funky numbers are numbers that double --> 1, 2, 4, 8, 16, 32, ...
def isBad (num):
    testnum = 4
    while testnum < num:
        testnum *= 2
    return testnum == num

# there'll be a cycle if reduced num1 + num2 != a "funky" number
def check_inf(num1, num2):
    if num1 == num2:
        return False

    divide = gcd(num1, num2)
    num1 /= divide
    num2 /= divide
    return not isBad(num1 + num2)

# get the number of monkeys with same banana count
# returned as dict
def get_count(slist):
    count = dict()

    for x in slist:
        if x not in count:
            count[x] = 1
        else:
            count[x] += 1

    return count

# put the valid banana count pairs as a dict
def get_partners(slist):
    partners = dict()

    for x in slist:
        if x[0] not in partners:
            partners[x[0]] = [x[1]]
        elif x[1] not in partners[x[0]]:
            partners[x[0]].append(x[1])
        if x[1] not in partners:
            partners[x[1]] = [x[0]]
        elif x[0] not in partners[x[1]]:
            partners[x[1]].append(x[0])

    return partners

# get key with the shortest array
# (the banana count with least number of partners for infinite cycle)
def get_min(sdict):
    min_length = 999

    for key in sdict:
        if len(sdict[key]) < min_length:
            min_length = len(sdict[key])
            min_partner = key

    return min_partner

# get key of partner (of get_min) with the shortest array
def get_min_partners(sdict, slist):
    min_length = 999

    for x in slist:
        if len(sdict[x]) < min_length:
            min_length = len(sdict[x])
            partner = x

    return partner

# remove banana count from dict
def eliminate(sdict, skey):
    sdict.pop(skey, None)           # remove banana count as a key
    for key in sdict:               # remove banana count as value from each key
        try:
            sdict[key].remove(skey)
        except ValueError:
            pass

    for k in sdict.keys():          # if partner list is empty, remove from dict
        if len(sdict[k]) == 0:
            sdict.pop(k, None)


def answer(banana_list):
    res_list = []                           # store valid pairs in this list

    counts = get_count(banana_list)         # number of monkeys w/ same number of bananas

    banana_list = list(set(banana_list))    # unique, in-order
    lsize = len(banana_list)                # number of unique banana counts

    # put valid banana count pairs in res_list
    for i in range(lsize):
        for j in range(i, lsize):
            if (check_inf(banana_list[i], banana_list[j])):
                res_list.append((banana_list[i], banana_list[j]))

    partners = get_partners(res_list)       # turn valid pairs into dict

    # while there are an even num of guards to pair up
    while len(partners) > 1:
        # get monkey with least partners
        # get monkey's partner with least partners                    
        monkey1 = get_min(partners)
        monkey2 = get_min_partners(partners, partners[monkey1])

        # subtract them from guard total
        # if no more monkeys with that banana count, remove from dict
        counts[monkey1] -= 1
        if counts[monkey1] == 0:
            eliminate(partners, monkey1)

        counts[monkey2] -= 1
        if counts[monkey2] == 0:
            eliminate(partners, monkey2)

    return sum(counts.values())



#banana_list = [1, 1]
#banana_list = [1, 2, 3]
#banana_list = [1, 7, 3, 21, 13, 19]
#banana_list = [1, 2, 1, 7, 3, 21, 13, 19]
print answer(banana_list)

