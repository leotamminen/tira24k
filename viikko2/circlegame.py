def create(n):
    # Luo alkujärjestyksen piiristä
    piiri = list(range(1, n + 1))
    # järjestys, jossa pelaajat lähtevät piiristä
    lahtojarjestys = []
    # Alustaa aloitusindeksin
    indeksi = 0
    
    # toistetaan kunnes piirissä ei ole pelaajia
    while piiri:
        # päivittää indeksin, kiertäen ympyrässä
        indeksi = (indeksi + 1) % len(piiri)
        
        # poistaa ja lisää pelaajan lähtöjärjestykseen
        lahtojarjestys.append(piiri.pop(indeksi))
    
    return lahtojarjestys
 
 
if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(3)) # [2,1,3]
    print(create(7)) # [2,4,6,1,3,5,7]
    print(create(6)) # [2, 4, 6, 3, 1, 5]
    print(create(2)) # [2, 1]
    print(create(4)) # [2, 4, 3, 1]