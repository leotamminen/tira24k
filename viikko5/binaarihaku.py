def binary_search(items, x):
    left = 0
    right = len(items) - 1

    while left < right:
        middle = (left + right) // 2

        if items[middle] == x:
            return True

        if items[middle] > x:
            right = middle - 1
        else:
            left = middle + 1

    return False

numbers = [1, 3, 8]

print(binary_search(numbers, 2)) # False
print(binary_search(numbers, 3)) # True
print(binary_search(numbers, 4)) # False

numbers = [1, 3, 8] # 1
numbers = [1, 3, 8] # 4
numbers = [1, 3, 8] # 9
 
# Esimerkiksi jos yrittää etsiä lukua 1 listasta [1,3,8] sitä ei löydy. Algoritmi aloittaa keskeltä ja siirtyy oikealle, kunnes menee pois hakualueelta. Vasempaan ääripäähän ei mennä ikinä.
# Myös jos luku ei ole listalla, se voi jäädä ikuiseen silmukkaan, kunnes hakualue on supistunut yhteen alkioon, mutta etsittyä alkiota ei ole löydetty.