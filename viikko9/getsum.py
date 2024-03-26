import itertools

def count(n, k, x):
    # lista numerot 1-n
    lista = [*range(1, n + 1)]
    tulos = 0

    # Käy läpi kaikki kombinaatiot listasta joissa on k alkiota
    for kombinaatio in itertools.combinations(lista, k):
        if sum(kombinaatio) == x:  # Tarkistaa onko kombinaation summa x
            tulos += 1  # kasvatetaan tulosta yhdellä jos on
    return tulos

if __name__ == "__main__":
    print(count(1, 1, 1)) # 1
    print(count(5, 2, 6)) # 2
    print(count(8, 3, 12)) # 6
    print(count(10, 4, 20)) # 16