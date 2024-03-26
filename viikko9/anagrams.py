import itertools
def create(s):
    tulos = {}

    # Hyödynnetään taas itertoolseja, jonka avulla saadaan kaikki mahdolliset permutaatiot
    for permutaatio in itertools.permutations(s):
        if permutaatio not in tulos:
            tulos[''.join(permutaatio)] = 0
    return sorted(tulos)

if __name__ == "__main__":
    print(create("abc")) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(create("aaaaa")) # ['aaaaa']
    print(create("abab")) # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
    print(len(create("aybabtu"))) # 1260
    print(len(create("aybabtuu"))) # 5040