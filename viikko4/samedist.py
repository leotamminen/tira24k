def find(t):
    eka_indeksi = {}
 
    max_etaisyys = 0
 
    for i, luku in enumerate(t):
        # Tarkistetaan, onko luku jo tallennettu eka_indeksiin
        if luku in eka_indeksi:
            # lasketaan etäisyys kahden saman luvun välillä
            etaisyys = i - eka_indeksi[luku] + 1  
            # Päivitetään suurin etäisyys tarvittaessa
            max_etaisyys = max( max_etaisyys, etaisyys )
        else:
            # Jos lukua ei ole vielä tallennettu, tallennetaan sen indeksi eka_indeksi sanakirjaan
            eka_indeksi[luku] = i
    
    # Jos suurin etäisyys on 0, palautetaan 0, muuten max_etaisyys - 1
    if max_etaisyys == 0:
        return max_etaisyys
    else:
        return max_etaisyys - 1
 
 
if __name__ == "__main__":
    print(find([1,2,1,1,2])) # 3
    print(find([1,2,3,4])) # 0
    print(find([1,1,1,1,1])) # 4
    print(find([1,1,2,3,4])) # 1
    print(find([1,5,1,5,1])) # 4