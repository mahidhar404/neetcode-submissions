class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        counter = {}
        str_len = len(strs[0])
        for i in range(len(strs[0])):
            counter[i] = strs[0][i]
        
        for i in range(1,len(strs)):
            match_len = 0
            for c in range(len(strs[i])):
                if c in counter and strs[i][c] == counter[c]:
                    match_len += 1
                    continue
                else:
                    break
            str_len = min(str_len, match_len)
        res = ""
        for i in range(str_len):
            res += counter[i]
        
        return res