# LeetCode 7: Reverse Integer


class Solution:
    def reverse(self, x: int) -> int:
        # Signed 32-bit integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Handle sign
        sign = -1 if x < 0 else 1
        x = abs(x)

        # Reverse digits using string
        rev_str = str(x)[::-1]
        rev_int = int(rev_str) * sign

        # Check 32-bit range
        if rev_int < INT_MIN or rev_int > INT_MAX:
            return 0
        return rev_int


# --- Tests ---
obj = Solution()
print(obj.reverse(123))    #  321
print(obj.reverse(-123))   #  -321
print(obj.reverse(120))    #  21
print(obj.reverse(1534236469))  #  0 (overflow case)
