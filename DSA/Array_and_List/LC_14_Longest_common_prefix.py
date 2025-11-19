def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Take the first string as reference
    prefix = strs[0]
    
    # Compare with each string
    for s in strs[1:]:
        # Reduce prefix until it matches the start of s
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    
    return prefix


# Example usage
print(longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(longestCommonPrefix(["dog","racecar","car"]))     # Output: ""
