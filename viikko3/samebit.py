def count(s):
    # Lasketaan nollien ja ykkösten määrät annetussa merkkijonossa
    nollat = s.count("0")
    ykkoset = s.count("1")
 
    # Lasketaan nollaparien määrä
    nolla_parit = nollat * (nollat - 1) // 2
    
    # Lasketaan ykkösparien määrä
    ykkos_parit = ykkoset * (ykkoset - 1) // 2
 
    # Palautetaan parien määrä yhteensä
    return nolla_parit + ykkos_parit
 
if __name__ == "__main__":
    print(count("0101")) # 2
    print(count("000000")) # 15
    print(count("000111")) # 6
    print(count("00100001101100")) # 46