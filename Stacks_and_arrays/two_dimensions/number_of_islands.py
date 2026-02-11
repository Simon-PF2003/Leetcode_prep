'''Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.'''
from typing import List

#I need to iterate through the grid (files and columns). If I find a '1', I have to increment the counter, and I have to mark all the neighboring '1's as '0's (sink the island)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        filas = len(grid)
        columnas = len(grid[0]) #This wouldn't work if the rows were not of the same length, but it is not the case, and it is more efficient this way.
        
        def sinkIsland(f, c):
            if f < 0 or f >= filas or c < 0 or c >= columnas or grid [f][c] == '0':
                return
            grid[f][c] = '0' #I mark the current cell as '0' to avoid counting it again.
            sinkIsland(f+1, c) #I check the cell below
            sinkIsland(f-1, c) #I check the cell above
            sinkIsland(f, c+1) #I check the cell to the right
            sinkIsland(f, c-1) #I check the cell to the left

        for f in range(filas):
            for c in range(columnas):
                if grid[f][c] == '1': #If I find a '1', I have to increment the counter, and I have to mark the neighboring '1's as '0's.
                    counter += 1
                    sinkIsland(f,c) #I can create the function to look for the neighbors and use recursion.
        return counter