# LeetCode 2154 Keep Multiplying Found Values by two

class Solution:
    @staticmethod
    def findFinalValue(nums: list[int], original: int) -> int:
        while True:
            changed = False
            for x in nums:
                if x == original:
                    original *= 2
                    changed = True
                    break  # restart from beginning after update
            if not changed:
                return original


# Tests
print(Solution.findFinalValue([5, 3, 6, 1, 12], 3))      # 24
print(Solution.findFinalValue([8, 19, 4, 2, 15, 3], 2))  # 16
print(Solution.findFinalValue([8, 19, 4, 2, 15, 3], 3))  # 6
