'''You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.'''

from collections import deque

def rottingOranges(grid):
    rows = len(grid)
    columns = len(grid[0])
    fresh_oranges = 0
    queue = deque()
    minutes = -1

    for row in range(rows):
        for col in range(columns):
            if grid[row][col] == 1:
                fresh_oranges += 1
            elif grid [row][col] == 2:
                queue.append((row, col))
        
    if fresh_oranges == 0:
        return 0
    if not queue:
        return -1
    
    while queue and fresh_oranges > 0:
        minutes += 1
        for rotten in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in ((0,1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r+dr, c+dc

                if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    queue.append((nr,nc))
    
    if fresh_oranges == 0:
        return minutes
    return -1
