'''Amazon wants to analyze search queries to find the longest sequence of characters that doesn't repeat.
Problem:
Given a string s, find the length of the longest substring without repeating characters.'''

#Input = s = 'abcabcbb' output = 3

def longestSubstring(s):
    if not s:
        return 0
    seen_characters = set()
    max_length = 0
    left_pointer = 0

    for right_pointer in range(len(s)):
        while s[right_pointer] in seen_characters:
            seen_characters.remove(s[left_pointer])
            left_pointer += 1
        
        seen_characters.add(s[right_pointer])
        max_length = max(max_length, right_pointer - left_pointer + 1)
    return max_length