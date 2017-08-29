prod = 0                # product of list
smallest = -99999       # negative closest to 0
count = 0               # number of negatives
nonzero = 0             # number of non-zero elements

for x in xs:
    # first non-zero element
    if (prod == 0 and x != 0):
        prod = x
        nonzero = nonzero + 1
    # all other non-zero elements
    elif (x != 0):
        prod = prod * x
        nonzero = nonzero + 1

    if (x < 0):
        count = count + 1

    if (x > smallest and x < 0):
        smallest = x

# if there's more than one non-zero number
# divide out negative if necessary
if (count % 2 == 1 and nonzero > 1):
    prod = prod / smallest

# if there's more than one element but product negative
# then, it must be case [-1, 0], so smallest element is 0
if (len(xs) > 1 and prod < 0):
    prod = 0


return str(prod)


