class Mex:
    def __init__(self):
        self.elementit = set()
        self.nykyinen_mex = 0
 
    def add(self, x):
        self.elementit.add(x)
        
        # Päivitetään nykyistä Mex arvoa, kunnes löydetään ensimmäinen puuttuva arvo
        while self.nykyinen_mex in self.elementit:
            self.nykyinen_mex += 1
            
        return self.nykyinen_mex
 
 
if __name__ == "__main__":
    m = Mex()
    print(m.add(1)) # 0
    print(m.add(3)) # 0
    print(m.add(4)) # 0
    print(m.add(0)) # 2
    print(m.add(5)) # 2
    print(m.add(2)) # 6