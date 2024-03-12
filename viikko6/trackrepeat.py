class TrackRepeat:
    def __init__(self):
        self.o = {}
        self.f = {}
 
    def add(self, n, c):
        if n not in self.o:
            self.o[n] = c
            if c not in self.f:
                self.f[c] = 1
            else:
                self.f[c] += 1
        else:
            p = self.o[n]
            self.f[p] -= 1
            if self.f[p] == 0:
                del self.f[p]
 
            new_count = p + c
            self.o[n] = new_count
            if new_count not in self.f:
                self.f[new_count] = 1
            else:
                self.f[new_count] += 1
 
    def check(self):
        return len(self.f) == len(self.o)
 
if __name__ == "__main__":
    t = TrackRepeat()
    print(t.check())  # True
    t.add(1, 3)
    print(t.check())  # True
    t.add(2, 3)
    print(t.check())  # False
    t.add(2, 2)
    print(t.check())  # True
    t.add(3, 1)
    print(t.check())  # True
    t.add(3, 4)
    print(t.check())  # False