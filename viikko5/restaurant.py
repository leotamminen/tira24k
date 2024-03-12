# a = arrivals, d = departures
def find(a, d):
    
    # Järjestetään tapahtumat saapumisajan mukaan, merkitään tyyppi ('arrival' tai 'departure') tapahtumille
    sorted_events = sorted([(aika, 'arrival') for aika in a] + [(aika, 'departure') for aika in d])
 
    # Alustetaan muuttujat asiakkaiden määrän, pisimmän odotusajan ja viimeisen lähtöajan seurantaa varten
    asiakkaiden_maara = 0
    pisin_odotusaika = 0
    viimeinen_lahtoaika = None
 
    # Käydään läpi järjestetyt tapahtumat
    for aika, event_type in sorted_events:
        if event_type == 'arrival':
            
            # Jos palvelupiste on tyhjä ja edellisestä lähdöstä on kulunut aikaa, päivitetään tila
            if asiakkaiden_maara == 0 and viimeinen_lahtoaika is not None and aika > viimeinen_lahtoaika:
                pisin_odotusaika = max(pisin_odotusaika, aika - viimeinen_lahtoaika)
            asiakkaiden_maara += 1
            viimeinen_lahtoaika = None
        else:
            # Vähennetään palveltavien asiakkaiden määrää ja päivitetään viimenen lähtöaika
            asiakkaiden_maara -= 1
            if asiakkaiden_maara == 0:
                viimeinen_lahtoaika = aika
 
    # palautetaan pisin odotusaika
    return pisin_odotusaika
 
 
if __name__ == "__main__":
    print(find([1, 6], [2, 9])) # 4
    print(find([1, 2, 3], [2, 3, 4])) # 0
    print(find([1, 4, 6, 8], [5, 5, 9, 9])) # 1
    print(find([1, 10**9], [2, 10**9+1])) # 999999998