class Solution(object):
    def isPalindrome(self, s):
        s = "".join([char.lower() for char in s if char.isalnum()])
        return s == s[::-1]

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))