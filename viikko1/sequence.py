def generate(n):
    # Alustetaan nykyinen arvo ja löydettyjen lukujen laskuri
    nykyinen = 1
    löydetyt = 0
    
    while True:
        # Muutetaan nykyinen luku merkkijonoksi
        string_nykyinen = str(nykyinen)
        
        # Tarkistetaan, onko ensimmäinen ja viimeinen merkki samat
        if string_nykyinen[0] == string_nykyinen[-1]:
 
            # kasvatetaan löydettyjen lukujen laskuria, jos on
            löydetyt += 1 
            
            # Jos löydettyjen lukujen määrä saavuttaa halutun määrän, palautetaan nykyinen
            if löydetyt == n: 
                return nykyinen
        
        # Siirrytään seuraavaan lukuun
        nykyinen += 1
        
if __name__ == "__main__":
    print(generate(1)) # 1
    print(generate(2)) # 2
    print(generate(3)) # 3
    print(generate(10)) # 11
    print(generate(123)) # 1141