def count(s):
    # Alustetaan muuttujat ei_a_laskuri ja pituus
    ei_a_laskuri = 0
    pituus = 0
 
    # Käydään läpi merkkijonon s merkit for loopissa
    for char in s:
        # Tarkista onko merkki eri kuin "a"
        if char != "a":
            # Jos merkki ei ole "a", kasvatetaan pituus arvoa yhdellä ja lisätään se ei_a_laskuri:in
            pituus += 1
            ei_a_laskuri += pituus
        else:
            # Jos nykyinen merkki on a, pituus = 0
            pituus = 0
 
    # Palautetaan
    return ei_a_laskuri
 
 
if __name__ == "__main__":
    print(count("aaa")) # 0
    print(count("saippuakauppias")) # 23
    print(count("x")) # 1
    print(count("aybabtu")) # 9