'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.'''
#First solution (Brute Force), bucle dentro de bucle. Poco eficiente, O(n^2)
from typing import List


'''class Solution: 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
'''
#Second Solution: Necesito mas eficiencia para no anidar bucles. Pienso en complemento del numero actual, y busco ese complemento en el array. 
#Para esto uso un diccionario (hash map) para almacenar los números y sus índices. Recorro la lista y si esta en el diccionario devuelvo el resultado, sino lo añado al diccionario. 
#O(n) de tiempo y O(n) de espacio.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       dict = {}
       for i, num in enumerate(nums):
            complement = target - num
            if complement in dict:
               return [dict[complement], i]
            else:
                dict[num] = i 

if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 4]
    target = 6
    result = sol.twoSum(nums, target)
    print(f"Result: {result}")
    