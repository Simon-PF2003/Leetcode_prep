'''Given an integer x, return true if x is a palindrome, and false otherwise.'''
#Efficient solution. I can convert the integer to a string and use two pointers to compare the characters from the start and end 
# of the string. If they are different, then it is not a palindrome. O(n) of time and O(1) of space.
# An inefficient solution would be to use a "for" loop to see the original input, and another to see it reversed.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        L=0
        R=len(s)-1
        while L<R:
            if s[L] != s[R]:
                return False
            L+=1
            R-=1
        return True



if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(121)) # True
    print(solution.isPalindrome(-121)) # False