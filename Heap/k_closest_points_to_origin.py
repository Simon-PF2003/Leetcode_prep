'''Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).'''

import heapq
from typing import List

# First Solution: I need to calculate the distance of each point to the origin, and I need to keep track of the k closest points. I can use a max_heap list that keeps only the 
# best K points. I can use the heapq library to maintain the heap property. Heap look for the minimum element, but I need to pop the maximum, so I can save the negative
# distance in the heap. I need to iterate through the list. O(n log k) of time and O(k) of space.

class Solution:
    def kClosest(self, points:  List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x, y in points:
            distance = -(x**2 + y**2) #Although the distance is the square root, this is very expensive, and I can compare without using the square root.
            if len(max_heap) < k: #If the list is not full, I add the point to the heap.
                heapq.heappush(max_heap, (distance, [x, y])) #The list will have the distance and the point, so I can compare the distance and return the point.
            else: #If the list is full, I compare the distance with the maximum distance. If it is smaller, I pop the maximum and add the new point.
                heapq.heappushpop(max_heap, (distance, [x, y]))
        return [point for _, point in max_heap] #I just return the points, I don't care about the distance anymore.
    
#Second Solution: I can use a sorted function and lambda to sort the points by their distance, and return the first k points. Much more efficient, but less clear. 
# O(n log n) of time and O(n) of space.

class Solution:
    def kClosest(self, points:  List[List[int]], k: int) -> List[List[int]]:
        ordered_points = sorted(points, key=lambda distances: distances[0]**2 + distances[1]**2) #I can compare the distance without using the square root, so I just compare the squares of the distances. 
        return ordered_points[:k]
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.kClosest([[1,3],[-2,2]], 1)) # [[-2,2]]
    print(solution.kClosest([[3,3],[5,-1],[-2,4]], 2)) # [[3,3],[-2,4]]