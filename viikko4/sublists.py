def count(t):
    # Alustetaan muuttuja osalistojen määrän laskemiseksi
    count = 0
    # Alustetaan osalistan summa
    summa = [0]
    
    # edellisille oma sanakirja
    edelliset = dict()
    for _, value in enumerate(t):
        if not summa:
            summa.append(value)
        else:
            summa.append(summa[-1] + value)
 
        # onko nykyinen arvo jo tallennettu
        if value not in edelliset:
            edelliset[value] = dict()
 
        # Tarkista onko edellinen summa tallennettu aiemmin nykyiselle arvolle
        if summa[-2] not in edelliset[value]:
            edelliset[value][summa[-2]] = 0
        edelliset[value][summa[-2]] += 1  # Lisää yhden edellisten summojen lukumäärään
 
        # Tarkista vielä onko nykyinen summa tallennettu aiemmin nykyiselle arvolle
        if summa[-1] in edelliset[value]:
            count += edelliset[value][summa[-1]]
 
    return count
 
 
if __name__ == "__main__":
    print(count([2,3,-7,2])) # 1
    print(count([1,2,3,4,5])) # 0
    print(count([0,0,0,0,0])) # 15
    print(count([2,1,-2,1,-1,1,-1,1])) # 3
    print(count([1,1,-4,-1,5,-4,2,1])) # 1
    print(count([0]*10**5)) # 5000050000