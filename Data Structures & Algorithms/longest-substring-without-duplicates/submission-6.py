class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, length = 0, 0
        temp_set = set()
        for r in range(len(s)):
            while s[r] in temp_set:
                temp_set.remove(s[l])
                l += 1
            temp_set.add(s[r])
            length = max(r-l+1, length)
        return length
        