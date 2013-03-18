from sys import argv
import pprint

debug_mode = True

def log_match_state(pairing):
    if debug_mode == True:
        print('----------')
        for key in pairing.keys():
            if key[0] == 'A':
                print(str(key[1]) + '--' + str(pairing[key]))


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


class GSMatching:
    def __init__(self, prefA, prefB):
        self.m = {}
        self.A = prefA
        self.B = prefB
        self.size = len(prefA)

    def is_engaged(self, X, i):
        return (X, i) in self.m

    def pair(self, i, j):
        self.m[('A', i)] = j
        self.m[('B', j)] = i

    # A_i proposes to B_j
    def propose(self, i, j):
        if self.is_engaged('B', j):
            if self.B[j].prefers( i, self.m[('B', j)] ):
                oldA = self.m.pop(('B',j))
                self.pair(i,j)
                self.m.pop(('A', oldA))
            else:
                return False
        else:
            self.pair(i,j)

    # return an un-matched element of A, or False if there isn't one
    def get_unmatched(self):
        for i in range(0, self.size):
            if not self.is_engaged('A', i):
                return i
        return False


# prefA and prefB are lists of prefEntities
def gs(size, prefA, prefB):
    m = GSMatching(prefA, prefB)

    # list of, for each A, the next B to propose to
    nextProp = []
    for i in range(0, size):
        nextProp.append(0)

    # main loop
    i = True
    while i is not False:
        i = m.get_unmatched()
        if i is not False:
            m.propose(i, prefA[i].prefs[ nextProp[i] ])
            nextProp[i] += 1

        log_match_state(m.m)

    return m.m


# run it
if __name__ == '__main__':
    if len(argv) == 1:
        print("need module name to import")
    else:
        inp = __import__(argv[1])

        print('a: ' + str(inp.a))
        print('b: ' + str(inp.b))

        prefA = []
        prefB = []
        for ele in inp.a:
            prefA.append(prefEntity(ele))

        for ele in inp.b:
            prefB.append(prefEntity(ele))

        pairing = gs(inp.n, prefA, prefB)
        print('\nFinal:')
        log_match_state(pairing)
