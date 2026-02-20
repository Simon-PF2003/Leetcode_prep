'''In our system, we have thousands of product 'tags'. Sometimes, different products have tags that are actually anagrams of each other 
(they use the exact same letters but in a different order).
Given an array of strings strs, group the anagrams together. You can return the answer in any order.'''
# input = ["eat","tea","tan","ate","nat","bat"] output = [["bat"],["nat","tan"],["ate","eat","tea"]]
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        dict = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in dict:
                dict[key] = []
            dict[key].append(word)
        return list(dict.values())