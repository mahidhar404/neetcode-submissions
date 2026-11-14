class Solution:
    def maxScore(self, s: str) -> int:
        values = []
        for i in range(len(s)-1):
            l, r = 0,0
            left = s[:i+1]
            right = s[i+1:]
            for i in left:
                if i == '0':
                    l += 1
            for i in right:
                if i == '1':
                    r += 1
            values.append(r+l)
        
        return max(values)