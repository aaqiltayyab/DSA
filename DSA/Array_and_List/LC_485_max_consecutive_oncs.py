# Leetcode 485_max_consecutive_oncs
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_cons = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                max_cons = max(max_cons, count)
            else:
                count = 0   # reset count when 0 encountered
        return max_cons
    

obj = Solution()
print(obj.findMaxConsecutiveOnes([1,1,0,1,1,1]))  #  3
print(obj.findMaxConsecutiveOnes([0,0,0]))        #  0
print(obj.findMaxConsecutiveOnes([1,1,1,1]))      #  4

