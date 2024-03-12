def count(grid):
    # etsii huoneiden lukumäärän verkossa käyttämällä dfs
    def dfs(x, y):
        # Tarkistetaan, onko solmu kelvollinen ja onko se jo käyty läpi
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '#' or visited[x][y]:
            return
        # Merkitään solmu käydyksi ja jatketaan etsintää naapurisolmuissa
        visited[x][y] = True
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
 
    # Alustetaan vierailtu matriisi ja huoneiden määrä
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    room_count = 0
 
    # käy läpi kaikki ruudut verkossa
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Jos solmu on käymätön ja se on huoneen osa, kutsutaan dfs
            if grid[i][j] == '.' and not visited[i][j]:
                dfs(i, j)
                room_count += 1
 
    return room_count
 
 
if __name__ == "__main__":
    r = ["########",
         "#..#...#",
         "####.#.#",
         "#..#.#.#",
         "########"]
    print(count(r)) # 3