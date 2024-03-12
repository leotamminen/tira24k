def count(a, b):
    # Luodaan sanakirja, jossa avaimina ovat listassa b olevien lukujen arvot ja
    # arvoina niiden indeksit listassa b
    b_indeksikartta = {arvo: indeksi for indeksi, arvo in enumerate(b)}
    
    # Alustetaan muuttuja tulos laskemaan vastausten määrää
    tulos = 0
    
    # Käydään läpi listan a luvut ja niiden indeksit
    for i, arvo in enumerate(a):
        # Jos luvun arvo esiintyy listassa b sen jälkeen kun kyseinen luku on
        # esiintynyt listassa a, lisätään yksi tulos-muuttujaan
        if b_indeksikartta[arvo] > i:
            tulos += 1
    
    # Palautetaan lopullinen tulos
    return tulos
 
if __name__ == "__main__":
    print(count([2,3,4,1], [1,2,3,4])) # 3
    print(count([1,2,3,4], [1,2,3,4])) # 0
    print(count([4,7,3,1,6,2,5], [5,6,1,2,4,3,7])) # 3
    print(count([5,4,9,1,8,3,2,6,7], [6,2,8,4,9,1,5,7,3])) # 5