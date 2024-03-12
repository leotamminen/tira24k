def count(s):
    maara = 0
    # sanakirja merkkejen kohdille
    merkit = {"t": None, "i": None, "r": None, "a": None}
 
    # Tarkistaa, onko kaikki merkit löydetty
    def kaikki_merkit_loytyy():
        return merkit["t"] is not None and merkit["i"] is not None and merkit["r"] is not None and merkit["a"] is not None
 
    # Palauttaa pienimmän indeksin
    def pienin():
        return min(merkit["t"], merkit["i"], merkit["r"], merkit["a"])
    
    # käy läpi merkkijonon
    for i, v in enumerate(s):
        if v in merkit:
            merkit[v] = i
 
        # Jos kaikki merkit on löydetty, lisätään laskuriin pienin indeksi
        if kaikki_merkit_loytyy():
            maara += pienin() - (-1)
 
    return maara
 
if __name__ == "__main__":
    print(count("aybabtu")) # 0
    print(count("tira")) # 1
    print(count("ritari")) # 6
    print(count("tiratiratira")) # 45
    print(count("xaxrxixtx")) # 4
    print(count("ritarita")) # 15
    # nyt toimii
    print(count("tira"*(10**5))) # 79999000003
