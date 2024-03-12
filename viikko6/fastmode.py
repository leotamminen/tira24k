class FastMode:
    def __init__(self):
        self.taajuus = {}  # Tallennetaan lukujen esiintymistiheydet sanakirjana
        self.moodin_taajuus = 0  # Moodin taajuus
        self.nykyinen_moodi = None  # Moodin arvo
 
    def add(self, x, k):
        self.taajuus[x] = self.taajuus.get(x, 0) + k
  
        # Tarkistetaan, onko uusi moodi tai onko nykyinen moodi suurempi kuin aiemmat
        if self.taajuus[x] > self.moodin_taajuus or \
           (self.taajuus[x] == self.moodin_taajuus and (self.nykyinen_moodi is None or x < self.nykyinen_moodi)):
            self.moodin_taajuus = self.taajuus[x]
            self.nykyinen_moodi = x
 
    def mode(self):
        return self.nykyinen_moodi
 
 
if __name__ == "__main__":
    m = FastMode()
    m.add(4, 7)
    print(m.mode()) # 4
    m.add(8, 5)
    print(m.mode()) # 4
    m.add(8, 3)
    print(m.mode()) # 8
    m.add(4, 1)
    print(m.mode()) # 4