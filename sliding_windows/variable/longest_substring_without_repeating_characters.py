'''Given a string s, find the length of the longest substring without duplicate characters.'''

#input = "abcabcbb" output = 3 because the longest substring without duplicate characters is "abc"

def lengthofLongestSubstring(s):
    left_pointer = 0
    max_length = 0
    seen_characters = set() #I use a set to keep track of the characters that I have seen in the current substring.

    for right_pointer in range(len(s)):
        while s[right_pointer] in seen_characters:
            seen_characters.remove(s[left_pointer]) #If the character at the right pointer is already in the set, it means that I have a duplicate character, so I need to move the left pointer until I remove the duplicate character from the set.
            left_pointer +=1
        seen_characters.add(s[right_pointer])
        max_length = max(max_length, right_pointer - left_pointer + 1) #I update the maximum length of the substring without duplicate characters.
    return max_length

#Option 2: Hashmap to store the last index of each character, so I can move the left pointer directly to the right of the last index of the duplicate character.
def lengthofLongestSubstring(s):
    left_pointer = 0
    max_length = 0
    seen_characters = {} #I use a hashmap to keep track of the last index of each character that I have seen in the current substring.

    for right_pointer in range(len(s)):
        char = s[right_pointer]
        if char in seen_characters and seen_characters[char] >= left_pointer:
            left_pointer = seen_characters[char] + 1 #If the character at the right pointer is already in the hashmap and its last index is greater or equal to the left pointer, it means that I have a duplicate character, so I need to move the left pointer to the right of the last index of the duplicate character.
        seen_characters[char] = right_pointer #I update the last index of the character at the right pointer in the hashmap.
        max_length = max(max_length, right_pointer - left_pointer + 1) #I update the maximum length of the substring without duplicate characters.
    return max_length