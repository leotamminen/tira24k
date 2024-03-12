class Node:
    def __init__(self, value, children = None):
        self.value = value
        self.children = children if children is not None else []
 
def count(node):
    def count_nodes(node):
        # Rekursiivinen funktio, joka laskee solmujen määrän alipuussa
        if not node.children:
            # Jos solmulla ei ole lapsia, palautetaan 1
            return 1
        return 1 + sum(count_nodes(child) for child in node.children)
 
    def tarkista_yht_alipuut(node):
        # Tarkistaa, ovatko kaikki alipuut yhtä suuria
        if not node.children:
            # Jos solmulla ei ole lapsia, kaikki alipuut ovat yhtäsuuria
            return True
        
        # Tarkistetaan, että kaikkien lasten alipuut ovat yhtäsuuria
        return len(set(count_nodes(child) for child in node.children)) == 1
 
    def laske_yhtamonta_solmua(node):
        # laskee yhtäsuurien alipuiden määrän juuresta
        count = 0
        if tarkista_yht_alipuut(node):
            # Jos juuri ja lapset muodostavat yhtäsuuret alipuut, kasvatetaan laskuria yhdellä
            count += 1
        for child in node.children:
            count += laske_yhtamonta_solmua(child)
        
        return count
 
    return laske_yhtamonta_solmua(node)
 
 
if __name__ == "__main__":
    tree = Node(1, [
               Node(2),
               Node(3, [Node(4, [Node(5), Node(6)])]),
               Node(7, [Node(8), Node(9)])
           ])
 
    print(count(tree)) # 8
 
    tree = Node(4, [Node(1), Node(3, [Node(2)])])
    print(count(tree)) # 3
 
    tree = Node(3, [Node(2, [Node(1)])])
    print(count(tree)) # 3