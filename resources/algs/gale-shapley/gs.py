# An entity with preferences
class prefEntity:
    # pass in a list of numbers representing some permutation of
    # 0, ..., n-1
    def __init__(self, prefs):
        self.prefs = prefs

    # return True if this entity prefers i to j
    def prefers(self, i, j):
        # inefficient but easy to code!
        return self.prefs.index(i) < self.prefs.index(j)

    def next_most_preferred(self, i):
        if i >= len(self.prefs):
            raise IndexError('no more options!') 

        return self.prefs.index(i) + 1


# prefA and prefB are lists of prefEntities
def gs(size, prefA, prefB):
    A = 'A'
    B = 'B'
    p = {}

    def is_engaged(X, i):
        return (X, i) in p

    def pair(i, j):
        p[(A, i)] = j
        p[(B, j)] = i

    # A_i proposes to B_j
    def propose(i, j):
        if is_engaged(B, j):
            if prefB[j].prefers(i, p[(B, j)]):
                oldA = p.pop((B,j))
                pair(i,j)
                p.pop((A, oldA))
            else:
                return False
        else:
            pair(i,j)

    # return an un-matched element of A, or False if there isn't one
    def get_unmatched():
        for i in range(0, size):
            if not is_engaged(A, i):
                return i
        return False

    # list of, for each A, the next B to propose to
    nextProp = []
    for i in range(0, size):
        nextProp.append(0)

    # main loop
    terminate = False
    while not terminate:
        i = get_unmatched()
        #print('matching ' + str(i))
        if i is not False:
            propose(i, prefA[i].prefs[ nextProp[i] ])
            nextProp[i] += 1
        else:
            terminate = True

    # finally return
    return p


# run it
from input import *

import pprint

print('a: ' + str(a))
print('b: ' + str(b))
pprint.pprint(a)
pprint.pprint(b)

prefA = []
prefB = []
for ele in a:
    prefA.append(prefEntity(ele))

for ele in b:
    prefB.append(prefEntity(ele))

pairing = gs(n, prefA, prefB)
print(pairing)
