'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

from numpy import stack

#I can use a stack to keep track of the opening brackets. If a closing bracket is found, I check the top of the stack to see if 
# it matches the corresponding opening bracket. If it does, I pop the stack. If it doesn't, I return false.
# At the end, if the stack is empty, it is because every closing bracket found the opening before him, so the string is valid. 
# O(n) of time and O(n) of space.
class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        dict_brackets = {')': '(', '}': '{', ']': '['}
        for char in s: 
            if char in dict_brackets: #If the character is a closing bracket. 
                if stack == [] or stack[-1] != dict_brackets[char]: #I check if the stack is empty or if the top is not the corresponding opening bracket
                    return False
                else:
                    stack.pop() # If the top of the stack is the corresponding opening bracket, I pop it from the stack.
            else:
                stack.append(char) #If the character is an opening bracket, I add it to the stack.
        return len(stack) == 0

        
if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("()")) # True
    print(solution.isValid("()[]{}")) # True
    print(solution.isValid("(]")) # False