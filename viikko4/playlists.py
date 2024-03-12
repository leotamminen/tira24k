def count(t):
    viimenen = {}
    alku = 0
    yhteensa = 0
 
    # Käydään läpi taulukon t alkioita indeksin ja kappaleen kautta
    for i, kappale in enumerate(t):
        # Tarkistetaan, onko kappale jo viimeisissä esiintymisindekseissä
        # ja onko sen indeksi suurempi tai yhtäsuuri kuin alkuindeksi
        if kappale in viimenen and viimenen[kappale] >= alku:
            # Jos näin on, päivitetään alkuindeksi seuraavaksi indeksiksi
            alku = viimenen[kappale] + 1
 
        # Päivitetään kappaleen viimeisin esiintymisindeksi
        viimenen[kappale] = i
        # Lisätään yhteenlaskettuihin etäisyyksiin etäisyys alkuindeksistä
        yhteensa += i - alku + 1
 
    # Palautetaan yhteenlasketut etäisyydet
    return yhteensa
 
 
if __name__ == "__main__":
    print(count([1,2,3,4])) # 10
    print(count([1,1,1,1])) # 4
    print(count([5])) # 1
    print(count([1,3,2,3,4,2,4,1,2,1])) # 24