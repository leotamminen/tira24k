class Coloring:
    def __init__(self, n):
        self.graph = {i: [] for i in range(1, n + 1)}
        self.visited = {i: False for i in range(1, n + 1)}
        self.color = {i: None for i in range(1, n + 1)}
 
    # Metodi, jolla lisätään reuna
    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)
 
    # Onko jaollinen kahdella
    def kahdella_jaollinen(self, node, c):
        # Jos solmu on jo käyty ja väritetty, tarkista konflikti
        if self.visited[node]:
            return self.color[node] == c
        
        # Väritä ja merkitse solmu käydyksi
        self.visited[node] = True
        self.color[node] = c
        
        # Tarkista kaikki naapurisolmut
        for neighbor in self.graph[node]:
            if not self.kahdella_jaollinen(neighbor, not c):
                return False
        return True
 
    # Metodi, joka tarkistaa, tarkastaa voiko verkon värittää kahdella värillä
    def check(self):
        
        self.visited = {i: False for i in self.visited}
        self.color = {i: None for i in self.color}
        
        # Yritä värittää verkosto kahdella värillä
        for node in range(1, len(self.graph) + 1):
            if not self.visited[node]:
                if not self.kahdella_jaollinen(node, True):
                    return False
        return True
  
if __name__ == "__main__":
    c = Coloring(4)
    c.add_edge(1, 2)
    c.add_edge(2, 3)
    c.add_edge(3, 4)
    c.add_edge(1, 4)
    print(c.check()) # True
    c.add_edge(2, 4)
    print(c.check()) # False