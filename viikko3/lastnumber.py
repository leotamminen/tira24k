import heapq
 
def find(t):
    # Luodaan minikeko
    heapq.heapify(t)
 
    while len(t) > 1:
        # Poistetaan kaksi pienintä lukua ja lasketaan niiden summa
        pienin1 = heapq.heappop(t)
        pienin2 = heapq.heappop(t)
        # uusi luku on tästä vähennetty 1
        uusi_luku = pienin1 + pienin2 - 1
 
        # Lisätään uusi luku minikekoon
        heapq.heappush(t, uusi_luku)
 
    # Palautetaan viimeinen luku
    return t[0]
 
if __name__ == "__main__":
    print(find([1,2,3,4])) # 7
    print(find([1,1,1])) # 1
    print(find([5,1,1,7,9,1,2])) # 20
    print(find([7,7,7])) # 19