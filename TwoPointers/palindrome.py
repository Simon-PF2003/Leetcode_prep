'''Given an integer x, return true if x is a palindrome, and false otherwise.'''

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