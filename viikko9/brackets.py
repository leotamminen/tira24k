import itertools

def count(n, k):
    tulos = laske_jonot(n, k)
    return tulos

def laske_jonot(n, k, d=0):
    # tarkistaa että annettu d-arvo kelvollinen
    if d < 0 or d > n or d > k:
        return 0
    
    # jos n on 0, palauttaa 1, koska yksi jono on mahdollinen tyhjällä listalla
    if n == 0:
        return 1
    
    # Laskee rekursiivisesti jäljellä olevat järjestyslukujonot lisäämällä ja vähentämällä d-arvoa
    return laske_jonot(n - 1, k, d + 1) + \
           laske_jonot(n - 1, k, d - 1)

if __name__ == "__main__":
    print(count(6, 1)) # 1
    print(count(6, 2)) # 4
    print(count(6, 3)) # 5
    print(count(9, 1)) # 0
    print(count(16, 4)) # 1094