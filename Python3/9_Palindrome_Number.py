x = 121

x = -121

x = 10

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[::-1] == str(x):
            return True
        else:
            return False

print(Solution().isPalindrome(x))