import time

def lisaa_ja_poista(n):
    # Mitataan aika luvun lisäämisestä listaan
    aloitus = time.time()
    lista = []
    for i in range(1, n + 1):
        lista.append(i)
    lisaysaika = time.time() - aloitus

    # Mitataan aika luvun poistolle
    aloitus = time.time()
    for i in range(n):
        del lista[0]
    poistoaika = time.time() - aloitus

    return lisaysaika, poistoaika

if __name__ == "__main__":
    n = 10**5
    lisaysaika, poistoaika = lisaa_ja_poista(n)
    print(f"Luvun lisäämiseen meni aikaa: {lisaysaika} sekuntia.")
    print(f"Luvun poistamiseen meni aikaa: {poistoaika} sekuntia.")
