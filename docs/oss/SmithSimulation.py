




n = 100000

t = 
s = 
u =

A_alleles = ("AA", "Aa", "aa")
B_alleles = ("BB", "Bb", "bb")
C_alleles = ("CC", "Cc", "cc")
X_alleles = {"XX", "XY"}
frequencies_0 = {(a,b,c,x): n/27 for a in A_alleles for b in B_alleles for c in C_alleles for x in X_alleles}
#for a in A_alleles:
    #for b in B_alleles:
        #for c in C_alleles:
            #frequencies_0[(a,b,c)] = n/27

populations = [Population(frequencies_0)]


class Population(frequencies):
    
    def __init__(self, frequencies):
        self.frequencies = frequencies
        
    def propagate(self):
        frequencies_next = {}
        for a in A_alleles:
            for b in B_alleles:
                for c in C_alleles:
                    for x in X_alleles:
                        if "C" not in c:
                            if "Y" in x:
                                if
                                frequencies_next(a,b,c,x) =
                        
                