# LeetCode - 9 : Palindrome
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert integer to string for easy indexing
        x_str = str(x)
        for i in range(len(x_str) // 2):
            if x_str[i] != x_str[len(x_str) - i - 1]:
                return False
        return True


# Test
print(Solution().isPalindrome(121))   #  True
print(Solution().isPalindrome(123))   #  False
