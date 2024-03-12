class NearList:
    def __init__(self, t):
        # Luodaan lajiteltu lista syötteen perusteella
        self.lajiteltu = sorted(t)
 
    def find(self, x):
        # Tarkistetaan, onko x pienempi tai yhtä suuri kuin pienin arvo listassa
        if x <= self.lajiteltu[0]:
            return self.lajiteltu[0]
        
        # Tarkistetaan, onko x suurempi tai yhtä suuri kuin suurin arvo listassa
        if x >= self.lajiteltu[-1]:
            return self.lajiteltu[-1]
 
        # Käytetään binäärihakua lähimmän arvon löytämiseksi
        alaraja, ylaraja = 0, len(self.lajiteltu) - 1
 
        while alaraja <= ylaraja:
            keski = (alaraja + ylaraja) // 2
  
            if self.lajiteltu[keski] == x:
                return x
 
            elif x < self.lajiteltu[keski]:
                ylaraja = keski - 1
 
            else:
                alaraja = keski + 1
        
        # Palautetaan lähin arvo
        if self.lajiteltu[alaraja] - x < x - self.lajiteltu[ylaraja]:
            return self.lajiteltu[alaraja]
        else:
            return self.lajiteltu[ylaraja]
 
        
if __name__ == "__main__":
    n = NearList([3, 6, 1, 3, 9, 8])
    print(n.find(1)) # 1
    print(n.find(2)) # 1
    print(n.find(3)) # 3
    print(n.find(4)) # 3
    print(n.find(5)) # 6
    print(n.find(6)) # 6
    print(n.find(7)) # 6
    print(n.find(8)) # 8
    print(n.find(9)) # 9