'''Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.'''

#First Solution: I can use a stack to keep track of the characters in each string. If I encounter # I pop the stack, else I append the character.
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        list_s = []
        list_t = []
        for char in s:
            if char != '#':
                list_s.append(char)
            elif list_s:   #If I encounter a # at the beginning, I do nothing to avoid indexerror.
                list_s.pop()
        for char in t: 
            if char != '#':
                list_t.append(char)
            elif list_t: #If I encounter a # at the beginning, I do nothing to avoid indexerror.
                list_t.pop()
        if list_t == list_s:
            return True
        return False
    
# Second Solution: DRY (Don't Repeat Yourself). I can create a function to avoid repeating the same code for both strings. O(n) of time and O(n) of space.
class Solution:
    def ackspacecompare(self, s: str, t: str) -> bool:
        def proces_string(string):
            result = []
            for char in string:
                if char != '#':
                    result.append(char)
                elif result:
                    result.pop()
            return result
        return proces_string(s) == proces_string(t)
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.backspaceCompare("ab#c", "ad#c")) # True
    print(solution.backspaceCompare("ab##", "c#d#")) # True
    print(solution.backspaceCompare("a##c", "#a#c")) # True
    print(solution.backspaceCompare("a#c", "b")) # False