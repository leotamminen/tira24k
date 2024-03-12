class MaxList:
    def __init__(self):
        self.max_arvo = None  # Suurimman arvon tallennus
 
    def add(self, arvo):
        # Lisää arvon listalle. Jos arvo on suurempi kuin nykyinen suurin arvo, päivitetään suurin arvo.
        if self.max_arvo is None or arvo > self.max_arvo:
            self.max_arvo = arvo
 
    def max(self):
        # Palauttaa suurimman arvon listalta. Palautetaan None, jos listalla ei ole arvoja.
        return self.max_arvo
 
 
if __name__ == "__main__":
    m = MaxList()
    print(m.max()) # None
    m.add(1)
    m.add(2)
    m.add(3)
    print(m.max()) # 3
    m.add(8)
    m.add(5)
    print(m.max()) # 8