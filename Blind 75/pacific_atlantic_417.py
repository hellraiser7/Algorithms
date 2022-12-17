def pacificAtlantic(heights):
    islandRows = len(heights)
    islandColumns = len(heights[0])
    pacificSet = set() # cells that can flow to the pacific
    atlanticSet = set() # to keep track of the cells that can flow to the atlantic

    def DFS_Util(row, column, visited, previousHeight):
        if 0 <= row < len(heights) and 0 <= column < len(heights[0]) and (row, column) not in visited and heights[row][column] >= previousHeight:
            # check if square is valid
            # if not visited
            # if we have correct water flowing criteria satisfied
            # only then proceed with DFS
            visited.add((row,column))
            # go right
            DFS_Util(row+1, column, visited, heights[row][column])
            # go left
            DFS_Util(row-1, column, visited, heights[row][column])
            # go down
            DFS_Util(row, column+1, visited, heights[row][column])
            # go up
            DFS_Util(row, column-1, visited, heights[row][column])

    # for row-wise water flow:pacific at the top, atlantic at the bottom
    for column in range(islandColumns):
        DFS_Util(0, column, pacificSet, heights[0][column]) # current cell value = current height
        DFS_Util(islandRows - 1, column, atlanticSet, heights[islandRows-1][column])
    
    # for column-wise water flow: pacific on the left, atlantic on the right
    for row in range(islandRows):
        DFS_Util(row, 0, pacificSet, heights[row][0])
        DFS_Util(row, islandColumns - 1, atlanticSet, heights[row][islandColumns-1])

    return list(pacificSet & atlanticSet)
if __name__ == "__main__":
    heights = [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]
    print(pacificAtlantic(heights))
    

