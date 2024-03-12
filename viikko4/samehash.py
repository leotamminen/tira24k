import itertools
import string
 
def find(N):
    # Sanakirja, johon tallennetaan hajautusarvoja luvulla N jaettuna
    hash_arvot = {}
 
    # Generoidaan merkkijonojen yhdistelmiä pienaakkosilla, aloittaen yksittäisistä kirjaimista
    for s in itertools.chain(string.ascii_lowercase, (''.join(p) for r in range(2, N+1) for p in itertools.product(string.ascii_lowercase, repeat=r))):
 
        # Lasketaan merkkijonon hajautusarvo luvulla N jaettuna
        h = hash(s) % N
        if h in hash_arvot:
            # Palautetaan jos on jo sanakirjassa
            return (hash_arvot[h], s)
        else:
            # Tallennetaan merkkijono sanakirjaan, jossa sen hajautusarvo modulo N on avain
            hash_arvot[h] = s
            
if __name__ == "__main__":
    print(find(42)) # esim. ('abc', 'aybabtu')