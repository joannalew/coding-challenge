import fractions as frac


def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


# check if there's an infinite loop
# return true if infinite loop available (good thing)
# return false if numbers equal each other (bad thing)
def check_inf(num1, num2, goodSet, badSet):
    visited = set()
    visited.add(frac.Fraction(num1, num2))

    while num1 != num2:
        if (frac.Fraction(num1, num2) in goodSet):
            return True
        if (frac.Fraction(num1, num2) in badSet):
            return False

        divide = frac.gcd(num1, num2)
        if divide != 1:
            num1 /= divide
            num2 /= divide

        if num1 < num2:
            num1 += num1
            num2 -= num1 / 2
        else:
            num2 += num2
            num1 -= num2 / 2

        if (frac.Fraction(num1, num2) in visited) or (frac.Fraction(num2, num1) in visited):
            goodSet.add(frac.Fraction(num1, num2))
            return True

        visited.add(frac.Fraction(num1, num2))

    badSet.add(frac.Fraction(num1, num2))
    return False

def isFour (num):
    testnum = 4
    while testnum < num:
        testnum *= 2
    return testnum == num

def better_check_inf(num1, num2):
    if num1 == num2:
        return False

    divide = frac.gcd(num1, num2)
    num1 /= divide
    num2 /= divide
    return not isFour(num1 + num2)

def answer(banana_list):
    # your code here
    return




#banana_list = [1, 1]
banana_list = [1, 7, 3, 21, 13, 19]

goodSet = set()
goodSet.add(frac.Fraction(1,2))
goodSet.add(frac.Fraction(1,4))
goodSet.add(frac.Fraction(1,5))
goodSet.add(frac.Fraction(1,6))
goodSet.add(frac.Fraction(1,8))
goodSet.add(frac.Fraction(1,9))
goodSet.add(frac.Fraction(1,10))
goodSet.add(frac.Fraction(1,11))
goodSet.add(frac.Fraction(1,12))
goodSet.add(frac.Fraction(1,13))
goodSet.add(frac.Fraction(1,14))

badSet = set()
badSet.add(frac.Fraction(1,3))
badSet.add(frac.Fraction(1,7))
badSet.add(frac.Fraction(1,15))
#for x in combinations(banana_list, 2):
#	print Fraction(x[0], x[1])

test = 1

for i in range(1, 101):
    print "[%d]: " % i, check_inf(test, i, goodSet, badSet), better_check_inf(test, i)