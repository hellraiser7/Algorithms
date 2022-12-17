def numIslands(grid):
    visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if visited[y][x] == False and grid[y][x] == "1":
                numIslands_Util(grid, visited, x, y)
                count += 1
    return count

def numIslands_Util(grid, visited, x, y):
    # check validity of the square and 
    # check if visited or not and
    # check if land or not, then continue to recurse
    if (0<=x<len(grid[0])) and (0<=y<len(grid)) and grid[y][x] == "1" and visited[y][x] == False:
        visited[y][x] = True
        numIslands_Util(grid, visited, x+1, y) # go right
        numIslands_Util(grid, visited, x-1, y) # go left
        numIslands_Util(grid, visited, x, y+1) # go down
        numIslands_Util(grid, visited, x, y-1) # go up

if __name__ == "__main__":
    grid = [
        ["1","1","1","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","1","0"],
        ["0","0","0","0","1"]
    ]
    grid2 = [
        ["1","0"],
        ["0","1"],
        ["0","0"]
    ]
    print(numIslands(grid))