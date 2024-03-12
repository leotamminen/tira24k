class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children
 
def count(node):
    # Jos solmulla ei ole lapsia, palautetaan 1
    if not node.children:
        return 1
    
    # Muuten lasketaan rekursiivisesti jokaisen lapsisolmun alipuun solmujen määrä ja lasketaan ne yhteen
    return sum(count(child) for child in node.children)
 
if __name__ == "__main__":
    tree = Node(1, [
               Node(2),
               Node(3, [Node(4, [Node(5), Node(6)])]),
               Node(7, [Node(8), Node(9)])
           ])
 
    print(count(tree)) # 5