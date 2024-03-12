# Varastossa n laatikkoa
# maksimipaino x
def solve(t, x):
 
    # Järjestä painolista ei-kasvavaan järjestykseen
    t.sort()
    
    maara = 0
    paino_yht = 0
    
    # Käytetään yhtä osoitinta laatikon maksimimäärän löytämiseen
    for paino in t:
        if paino_yht + paino <= x:
            paino_yht += paino
            maara += 1
        else:
            # Jos lisäys ylittää painorajan, break
            break
    
    return maara
 
if __name__ == "__main__":
    print(solve([1, 1, 1, 1], 2)) # 2
    print(solve([2, 5, 3, 2, 8, 7], 10)) # 3
    print(solve([2, 3, 4, 5], 1)) # 0
    print(solve([2, 3, 4, 5], 10**9)) # 4
    print(solve([10**9, 1, 10**9], 10**6)) # 1