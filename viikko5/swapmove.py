def solve(t):
    komennot = []
    n = len(t)
    
    jarjestys = t.copy()
    tavoite = list(range(1,n + 1))
 
    while jarjestys != tavoite:
        if jarjestys[0] > jarjestys[1] and jarjestys[1] != 1:
            komennot.append('SWAP')
            jarjestys = [jarjestys[1]] + [jarjestys[0]] + jarjestys[2:]
 
        else:
            komennot.append('MOVE')
            jarjestys = jarjestys[1:] + [jarjestys[0]]
    
    # print("Lista järjestettynä:", t)
 
    return komennot
 
if __name__ == "__main__":
    print(solve([1, 2])) # []
    print(solve([2, 1])) # ['SWAP']
    print(solve([1, 3, 2])) # ['SWAP', 'MOVE']
    print(solve([3, 2, 1])) # ['MOVE', 'SWAP']
    print(solve([2, 3, 4, 1])) # ['MOVE', 'MOVE', 'MOVE']
    print(solve([2, 3, 4, 1, 5, 6])) # 
    print(solve([1, 5, 2, 10, 4, 8, 7, 3, 6, 9]))