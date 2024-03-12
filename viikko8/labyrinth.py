def count(r):
    alku = None  # Alustetaan alkupiste (A) ja loppupiste (B)
    loppu = None
 
    # Etsitään alkupiste ja loppupiste ruudukosta
    for i in range(len(r)):
        for j in range(len(r[0])):
            if r[i][j] == 'A':
                alku = (i, j)  # Tallennetaan alkupisteen sijainti
            elif r[i][j] == 'B':
                loppu = (i, j)  # Tallennetaan loppupisteen sijainti
 
    # Jos mitään reittiä ei ole olemassa, palauta -1
    if alku is None or loppu is None:
        return -1
 
    # Määritetään mahdolliset liikkeet: ylös, alas, vasemmalle, oikealle
    liikkeet = [(1, 0), (-1, 0), (0, 1), (0, -1)]
 
    # Tarkistetaan, onko annettu sijainti kelvollinen
    def on_kelvollinen(x, y):
        return 0 <= x < len(r) and 0 <= y < len(r[0]) and r[x][y] != '#'
 
    # jono ja oltu
    jono = [(alku[0], alku[1], 0)]
    oltu = set() 
 
    # Käydään läpi solmut BFS-menetelmällä
    while jono:
        x, y, etaisyys = jono.pop(0)  # Poistetaan ensimmäinen solmu jonosta
        if (x, y) == loppu:  # Jos ollaan loppupisteessä, palautetaan etäisyys
            return etaisyys
 
        # Tutkitaan kaikki mahdolliset liikkeet
        for dx, dy in liikkeet:
            uusi_rivi, uusi_sarake = x + dx, y + dy
 
            # Jos uusi sijainti on kelvollinen ja sitä ei ole jo käyty, lisätään se jonoon
            if on_kelvollinen(uusi_rivi, uusi_sarake) and (uusi_rivi, uusi_sarake) not in oltu:
                jono.append((uusi_rivi, uusi_sarake, etaisyys + 1))  # Lisätään uusi solmu jonoon
                oltu.add((uusi_rivi, uusi_sarake))  # Lisätään oltuun
 
    # Jos loppupistettä ei löydetty, palautetaan -1
    return -1
 
if __name__ == "__main__":
    r = ["########",
         "#.A....#",
         "#.#.##.#",
         "#.##...#",
         "#...B#.#",
         "########"]
    print(count(r)) # 7