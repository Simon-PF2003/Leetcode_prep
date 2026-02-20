'''Amazon receives millions of product reviews. We want to group together "duplicate" or "near-duplicate" reviews that are just permutations of each other to clean up our 
database.
Problem:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.'''

def groupReviews(strs):
    dict = {}
    for word in strs:
        sorted_key = "".join(sorted(word))
        if sorted_key not in dict:
            dict[sorted_key] = []
        dict[sorted_key].append(word)
    return list(dict.values())


# Test inputs
if __name__ == "__main__":
    # Test case 1
    input1 = ["eat", "tea", "ate", "bat", "tab", "cat"]
    print(f"Input: {input1}")
    print(f"Output: {groupReviews(input1)}")
    print()
    
    # Test case 2
    input2 = ["listen", "silent", "enlist", "hello", "world"]
    print(f"Input: {input2}")
    print(f"Output: {groupReviews(input2)}")
    print()
    
    # Test case 3
    input3 = ["a", "b", "c"]
    print(f"Input: {input3}")
    print(f"Output: {groupReviews(input3)}")

