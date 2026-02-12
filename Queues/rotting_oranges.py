'''You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.'''

from typing import List
from collections import deque

#I need to iterate through the grid to find rotten oranges. If I find one, I add it to a queue, and count the number of fresh oranges. Then, I see the queue, and for each
#rotten orange, I check its neighbors. If I find a fresh orange, I update the fresh_oranges, I rot it, and I add it to the queue. I also take out the previous rotten orange
#I repeat this process and update the minutes until there are no more fresh oranges.

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque() #I create a queue to keep track of the rotten oranges.
        fresh_oranges = 0
        rows = len(grid)
        columns = len(grid[0])
        minutes = -1 #I start with -1 because the first time I check the queue, I will update it to 0, and I want to count the minutes correctly.

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    fresh_oranges += 1 #I count the number of fresh oranges.
                elif grid[r][c] == 2:
                    queue.append((r,c)) #I add the rotten oranges to the queue.
        
        if fresh_oranges == 0: #If there are no fresh oranges, I return 0.
            return 0

        while queue:
            minutes += 1
            for i in range(len(queue)):
                r, c = queue.popleft() #I take out the rotten orange from the queue.
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]: #I check if the neighbors are fresh oranges.
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 1: #I am inside the map and there is a fresh orange.
                        grid[nr][nc] = 2 #I rot the fresh orange.
                        fresh_oranges -= 1 #I update the number of fresh oranges.
                        queue.append((nr, nc)) #I add the newly rotten orange to the queue.
        if fresh_oranges > 0:
            return minutes
        else: 
            return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])) # 4
    print(solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])) # -1
    print(solution.orangesRotting([[0,2]])) # 0