def area(rec1, rec2, rec3):
    
    # Funktio laskemaan pinta-ala, joka on päällekkäin kahden suorakulmion välillä
    def paallekkain(r1, r2):
        x_paallekkain = max(0, min(r1[2], r2[2]) - max(r1[0], r2[0]))
        y_paallekkain = max(0, min(r1[1], r2[1]) - max(r1[3], r2[3]))  # Korjattu indeksi tässä
        return x_paallekkain * y_paallekkain
 
    # Laske kaikkien kolmen suorakulmion peittämä yhteisala
    ala_yht = sum((rect[2]-rect[0]) * (rect[1]-rect[3]) for rect in [rec1, rec2, rec3])  # Korjattu indeksi tässä
 
    # Vähennä päällekkäisalueet suorakulmioiden parien välillä
    ala_yht -= paallekkain(rec1, rec2)
    ala_yht -= paallekkain(rec1, rec3)
    ala_yht -= paallekkain(rec2, rec3)
 
    # Tarkista päällekkäisyys kaikkien kolmen suorakulmion välillä ja lisää se takaisin
    x_paallekkain_kaikki = max(0, min(rec1[2], rec2[2], rec3[2]) - max(rec1[0], rec2[0], rec3[0]))
    y_paallekkain_kaikki = max(0, min(rec1[1], rec2[1], rec3[1]) - max(rec1[3], rec2[3], rec3[3]))  # Korjattu indeksi tässä
    ala_yht += x_paallekkain_kaikki * y_paallekkain_kaikki
 
    return ala_yht
 
if __name__ == "__main__":
    rec1 = (-1, 1, 1, -1)
    rec2 = (0, 3, 2, 0)
    rec3 = (0, 2, 3, -2)
    print(area(rec1, rec2, rec3))  # 16