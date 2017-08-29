import math

mylist = []
answers = []

def answer(area):
    curArea = area;
    i = 0
    while curArea > 0:
        getSqrt(curArea)
        curArea = curArea - mylist[i];
        i = i+1;

    answers = list(mylist)
    del mylist[:]
    return answers;

def getSqrt(area):
    floorRoot = int(math.sqrt(area))
    mylist.append(floorRoot * floorRoot)
    return;