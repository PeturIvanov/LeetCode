class Solution(object):
    def isPalindrome(self, s):
        sentence_string = "".join([char.lower() for char in s if char.isalnum()])
        return sentence_string == sentence_string[::-1]

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))