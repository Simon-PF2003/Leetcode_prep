'''Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible.'''

import collections
import heapq
from typing import List

#To be sure that I am not repeating characters, I need to count their frequency. I can use a dictionary for that, I'll use the Counter class. After that, 
# I can order the characters using heap, and I need a variable to save the last character that I added to the result, so I can compare it with the next character. 
# If the next character is the same as the last one, I need to pop the second most frequent character and add it to the result. O(n log n) of time and O(n) of space. 

class Solution:
    def reorganizeString(self, s: str) -> str:
        characters = collections.Counter(s) #I create the dictionary with the frequency of each character. 
        prev = None #I need a variable to save the last character that I added to the result, so I can compare it with the next character.
        res = [] #I need a list to save the result, because strings are immutable in Python, and I need to join the list at the end.
        heap = [(-quantity, char) for char, quantity in characters.items()] #I need negative quantity because I want to pop the most frequent characters, and the heap pops the smallest element (which is in the beginning)
        heapq.heapify(heap) #I create the heap with the frequency and the character.

        while heap or prev: #I need to keep adding characters until the heap is empty and there is no previous character that I need to add.
            if prev and not heap: #If there is a previous character I need to add, but the heap is empty, it means I can't add any more characters.
                return ""
            
            quantity, char = heapq.heappop(heap) #I pop the most frequent character and its quantity
            res.append(char) #I add the character to the result.

            if prev:
                heapq.heappush(heap, prev) #If there is a previous character that I need to add, I push it back to the heap, because I can use it again in the future.
                prev = None #I set the previous character to None, because I have added it to the result.

            if quantity + 1 < 0: #If after adding the character, there are still more to add, I need to save it as the previous character.
                prev = (quantity + 1, char) #I save the character and its quantity as the previous character, because I need to add it again in the future.
        
        return "".join(res) 

if __name__ == "__main__":
    solution = Solution()
    print(solution.reorganizeString("aab")) # "aba"
    print(solution.reorganizeString("aaab")) # ""