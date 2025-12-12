# Leet code 1929. Concatenation of Array

#  Simplest Solution

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums


# Little Complex
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        i = 1
        ans = []
        while i <=2:
            for j in range(len(nums)):
                ans.append(nums[j])
            i+=1
        return ans
    

obj = Solution()
print(obj.getConcatenation([1,2,1]))   #  [1,2,1,1,2,1]
print(obj.getConcatenation([1,3,2,1])) #  [1,3,2,1,1,3,2,1]


# Explanation
# nums + nums → Python me list concatenation hota hai.

# Agar nums = [1,2,1] hai → [1,2,1] + [1,2,1] = [1,2,1,1,2,1].

# Ye exactly wahi output deta hai jo problem statement me expected hai.
