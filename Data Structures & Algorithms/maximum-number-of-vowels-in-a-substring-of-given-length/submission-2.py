class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_sub = 0
        window_vowels = 0
        l = 0
        window = []
        for r in range(len(s)):
            if r-l+1 > k:
                if s[l] in ['a', 'e','i', 'o','u']:
                    window_vowels -= 1
                window.remove(s[l])
                l += 1
            if s[r] in ['a', 'e','i', 'o','u']:
                window_vowels += 1
            window.append(s[r])
            max_sub = max(window_vowels, max_sub)
        
        return max_sub

                

