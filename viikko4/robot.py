def count(s):
    # ruudut, jossa robotti käy
    kaydyt = set()
    
    # Alustetaan robotin sijainti (x, y)
    x, y = 0, 0
    
    # Lisätään aloitusruutu käytyjen joukkoon
    kaydyt.add((x, y))
    
    # Käydään läpi jokainen liike merkkijonosta
    for liikuta in s:
        # Päivitetään robotin sijainti liikkeen perusteella
        if liikuta == 'U':
            y += 1
        elif liikuta == 'D':
            y -= 1
        elif liikuta == 'L':
            x -= 1
        elif liikuta == 'R':
            x += 1
        
        # Lisätään ruutu käytyihin
        kaydyt.add((x, y))
    
    # Palautetaan käytyjen ruutujen määrä
    return len(kaydyt)
 
 
if __name__ == "__main__":
    print(count("LL"))     # 3
    print(count("UUDLRR")) # 5
    print(count("UDUDUDU"))# 2
    print(count("URDLL"))# 5
    print(count("URDLLRDU"))# 6