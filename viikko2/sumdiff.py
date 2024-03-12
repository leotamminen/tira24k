def create(n):
    # Alustetaan lista, joka sisältää luvut 1 - n
    lista = list(range(1, n + 1))
    
    # Lisätään jokaiseen alkioon 1.
    for i in range(n):
        lista[i]
    
    # Palautetaan lopullinen lista
    return lista
 
if __name__ == "__main__":
    print(create(6)) # [3, 1, 6, 2, 4, 5]
    print(create(10)) # [7, 10, 3, 1, 5, 4, 8, 6, 9, 2]
    print(create(15)) # [9, 4, 6, 14, 15, 13, 12, 11, 5, 2, 3, 8, 1, 7, 10]