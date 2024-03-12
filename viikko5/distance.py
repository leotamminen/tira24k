def find(t, k):
    # Lajitellaan luvut nousevaan järjestykseen
    t = sorted(t)
    # Alustetaan muuttuja suurimmalle etäisyydelle
    suurin_etaisyys = 0
    
    # Käydään läpi jokainen parillisen luvun väli ja päivitetään suurin etäisyys tarvittaessa
    for i in range(1, len(t)):
        etaisyys = (t[i] - t[i - 1]) // 2  # Lasketaan etäisyys kahden peräkkäisen luvun välillä
        suurin_etaisyys = max(suurin_etaisyys, etaisyys)  # Päivitetään suurin etäisyys tarvittaessa
    
    # Tarkistetaan, onko suurin etäisyys ensimmäisen ja viimeisen luvun sekä k:n ja listan viimeisen luvun välillä
    suurin_etaisyys = max(suurin_etaisyys, t[0] - 1, k - t[-1])
    # Palautetaan suurin etäisyys
    return suurin_etaisyys
 
 
if __name__ == "__main__":
    print(find([1, 2, 9], 11)) # 3
    print(find([2, 1, 3], 3)) # 0
    print(find([7, 4, 10, 4], 10)) # 3
    print(find([15, 2, 6, 4, 18], 20)) # 4
    print(find([41222388, 392676742, 307110407, 775934683, 25076911], 809136843)) # 191628970