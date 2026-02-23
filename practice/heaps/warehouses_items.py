'''In our warehouses, we track millions of items. Sometimes, we need to find which items are being 'picked' the most to optimize where we store them. This brings us to a classic
 problem: Top K Frequent Elements."

The Problem:
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.'''


#Heap (O(len(nums)))
import heapq
from collections import Counter

def frequentItems(nums, k):
    if not nums or not k:
        return []
    dict_items = Counter(nums)
    heap = [(-quantity, item) for item, quantity in dict_items.items()]
    heapq.heapify(heap)
    res = []
    for i in range(k):
        _, item = heapq.heappop(heap)
        res.append(item)
    return res

#Heap (O(K))

def frequentItems(nums, k):
    if not nums or not k:
        return []
    dict_items = Counter(nums)
    heap = []
    for i, freq in dict_items.items():
        heapq.heappush(heap, (freq, i))
        if len(heap) > k:
            heapq.heappop(heap)
    return [i for _, i in heap]
    
#Bucket
def frequentItems(nums, k):
    if not nums or not k:
        return []
    bucket = {}
    items = Counter(nums)
    for item, value in items.items():
        if value not in bucket:
            bucket[value] = []
        bucket[value].append(item)
    res = []
    for i in range(len(bucket) - 1, 0, -1):
        for num in bucket[i]:
            res.append(num)
            if len(res) == k:
                return res
    
