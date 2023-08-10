class Solution(object):
    def longestCommonPrefix(self, strs):
        result = ""
        first_word = strs[0]

        for i in range(len(first_word)):
            current_char = first_word[i]

            for word in strs[1:]:
                if i >= len(word):
                    return result

                compare_char = word[i]

                if current_char != compare_char:
                    return result

            result += current_char


        return result


solution = Solution()
print(solution.longestCommonPrefix(["flower", "fldas", "flplpl"]))


