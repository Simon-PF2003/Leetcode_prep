'''Given an integer array, return true if any value appears at least twice in the array, and return false if every element is distinct.'''
#First solution (Brute Force), bucle dentro de bucle. Poco eficiente, O(n^2)
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] == nums [j]:
                    return True
        return False

#Second Solution: I need more efficiency to avoid nested loops. I interact with the list and save it on a dictionary to check if the number is already saved.
#O(n) of time and O(n) of space.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for num in nums:
            if num in dict: 
                return True
            else:
                dict[num] = 1
        return False

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1]
    result = sol.containsDuplicate(nums)
    print(f"Result: {result}")