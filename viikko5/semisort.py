def solve(t):
 
    siirrot = 0
    keski = len(t) // 2
    if len(t) % 2 != 0:  # onko jakojäännös
        keski += 1  # jos on lisää 1
 
    # Tarkistetaan, onko lista jo järjestetty
    if sorted(t) == t:
        return 0
 
    for i, j in enumerate(t):
        if i < keski and j > keski:
            siirrot += (keski - i)
        elif i >= keski and j <= keski:
            siirrot += (i - keski)
    return siirrot
 
if __name__ == "__main__":
    print(solve([2, 1, 4, 3])) # 0
    print(solve([5, 3, 4, 1, 6, 2])) # 6
    print(solve([6, 5, 4, 3, 2, 1])) # 9
    print(solve([10, 1, 9, 2, 8, 3, 7, 4, 6, 5])) # 15
    print(solve([1, 6, 4, 2, 3, 5])) # 4 toimii