''' Te dan una lista de intervalos de tiempo de reuniones intervals, donde intervals[i] = [inicio, fin]. Tenés que encontrar el número mínimo de salas de conferencias 
necesarias para que se puedan llevar a cabo todas las reuniones'''

import heapq
from typing import List

# I need to sort the intervals by their start time, and iterate through them in order. I can use a min heap to keep track of the end time of the meetings that are 
# currently happening. If the start time of the current meeting is greater than or equal to the end time of the meeting that is at the top of the heap, it means that
# they can use the same room, so I pop the end time of the meeting that is at the top of the heap. Then, I add the end time of the current meeting to the heap. The size of the
# heap at the end of the iteration will be the number of rooms that are needed. O(n log n) of time and O(n) of space.

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0]) #I sort the intervals by their start time.
        heap = [] #I create a min heap to keep track of the end time of the meetings that are currently happening.
        heapq.heappush(heap, intervals[0][1]) #I add the end time of the first meeting to the heap.

        for i in range(1, len(intervals)): #I iterate through the intervals starting from the second one.
            current_start = intervals[i][0]
            end_time = intervals[i][1]

            if current_start >= heap[0]: #If the start time is greater than or equal to the end time of the meeting at the top of the heap, I can use the same room.
                heapq.heappushpop(heap, end_time) #I pop the end time of the meeting at the top of the heap and add the end time of the current meeting.
            
            else:
                heapq.heappush(heap, end_time) #If I can't use the same room, I just add the end time of the current meeting to the heap.
        return len(heap) #The size of the heap is the number of rooms that are needed.
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.minMeetingRooms([[0,30],[5,10],[15,20]])) # 2
    print(solution.minMeetingRooms([[7,10],[2,4]])) # 1