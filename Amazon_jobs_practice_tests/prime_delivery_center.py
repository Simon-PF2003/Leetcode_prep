'''Amazon has a distribution center in the coordenate (0,0) and it has to deliver packages to different coordenates (x,y).
You are given a list of coordenates and an integer k. Your task is to return the closest k coordenates to the distribution center.
The distance between two coordenates (x1,y1) and (x2,y2) is given by the formula: sqrt((x2-x1)^2 + (y2-y1)^2).'''

import heapq
#First solution: Less efficient, but clearer. I calculate the distance of each coordenate to the distribution center and save it in a list. Then, I convert the list into a heap 
# and I pop the closest coordenates from the heap until I have k coordenates in the result list. O(n log n) of time and O(n) of space.

def primeDeliveryCenter(coordinates, k):
    if not coordinates or k <= 0:
        return []
    heap = [(x**2 + y**2, [x,y]) for x,y in coordinates] #I calculate the distance of each coordenate to the distribution center and save it in a list.
    heapq.heapify(heap) #I convert the list into a heap. The heap will be ordered by distance, so the closest coordenates will be at the top of the heap.
    result = []

    for _ in range(min(k, len(heap))):
        distance, coordinate = heapq.heappop(heap) #I pop the closest coordenate from the heap. The distance is positive, so I don't need to negate it.
        result.append(coordinate) #I add the coordenate to the result list.
    
    return result

#Second Solution: More efficient, but less clear. I can save in the heap only the top k elements. For that, I need to save the distances as its negative, so the heashpushpop
# takes out the biggest and keep the smallest k elements. O(n log n) of time and O(n) of space.    

def primeDeliveryCenter(coordinates, k):
    if not coordinates or k <= 0:
        return []
    heap = []
    result = []
    for x, y in coordinates:
        dist = (x**2+y**2)

        if len(heap) < k:
            heapq.heappush(heap, (-dist, [x,y])) #I save the distance as negative, so the heashpushpop takes out the biggest and keep the smallest k elements.
        else:
            heapq.heappushpop(heap, (-dist, [x,y])) #If the heap has more than k elements, I push the new coordenate and pop the farthest coordenate. This way, I keep only the k closest coordenates in the heap.
    
    while heap:
        distance, coordinate = heapq.heappop(heap) #I pop the closest coordenate from the heap. The distance is negative, so I need to negate it to get the actual distance.
        result.append(coordinate) #I add the coordenate to the result list.
    
    return result[::-1]

#Third Solution: I can use the sorted function and a lambda to sort the coordenates by their distance to the distribution center, and return the first k coordenates.

def primeDeliveryCenter(coordinates, k):
    if not coordinates or k <= 0:
        return []
    ordered_coordinates = sorted(coordinates, key=lambda coord: coord[0]**2 + coord[1]**2) #I can compare the distance without using the square root, so I just compare the squares of the distances. 
    return ordered_coordinates[:k] #I return the first k coordenates, which are the closest to the distribution center.

if __name__ == "__main__":
    print(primeDeliveryCenter([[1,2],[3,4],[1,-1]], 2)) # [[1,-1],[1,2]]
    print(primeDeliveryCenter([[3,3],[5,-1],[-2,4]], 2)) # [[3,3],[-2,4]]
    print(primeDeliveryCenter([[0,1],[1,0]], 2)) # [[0,1],[1,0]]