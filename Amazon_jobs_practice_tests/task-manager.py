'''The enterprise has K servers. Each one gives you a list of tasks IDs that are ordered from less to more recent. You have to combine all the lists in a single list
thar is also ordered.'''

import heapq

# I have k servers. Each one with a list of task ID ordered. I need to combine all the lists in a single list that is also ordered. 
# I can use a heap to keep track of the next task ID from each server. The heap will have at most k elements, one from each server.
# I will pop the smallest task ID and add it to the result list. Then, I will push the next task ID from the same server into the heap. 
# I will repeat this process until the heap is empty. 
#To do that, I need to know the value of the task ID, the index of the server it came from, and the index of the task ID in that server's list.
def mergeTasks(tasks_list, k):
    heap = []
    for i in range(k): #I iterate through the servers and I push the first task ID of each server into the heap.
        if tasks_list[i]:
            heapq.heappush(heap, (tasks_list[i][0], i, 0)) #I push a tuple with the task ID, index of the server, and index of the task ID for each server.
    
    result = []
    while heap: 
        value, list_index, element_index = heapq.heappop(heap) #I pop the smallest task ID from the heap. I get the value, index of server and index of task ID from the tuple.
        result.append(value) #I add the task ID to the result list.

        if element_index + 1 < len(tasks_list[list_index]):  #If there are more tasks IDs in the same server, I push them to the heap.
            next_value = tasks_list[list_index][element_index + 1]
            heapq.heappush(heap, (next_value, list_index, element_index + 1))