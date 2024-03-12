def count(t):
    # Järjestetään lista ei-kasvavaan järjestykseen
    t.sort()
    
    # sanakirja osajonojen pituuksille
    osajonot = {}
 
    # Käydään läpi luvut listassa
    for luku in t:
        # Lasketaan luvun jälkeisen luvun esiintymiskerrat ja päivitetään
        osajonot[luku] = osajonot.get(luku - 1, 0) + 1
 
    # Palautetaan pisimmän osajonon pituus
    return max(osajonot.values())
 
 
if __name__ == "__main__":
    print(count([1, 1, 1, 1])) # 1
    print(count([10, 4, 8])) # 1
    print(count([7, 6, 1, 8])) # 3
    print(count([1, 2, 1, 2, 1, 2])) # 2
    print(count([987654, 12345678, 987653, 999999, 987655])) # 3