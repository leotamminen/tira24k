def find(s):
 
    # Iteroidaan alimerkkijonon pituuden läpi. 1:stä puoleen pituuteen
    # Sillä jos alimerkkijono on pidempi kuin puolet alkuperäisen merkkijonon pituudesta, sitä ei voida toistaa koko merkkijonossa.
    for i in range(1, len(s) // 2 + 1): 
        # Tarkistetaan, voiko merkkijono jakautua tasaisiin osiin pituudella i
        if s[:i] * (len(s) // i) == s and len(s) % i == 0:
            return i  # Palautetaan lyhimmän toistuvan alimerkkijonon pituus
    return len(s)  # Jos ei toistuvaa alimerkkijonoa, palautetaan alkuperäinen pituus
 
if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7
