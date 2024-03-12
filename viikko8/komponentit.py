# laskee verkon komponenttien määrän
def laske_komponentit(N):
    # solmujen edustajat
    edustajat = [0] * (N + 1)
 
    # Funktio etsii solmun edustajan
    def etsi_edustaja(x):
        if edustajat[x] == 0:
            return x
        edustajat[x] = etsi_edustaja(edustajat[x])
        return edustajat[x]
 
    # Alustetaan komponenttien määrä
    komponentit = N - 1  # Vähennetään yksi, koska solmu 1 ei ole mukana
 
    # Käydään läpi kaikki solmut välillä 2 - N
    for i in range(2, N + 1):
        for j in range(2 * i, N + 1, i):
            # Etsitään solmun edustajat
            edustaja_i = etsi_edustaja(i)
            edustaja_j = etsi_edustaja(j)
            # jos solmujen edustajat eivät ole samat yhdistetään ne
            if edustaja_i != edustaja_j:
                edustajat[edustaja_j] = edustaja_i
                komponentit -= 1
 
    return komponentit
 
# kun N = 1000
N = 1000
print(f"Komponenttien määrä N = {N} on {laske_komponentit(N)}")

# 74