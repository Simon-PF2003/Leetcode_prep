#Glosary -> Anagram: A word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.
'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.'''

# Solution: I can use a dictionary to count the frequency of each character in the first string and compare it with the second one. If frequencies match, 
# then they are anagrams. O(n) of time and O(n) of space.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        #First, I check if the lengths of the strings are different. If they are, they cannot be anagrams, so I return false.
        if len(s) != len(t):
            return False
        #I count the frequency of each character in the first string and save it in a dictionary.
        for char in s:
            if char in dict_s:
                dict_s[char] += 1
            else:
                dict_s[char] = 1
        #I count the frequency of each character in the second string and save it in another dictionary.
        for char in t:
            if char in dict_t:
                dict_t[char] += 1
            else:
                dict_t[char] = 1
        #I compare the two dictionaries. If they are the same, then the strings are anagrams.
        if dict_s == dict_t:
            return True
        else:
            return False