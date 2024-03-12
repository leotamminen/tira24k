def count(t):
    # Alustetaan sanakirja hinnan tuplaantumisten määrillä
    hinnan_tuplaantuminen_maara = {}
    # Alustetaan muuttuja eri tapojen määrälle
    tapojen_maara = 0
 
    # käydään läpi taulukko t käänteisessä järjestyksessä indeksin ja arvon kautta
    for i in range(len(t) - 1, -1, -1):
        # Lisätään tapojen määrään arvo hinnan tuplaantumisten sanakirjasta kaksinkertaiselle arvolle
        tapojen_maara += hinnan_tuplaantuminen_maara.get(t[i] * 2, 0)
        # Päivitetään hinnan tuplaantumisten sanakirjaa, lisäämällä yksi kappale hinnalle tai päivittämällä sen määrää
        hinnan_tuplaantuminen_maara[t[i]] = hinnan_tuplaantuminen_maara.get(t[i], 0) + 1
    
    # Palautetaan tapojen määrä
    return tapojen_maara
 
 
 
if __name__ == "__main__":
    print(count([1,2,3,4])) # 2
    print(count([1,1,1,1])) # 0
    print(count([1,2,1,2,1,2])) # 6
    print(count([5,1,3,4,1,6])) # 1