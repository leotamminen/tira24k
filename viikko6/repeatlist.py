class RepeatList:
    def __init__(self):
        self.luvut = set()  # Luvut tallennetaan joukkona
        self.toisto_on = False  # Muuttuja, joka kertoo, onko toistoja
 
    # Lisää luvun x listaan
    def add(self, x):
        if x in self.luvut:
            self.toisto_on = True
        else:
            self.luvut.add(x)
 
    # Palauttaa True, jos jokin luku toistuu listalla, muuten False
    def check(self):
        return self.toisto_on
    
if __name__ == "__main__":
    r = RepeatList()
    print(r.check()) # False
    r.add(1)
    r.add(2)
    r.add(3)
    print(r.check()) # False
    r.add(2)
    print(r.check()) # True
    r.add(5)
    print(r.check()) # True