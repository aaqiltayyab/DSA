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

#Explanation:

# Problem setup
# Apples: [1, 3, 2]

# Total apples: 1 + 3 + 2 = 6

# Box capacities: [4, 3, 1, 5, 2]

# Goal: pick the minimum number of boxes whose total capacity ≥ 6.

# Greedy strategy
# Sort capacities descending: pick largest boxes first to reach the required total faster.

# Sorted capacities: [5, 4, 3, 2, 1]

# This ordering ensures each pick contributes the maximum possible capacity at that step, minimizing the count of boxes.

# Step-by-step selection
# Start: cumulative capacity = 0, boxes used = 0, target = 6

# Pick 5: cumulative = 0 + 5 = 5, boxes used = 1

# Check: 5 < 6 → need more capacity

# Pick 4: cumulative = 5 + 4 = 9, boxes used = 2

# Check: 9 ≥ 6 → requirement met

# Result: minimum boxes = 2 (capacities 5 and 4)

