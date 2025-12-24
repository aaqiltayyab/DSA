# LeetCode 645: Set Mismatch

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        seen = set()
        duplicate = -1

        # find duplicate
        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)

        # find missing
        exp = n * (n + 1) // 2
        act = sum(nums)
        missing = exp - (act - duplicate)

        return [duplicate, missing]
    

obj = Solution()
print(obj.findErrorNums([1,2,2,4]))  #  [2,3]
print(obj.findErrorNums([1,1]))      #  [1,2]
print(obj.findErrorNums([2,2]))      #  [2,1]

#Explanation:
# Example Dry Run: nums = [1,2,2,4]
# n = 4

# seen = {} initially

# Loop:

# 1 → not in seen → add → seen = {1}

# 2 → not in seen → add → seen = {1,2}

# 2 → already in seen → duplicate = 2

# 4 → not in seen → add → seen = {1,2,4}

# Duplicate = 2

# exp = 4*5//2 = 10

# act = sum([1,2,2,4]) = 9

# missing = 10 - (9 - 2) = 10 - 7 = 3

#  Answer = [2,3]

# Final Output
# Duplicate number → 2
# Missing number → 3
# Return → [2,3]

