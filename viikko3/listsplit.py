def count(t):
    # pienin arvo listassa
    min_arvo = min(t)
    
    # Etsitään pienimmän arvon ensimmäinen esiintymä
    ensimmainen_esiintyma = t.index(min_arvo)
    
    # Etsitään pienimmän arvon viimeinen esiintymä
    viimeinen_esiintyma = len(t) - 1 - t[::-1].index(min_arvo)
    
    # Lasketaan mahdollisten jakojen määrä
    mahd_jaot = viimeinen_esiintyma - ensimmainen_esiintyma
    
    # Palautetaan mahdollisten jakojen määrä
    return mahd_jaot
 
if __name__ == "__main__":
    print(count([2,1,1,3])) # 1
    print(count([1,1,1,1])) # 3
    print(count([1,2,3,1,2,3])) # 3
    print(count([1,2,3,4,3,2,1])) # 6
    print(count([4,3,2,1,2,3,4])) # 0
