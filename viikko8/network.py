class Network:
    def __init__(self, n):
        # Alustetaan verkko tietokoneiden määrällä ja tyhjällä sanakirjalla
        self.n = n
        self.connections = {}
 
    def add_link(self, a, b):
        # Lisätään yhteys kahden tietokoneen välille
        if a not in self.connections:
            self.connections[a] = set()
        if b not in self.connections:
            self.connections[b] = set()
        self.connections[a].add(b)
        self.connections[b].add(a)
 
    def best_route(self, a, b):
        # Tarkistetaan, onko alku- ja loppupiste olemassa verkossa
        if a not in self.connections or b not in self.connections:
            return -1
        # Käytetään leveyssuuntaista hakua (BFS) etsimään lyhin reitti alku- ja loppupisteen välillä
        visited = set()
        queue = [(a, 0)]
 
        while queue:
            node, distance = queue.pop(0)
            if node == b:
                return distance
            visited.add(node)
            for neighbor in self.connections[node]:
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))
        # Jos reittiä ei löydy, palautetaan -1
        return -1
 
if __name__ == "__main__":
    # Luodaan verkko, lisätään yhteyksiä ja etsitään parhaat reitit
    w = Network(5)
    w.add_link(1, 2)
    w.add_link(2, 3)
    w.add_link(1, 3)
    w.add_link(4, 5)
    print(w.best_route(1, 5))  # -1
    w.add_link(3, 5)
    print(w.best_route(1, 5))  # 2