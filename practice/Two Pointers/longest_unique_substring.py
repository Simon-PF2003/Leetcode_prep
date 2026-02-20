'''Amazon wants to analyze search queries to find the longest sequence of characters that doesn't repeat.
Problem:
Given a string s, find the length of the longest substring without repeating characters.'''

#Input = s = 'abcabcbb' output = 3

def longestSubstring(s):
    if not s:
        return 0
    max_count = 0
    char_set = set()
    left_pointer = 0

    for right_pointer in range(len(s)):
        while s[right_pointer] in char_set:
            char_set.remove(s[left_pointer])
            left_pointer += 1
        char_set.add(s[right_pointer])
        max_count = max(max_count, len(char_set))
    
    return max_count