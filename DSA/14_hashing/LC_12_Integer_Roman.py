# Leetcode 12, Integer to Roman


d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

class Solution:
    def intToRoman(self, num: int) -> str:
        # ordered list of values and symbols including subtractive forms
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]

        res = ""
        for v, s in zip(values, symbols):
            while num >= v:
                res += s
                num -= v
        return res


# --- Tests ---
obj = Solution()
print(obj.intToRoman(3749))  #  "MMMDCCXLIX"
print(obj.intToRoman(58))    #  "LVIII"
print(obj.intToRoman(1994))  #  "MCMXCIV"



# Explanation
# Humne dictionary d reference ke liye rakha hai (values of symbols).
# Lekin conversion ke liye ek ordered list banayi jisme subtractive forms bhi include hain:
# 900 → "CM", 400 → "CD", 90 → "XC", 40 → "XL", 9 → "IX", 4 → "IV".
# Har step pe check karte hain ki num ≥ value hai ya nahi.
# Agar hai → symbol append karte hain aur num se subtract karte hain.
# Loop chalta hai jab tak number 0 nahi ho jata.

# ## Example Dry Run: num = 3749
# 1000 → "M" × 3 → "MMM", remainder = 749
# 500 → "D" × 1 → "MMMD", remainder = 249
# 100 → "C" × 2 → "MMDC C", remainder = 49
# 40 → "XL" → "MMDC CXL", remainder = 9
# 9 → "IX" → "MMDC CXLIX", remainder = 0

# Final result: "MMMDCCXLIX"
