# Leetcode 3074 Apple Resdistribution into boxes


class Solution:
    def minBoxes(self, apple: list[int], capacity: list[int]) -> int:
        total_apples = sum(apple)
        capacity.sort(reverse=True)  # largest boxes first
        used = 0
        curr_capacity = 0

        for box in capacity:
            curr_capacity += box
            used += 1
            if curr_capacity >= total_apples:
                return used
        return used  # though problem guarantees it's always possible
    

obj = Solution()
print(obj.minBoxes([1,3,2], [4,3,1,5,2]))   #  2
print(obj.minBoxes([5,5,5], [2,4,2,7]))     #  4
print(obj.minBoxes([10], [5,5,5,5]))        #  2
print(obj.minBoxes([2,2,2], [3,3,3]))       #  2

