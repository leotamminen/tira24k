def count(s):
    # Luodaan laskurit nollien ja ykkösten määrälle. (Alussa molemmat 0.)
    nollia = 0
    ykkosia = 0
 
    # Iteroidaan s:n yli ja lasketaan siitä nollat ja ykköset.
    for merkki in range(0, len(s)):
 
        if s[merkki] == "0":
            nollia += 1
 
        elif s[merkki] == "1":
            ykkosia += 1
 
    if nollia >= ykkosia:
        # print(f"nollia on enemmän -> {ykkosia} ykköstä vaihdetaan.")
        return ykkosia
 
    else:
        # print(f"ykkösiä on enemmän -> {nollia} nollaa vaihdetaan.")
        return nollia
 
if __name__ == "__main__":
    print(count("01101")) # 2
    print(count("1111")) # 0
    print(count("101111")) # 1
    print(count("00001111")) # 4
