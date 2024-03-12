class QuickList:
    def __init__(self, t):
        self.t = t.copy()  # kopioidaan t
        self.id = list(range(len(t)))  # Luodaan indeksilista t:n pituuden mukaan
        self.offset = 0  # offset nolla
 
    def move(self, k):
        self.offset -= k  # Päivitetään offset vähentämällä k:lla
 
    def get(self, i):
        return self.t[(i - self.offset) % len(self.id)]  # Palautetaan alkio listasta t käyttäen modulolaskua varmistaaksemme, että i on oikean sisäisen indeksin rajoissa
 
if __name__ == "__main__":
    q = QuickList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(q.get(4)) # 5
    q.move(3)
    print(q.get(4)) # 8
    q.move(3)
    print(q.get(4)) # 1
    q.move(10)
    print(q.get(4)) # 1
    q.move(7)
    q.move(5)
    print(q.get(0)) # 9