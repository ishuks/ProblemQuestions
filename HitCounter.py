from collections import defaultdict
import threading 
from random import seed, randint

class HitCounterUnordered: 
    def __init__(self): 
        self.hits = defaultdict(int)
        self.total_hits = 0 
        self.lock = threading.Lock()

    def record(self, timestamp): 
        '''
        Increments number of hits at a particular timestamp and total number timestamps

        Complexity: 
            Time: O(1)
            Space: O(N) space allocated for N unique timestamps
        '''

        with self.lock:
            self.hits[timestamp] += 1 
            self.total_hits += 1

    def total(self):
        return self.total_hits

    def range(self, lower, upper):
        '''
        Use input range to return total hits in particular range 

        Complexity: 
            Time: O(N)
            Space: O(1) additional space to existing stored key,value pairs
        '''

        if(upper < lower):
            raise Exception("Upper should be less than or equal to Lower")
        total_in_range = 0 
        for key, value in self.hits.items(): 
            if(lower <= key <= upper): 
                total_in_range += value 
        return total_in_range 

class HitCounterOrdered: 

    def __init__(self): 
        self.hits = []
        self.total_hits = 0 

    def record(self, timestamp): 
        self.hits.append(timestamp)
        self.total_hits += 1

    def total(self):
        return self.total_hits

    def range(self, lower, upper): 
        if(upper < lower):
            raise Exception("Upper should be less than or equal to Lower")
        total_hits_range = 0 
        for i in range(len(self.hits)): 
            if(lower<=self.hits[i]<=upper): 
                total_hits_range += self.hits[i]
            if(self.hits > upper): 
                break
        return total_hits_range 
        
if __name__ == '__main__': 
    seed(2)
    hitCounter = HitCounterUnordered()
    for i in range(500):
        timestamp = randint(1,500)
        threading.Thread(target= hitCounter.record, args = (timestamp,)).start()
    print(hitCounter.total())
    print(hitCounter.range(0,450))
