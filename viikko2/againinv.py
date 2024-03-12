def create(n, k):
    lista = [i + 1 for i in range(n)]
    # Alustetaan muuttujat laskuri, i ja j = 0
    laskuri, i, j = 0, 0, 0
    
    while i < k:
        if j == n - 1 - laskuri:
            j = 0
            laskuri += 1
            continue  # Siirrytään seuraavaan iteraatioon
        pito = lista[j]
        lista[j] = lista[j + 1]
        lista[j + 1] = pito
 
        # kasvata i:tä ja j:tä yhdellä
        j, i = j + 1, i + 1
 
    return lista
 
if __name__ == "__main__":
    print(create(3, 0)) # [1,2,3]
    print(create(3, 1)) # [1,3,2]
    print(create(3, 2)) # [3,1,2]
    print(create(10, 34))