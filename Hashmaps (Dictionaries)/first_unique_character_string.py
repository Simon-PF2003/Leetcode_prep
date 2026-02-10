'''Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.'''

#First solution: I can use a dictionary to count the frequency of each character and iterate through the string to find the first
# non-repeating character. O(n) of time and O(n) of space.
'''
class Solution:
    def firstUniqueChar(self, x: str) -> int:
        dict_s = {}
        # for each character, I need to count its frequency and save it in a dictionary.
        for char in x: 
            if char in dict_s:
                dict_s[char] += 1
            else:
                dict_s[char] = 1
        #Now, I need to iterate through the string and compare to the frequency of each character in the dictionary. If the frequency 
        # is 1, I break the loop and return the index of that character. If I finish the loop without finding a unique character, I return -1.
        for i in range(len(x)):
            if dict_s[x[i]] == 1:
                return i
        return -1 '''

#Second Solution: Instead of if/else, I can use the get method of the dictionary to simplify the code. O(n) of time and O(n) of space.
class Solution:
    def firstUniqueChar(self, x: str) -> int:
        dict_s = {}
        for char in x: 
            dict_s[char] = dict_s.get(char, 0) + 1
        for i in range(len(x)):
            if dict_s[x[i]] == 1:
                return i
        return -1
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.firstUniqueChar("leetcode")) # 0
    print(solution.firstUniqueChar("loveleetcode")) # 2
    print(solution.firstUniqueChar("aabb")) # -1