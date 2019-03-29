

import numpy as np


def gmean(iterable):
    a = np.array(iterable)
    return a.prod()**(1.0/len(a))

class Autosome:

    def __init__(self):
        self.gathering = np.random.uniform(0.3,1.7, 10)
        self.evasion = np.random.uniform(0.3,1.7, 10)
        
class Chromosome_x:

    def __init__(self, ss):
        self.egg_num = np.random.uniform(0,7, 5)
        
        if ss:
            self.ssa = np.random.normal(10,3, 10)   # attraction to ss
        else:
            self.ssa = np.random.normal(0,3, 10)   # attraction to ss
        
class Chromosome_y:

    def __init__(self, ss, attachment):
    
        if ss:
            self.ss = np.random.normal(10,3, 10)   # attraction to ss
        else:
            self.ss = np.random.uniform(0,5, 10)   # attraction to ss
            
        if attachment == "random":
            self.attachment = np.random.uniform(0,1, 10)
        elif attachment:
            self.attachment = np.random.uniform(8,1, 10)
        else:
            self.attachment = np.random.uniform(0,0.1, 10)
            
class Creature:

    def __init__(self, autosome1 = None, autosome2 = None):
        self.autosome1 = autosome1
        self.autosome2 = autosome2
        for autosome in [self.autosome1, self.autosome2]:
            if not autosome:
            autosome = get_autosome()

        
        
class Female(Creature):

    def __init__(self, autosome1 = None, autosome2 = None, chromosome_x1 = None, chromosome_x2 = None):
        Creature.__init__(self, autosome1 = autosome1, autosome2 = autosome2)
        self.chromosome_x1 = chromosome_x1
        self.chromosome_x2 = chromosome_x2
        for chromosome_x in [self.chromosome_x1, self.chromosome_x2]:
            if not chromosome_x:
            chromosome_x = get_chromosome_x()
    
    
class Male(Creature):

    def __init__(self, autosome1 = None, autosome2 = None, chromosome_x = None, chromosome_y = None):
        Creature.__init__(self, autosome1 = autosome1, autosome2 = autosome2)
        self.chromosome_x = chromosome_x
        self.chromosome_y = chromosome_y
        if not self.chromosome_x:
            self.chromosome_x = get_chromosome_x()
        if not self.chromosome_y:
            self.chromosome_y = get_chromosome_y()
            
            

