# LeetCode-13 : Roman TO Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50,
             "C": 100, "D": 500, "M": 1000}
        
        total = 0
        # Iterate through string with index
        for i in range(len(s)):
            # If current value < next value → subtract
            if i + 1 < len(s) and d[s[i]] < d[s[i + 1]]:
                total -= d[s[i]]
            else:
                total += d[s[i]]
        
        return total


# --- Testcases ---
print(Solution().romanToInt("III"))     # 3
print(Solution().romanToInt("IV"))      # 4
print(Solution().romanToInt("IX"))      # 9
print(Solution().romanToInt("LVIII"))   # 58
print(Solution().romanToInt("MCMXCIV")) # 1994
