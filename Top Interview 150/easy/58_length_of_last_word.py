class Solution(object):
    def lengthOfLastWord(self, s):
        list_of_strings = s.split()

        return len(list_of_strings[-1])

solution = Solution()
print(solution.lengthOfLastWord("   fly me   to   the moon  "))