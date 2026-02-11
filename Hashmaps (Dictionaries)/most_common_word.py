'''Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
The words in paragraph are case-insensitive and the answer should be returned in lowercase.'''

from typing import List

#First, I need to take into account the uppercase words in the paragraph and the punctuation. I can use a list comprehension to create a new string with only lowercase 
# letters and spaces instead of punctuation. The, I need to split the words and iterate through them. If they are not banned, I will count its frequency in a dictionary,
# and I will keep track of the most frequent word and its frequency. O(n) of time and O(n) of space.

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        normalized_string = "".join([c.lower() if c.isalnum() else " " for c in paragraph])
        words = normalized_string.split()
        
        max_frequency = 0
        max_word = ''
        dict_words = {}

        for word in words:
            if word not in banned:
                dict_words[word] = dict_words.get(word, 0) + 1
                if dict_words[word] > max_frequency:
                    max_frequency = dict_words[word]
                    max_word = word
        return max_word
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])) # "ball"
    print(solution.mostCommonWord("a.", [])) # "a"
    print(solution.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"])) # "b"

