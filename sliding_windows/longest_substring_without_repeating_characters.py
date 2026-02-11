'''Given a string s, find the length of the longest substring without duplicate characters.'''

#I need to keep track of the characters in the current substring and count the length of the substring.
#While I read the string, it increases its length, and I save that length if it is the longest. If I find a duplicate character, I need to remove ALL the characters
#before its first occurence. I can use a set to keep track of the characters in the substring, and two pointers to the beginning and the end of the substring. 
# O(n) of time and O(n) of space. 

class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        substring = set() #It acts as a temporary memory of the characters in the current substring.
        left = 0 #It is the left pointer of the substring.
        max_length = 0 #It is the length of the longest substring without duplicate characters.

        for right in range(len(s)): #Each new character will be at right of the string
            while s[right] in substring: # If the character is in the set, it is because it repeated, so I need to remove all the characters before its first occurence.
                substring.remove(s[left]) #I remove the first character of the substring, which is at left of the string. This is not enough, the repeated character can be in the middle of the substring, so I need to keep removing characters until I remove the repeated character.
                left += 1 #I move the left pointer to the right. This repeats until the character is no longer repeated (not in the set)
            substring.add(s[right]) #In case the character is not in the set, I add it and check the length of the substring.
            max_length = (max(max_length, right-left+1))
        return max_length

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb")) # 3
    print(solution.lengthOfLongestSubstring("bbbbb")) # 1
    print(solution.lengthOfLongestSubstring("pwwkew")) # 3