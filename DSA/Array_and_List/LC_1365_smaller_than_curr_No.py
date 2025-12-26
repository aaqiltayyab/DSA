# LEetcode 1365 how maany numbers are smaller than the current number

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            ans.append(count)
        return ans

# Tests
obj = Solution()
print(obj.smallerNumbersThanCurrent([8,1,2,2,3]))  #  [4,0,1,1,3]
print(obj.smallerNumbersThanCurrent([6,5,4,8]))    #  [2,1,0,3]
print(obj.smallerNumbersThanCurrent([7,7,7,7]))    #  [0,0,0,0]
