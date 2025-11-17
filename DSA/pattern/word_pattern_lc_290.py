#leetcode = 290 word pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        # Length mismatch → fail
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for c, w in zip(pattern, words):
            # If char already mapped, check consistency
            if c in char_to_word and char_to_word[c] != w:
                return False
            # If word already mapped, check consistency
            if w in word_to_char and word_to_char[w] != c:
                return False

            # Establish mapping
            char_to_word[c] = w
            word_to_char[w] = c

        return True


# --- Testcases ---
print(Solution().wordPattern("abba", "dog cat cat dog"))   # ✅ True
print(Solution().wordPattern("abba", "dog cat cat fish"))  # ❌ False
print(Solution().wordPattern("aaaa", "dog cat cat dog"))   # ❌ False
