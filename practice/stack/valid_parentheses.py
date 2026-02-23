'''You are given a string s consisting of just the characters (, ), {, }, [ and ]. You need to write a function that returns True if the string is valid, and False otherwise.'''

def validParentheses(s):
    if not s:
        return True
    mapping_dict = {'}' : '{', ')': '(', ']':'['}
    stack = []
    for char in s:
        if char in mapping_dict:
            if stack == [] or stack[-1] != mapping_dict[char]:
                return False
            else:
                stack.pop()
        else:
            stack.append(char)
    return len(stack)==0

        
    
        