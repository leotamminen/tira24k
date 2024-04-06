def count(x):
    # Lasketaan kolikoiden kokonaismäärä jokaiselle arvolle
    kolikot_5 = x // 5
    kolikot_2 = (x % 5) // 2
    kolikot_1 = (x % 5) % 2

    # Palauta kolikoiden kokonaismäärä
    return kolikot_5 + kolikot_2 + kolikot_1

if __name__ == "__main__":
    print(count(13)) # 4
    print(count(12345)) # 2469
    print(count(1337**9)) # 2730314408854633746890878156
