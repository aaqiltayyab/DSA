# LeetCode 1018: Binary Prefix Divisible By 5


class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        ans = []
        num = 0
        for bit in nums:
            num = (num * 2 + bit) % 5   # only keep remainder to avoid overflow
            ans.append(num == 0)
        return ans


# --- Test ---
obj = Solution()
print(obj.prefixesDivBy5([0,1,1]))        # [True, False, False]
print(obj.prefixesDivBy5([1,1,1]))        # [False, False, False]
print(obj.prefixesDivBy5([0,1,1,1,1,1]))  # [True, False, False, False, True, False]


# Explanation
# Input: [0,1,1,1,1,1]

# Prefixes: 0 → 0, 01 → 1, 011 → 3, 0111 → 7, 01111 → 15, 011111 → 31.

# Divisible by 5: 0 true, 1 false, 3 false, 7 false, 15 true, 31 false.

# Output: [True, False, False, False, True, False].


#  Example Dry Run: nums = [0,1,1,1,1,1]
# Step	bit	Calculation	num (remainder)	Divisible?	ans list
# 1	0	(0*2 + 0) % 5 = 0	0	 True	[True]
# 2	1	(0*2 + 1) % 5 = 1	1	 False	[True, False]
# 3	1	(1*2 + 1) % 5 = 3	3	 False	[True, False, False]
# 4	1	(3*2 + 1) % 5 = 7 % 5 = 2	2	 False	[True, False, False, False]
# 5	1	(2*2 + 1) % 5 = 5 % 5 = 0	0	 True	[True, False, False, False, True]
# 6	1	(0*2 + 1) % 5 = 1	1	 False	[True, False, False, False, True, False]
