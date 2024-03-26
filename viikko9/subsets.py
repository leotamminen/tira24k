import itertools

def create(t):
    tulos = [0]

    # Käy läpi mahdolliset kombinaatioiden pituudet
    for i in range(1, len(t) + 1):
        for kombinaatio in itertools.combinations(t, i):
            # Käydään läpi kaikki kombinaatiot listassa pituudella i
            tulos.append(sum(kombinaatio))
    return sorted(tulos)
    
if __name__ == "__main__":
    print(create([1, 2, 3])) # [0, 1, 2, 3, 3, 4, 5, 6]
    print(create([42, 1337])) # [0, 42, 1337, 1379]
    print(create([1, 1, 1])) # [0, 1, 1, 1, 2, 2, 2, 3]
    print(create([5])) # [0, 5]
