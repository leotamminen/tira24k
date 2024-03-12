def count(s):
    # Alustetaan muuttujat yhteensä ja laskuri
    yhteensa = 0  # tallennetaan erilaisten samanlaisten merkkien kokonaismäärä
    laskuri = 1   # pitää kirjaa peräkkäisten samanlaisten merkkien määrästä
 
    # Käydään läpi merkkijono
    for i in range(1, len(s)):
        # Tarkistaa onko nykyinen merkki sama kuin edellinen merkki
        if s[i] == s[i - 1]:
            # Jos nykyinen merkki on sama kuin edellinen, laskuri+1
            laskuri += 1
        else:
            # Jos nykyinen merkki eroaa edellisestä, lisätään erilaisten samanlaisten merkkien määrä yhteensä-muuttujaan
            # Lasketaan määrä yhdistämällä peräkkäisten samanlaisten merkkien määrä
            yhteensa += laskuri * (laskuri + 1) // 2
            # laskuri = 1, kun uusi erilainen merkki löytyy
            laskuri = 1
 
    # Lisätään yhteensä-muuttujaan vielä viimeisten samanlaisten merkkien määrä
    yhteensa += laskuri * (laskuri + 1) // 2
 
    # Palautetaan yhteensä
    return yhteensa
 
if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5