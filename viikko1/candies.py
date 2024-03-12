def count(a, b, c):
    # Lasketaan maksimi nallekarkit
    max_nalle = c // a
    max_karkit = max_nalle
 
    # Käydään läpi kaikki mahdolliset nallekarkkien määrät
    for i in range(max_nalle + 1):
 
        # Lasketaan jäljellä oleva raha kun on ostettu i nallekarkkia
        jaljella = c - (a * i)
 
        # Lasketaan suurin mahdollinen suklaakarkkien määrä, jota voidaan ostaa
        max_suklaa = jaljella // b
 
        # Päivitetään suurin mahdollinen karkkien määrä yhteensä
        max_karkit = max(max_karkit, i + max_suklaa)
 
    return max_karkit
 
if __name__ == "__main__":
    print(count(3, 4, 11)) # 3
    print(count(5, 1, 100)) # 100
    print(count(2, 3, 1)) # 0
    print(count(2, 3, 9)) # 4
    print(count(6, 7, 6)) # 1
    print(count(2, 2, 10)) # 5