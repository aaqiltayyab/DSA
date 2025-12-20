# LEet code 1470 Shuffle the Array

class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        result = []
        for i in range(n):
            j = n + i
            result.append(nums[i])
            result.append(nums[j])
        return result