def sijainticount(s, start, kaydyt):
  sijainti = start.copy()  # Kopioidaan alku sijainti muuttamista varten
  kaydyt.add(tuple(sijainti))  # Lisätään alku sijainti käytyihin ruutuihin
 
  for liikuta in s:
    # Päivitetään robotin sijainti liikkeen perusteella
    if liikuta == 'U':
      sijainti[1] += 1
    elif liikuta == 'D':
      sijainti[1] -= 1
    elif liikuta == 'L':
      sijainti[0] -= 1
    elif liikuta == 'R':
      sijainti[0] += 1
 
    # Lisätään uusi ruutu käytyihin, jos ei käyty
    if tuple(sijainti) not in kaydyt:
      kaydyt.add(tuple(sijainti))
 
  return (len(kaydyt), sijainti, kaydyt)
 
def count(s, k):
  
  # Laskee ensimmäisen liikesarjan käydyt ja robotin lopullisen sijainnin
  (ensimmainen_kayty, sijainti, kaydyt) = sijainticount(s, [0, 0], set())
 
  # Lista eri liikesarjojen käymien ruutujen erotuksille
  erotukset = [ensimmainen_kayty]
  
  # Seuraavan liikesarjan käytyjen ruutujen määrä
  seuraava_kayty = ensimmainen_kayty
 
  # Looppaa läpi simuloiden k toistoa
  for _ in range(len(s + "1")):
    # Välimuuttuja edelliselle käytyjen ruutujen määrälle
    edellinen_kayty = seuraava_kayty
 
    # Laskee seuraavan liikesarjan käydyt ja päivittää sijainnin ja käydyt
    (seuraava_kayty, sijainti, kaydyt) = sijainticount(s, sijainti, kaydyt)
 
    # Tallentaa erotuksen käytyjen ruutujen määrässä edelliseen liikesarjaan nähden
    erotukset.append(seuraava_kayty - edellinen_kayty)
 
  # Palauttaa kaikkien liikesarjojen käytyjen ruutujen määrän summan
  # ja lisää viimeisen erotuksen kerrottuna toistojen määrällä (k) - toistettujen liikesarjojen määrä
  return sum(erotukset) + (erotukset[-1]) * (k - len(erotukset))
 
if __name__ == "__main__":
    print(count("UR", 100)) # 201
    print(count("UD", 100)) # 2
    print(count("UURRDDL", 500)) # 1506
    print(count("L", 10**9)) # 1000000001
    print(count("DLUR", 10**9)) # 4