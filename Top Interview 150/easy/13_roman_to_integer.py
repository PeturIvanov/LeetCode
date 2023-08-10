class Solution(object):
    def romanToInt(self, s):
        symbols = {"I": 1,
                   "V": 5,
                   "X": 10,
                   "L": 50,
                   "C": 100,
                   "D": 500,
                   "M": 1000,
                   "IV": 4,
                   "IX": 9,
                   "XL": 40,
                   "XC": 90,
                   "CD": 400,
                   "CM": 900}
        result = 0
        current_idx = 0

        while current_idx < len(s):
            current_symbol = s[current_idx]
            double_symbols = ""

            if current_idx + 1 < len(s):
                next_symbol = s[current_idx + 1]
                double_symbols = current_symbol + next_symbol

            if double_symbols in symbols:
                result += symbols[double_symbols]
                current_idx += 2

            else:
                result += symbols[current_symbol]
                current_idx += 1

        return result

solution = Solution()
print(solution.romanToInt("MCMXCIV"))





