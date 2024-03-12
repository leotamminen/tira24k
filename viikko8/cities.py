class Cities:
    def __init__(self, n):
        # sanakirja kaupunkien teille
        self.roads = {i: set() for i in range(1, n + 1)}
 
    def add_road(self, a, b):
        # Lisää tie kaupunkien a ja b välille
        self.roads[a].add(b)
        self.roads[b].add(a)
 
    def has_route(self, a, b):
        # leveyssuuntainen haku selvittämään, onko reittiä a:sta b:hen
        visited = set()
        queue = [a]
 
        while queue:
            # Poistetaan ensimmäinen alkio jonosta
            current = queue.pop(0)
            # Jos nykyinen solmu on kohdesolmu b, palautetaan True
            if current == b:
                return True
            
            # Jos solmussa ei ole vielä vierailtu, lisätään se vierailtujen joukkoon
            if current not in visited:
                visited.add(current)
                # Jonoon lisätään kaikki naapurisolmut, jotka eivät ole vielä vierailtuja
                # ja joilla on yhteys nykyiseen solmuun (current)
                queue.extend(self.roads[current] - visited)
        
        return False
 
if __name__ == "__main__":
    c = Cities(5)
    c.add_road(1, 2)
    c.add_road(1, 3)
    c.add_road(4, 5)
    print(c.has_route(1, 5)) # False
    c.add_road(3, 4)
    print(c.has_route(1, 5)) # True