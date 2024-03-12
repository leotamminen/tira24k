def find(t):
    # sanakirja numerot, johon tallennetaan lukujen esiintymismäärät
    numerot = {}
 
    # Käydään läpi lista for loopilla
    for luku in t:
        # Lisätään luku sanakirjaan ja päivitetään sen esiintymismäärä
        numerot[luku] = numerot.get(luku, 0) + 1
 
    # Käydään läpi sanakirjan avain-arvo pareja
    for luku, maara in numerot.items():
        # Jos luku esiintyy vain kerran, palauta luku
        if maara == 1:
            return luku
 
 
if __name__ == "__main__":
    print(find([1,1,2,1])) # 2
    print(find([4,5,5])) # 4
    print(find([1,1,1,1,2])) # 2
    print(find([8,8,5,8,8])) # 5