'''Given an array of strings words and an integer k, return the k most frequent strings.
Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.'''

import collections
import heapq
from typing import List
# I need to count the frequency of each word, so a dictionary is necessary. The counter class might help me avoid a for loop and if. After that, I need to create a heap
# with the frequency and the word. I need to compare the frequency first, and if they are the same, I need to compare the word. To do that, I can't usa a min heap, and I 
# should save all the words and frequencies. Then, I need to pop the K most frequent words. O(n log n) of time and O(n) of space.
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cant_words = collections.Counter(words) #I create the dictionary with the frequency of each word. O(n) of time and O(n) of space.
        heap = [(-quantity, word) for word, quantity in cant_words.items()] #I need negative quantity because I want to pop the most frequent words, and the heap pops the smallest element (which is in the beginning)
        heapq.heapify(heap) #I create the heap with the frequency and the word. O(n) of time and O(n) of space.

        result = []
        for i in range(k): #I need to pop the K most frequent words. O(k log n) of time and O(k) of space.
            result.append(heapq.heappop(heap)[1]) #I pop the most frequent word and I append it to the result. I just need the word, not the frequency, so I take the second element of the tuple.
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent(["i","love","leetcode","i","love","coding"], 2)) # ["i","love"]
    print(solution.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4)) # ["the","is","sunny","day"]