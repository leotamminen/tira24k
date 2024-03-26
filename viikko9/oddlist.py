import itertools

def count(n, x):
    # lista 1...n
    lista = list(range(1, n + 1))
    laskuri = 0

    # Käydään läpi kaikki mahdolliset permutaatiot listassa
    for jarjestys in itertools.permutations(lista):
        # Tarkistetaan, onko järjestys kelvollinen ja alkaako se x:llä
        if kelvollinen_jarjestys(jarjestys) and jarjestys[0] == x:
            laskuri += 1
    return laskuri

def kelvollinen_jarjestys(jarjestys):
    # Tallentaa jokaisen parin summan
    summat = {}

    for i in range(len(jarjestys) - 1):
        # Tarkistaa, onko absoluuttinen summa jo tallennettu
        if abs(jarjestys[i] + jarjestys[i + 1]) in summat:
            return False
        summat[abs(jarjestys[i]+jarjestys[i + 1])] = 1
    return True

if __name__ == "__main__":
    print(count(1, 1)) # 1
    print(count(4, 2)) # 4
    print(count(8, 5)) # 830