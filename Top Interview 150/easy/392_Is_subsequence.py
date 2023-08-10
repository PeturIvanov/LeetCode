class Solution(object):
    def isSubsequence(self, s, t):
        for c in s:
            i = t.find(c)
            if i == -1:
                return False
            t = t[i+1:]

        return True

solution = Solution()
print(solution.isSubsequence(s="abc", t ="ahbgdc"))
