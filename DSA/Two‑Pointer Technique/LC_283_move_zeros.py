class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointer for position of non-zero elements
        count = 0  
        
        # Step 1: Move all non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        
        # Step 2: Fill remaining positions with zero
        while count < len(nums):
            nums[count] = 0
            count += 1
