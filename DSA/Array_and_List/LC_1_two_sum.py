class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # check all pairs
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

obj = Solution()
print(obj.twoSum([2,7,11,15], 9))   #  [0,1]
print(obj.twoSum([3,2,4], 6))       #  [1,2]
print(obj.twoSum([3,3], 6))         #  [0,1]
