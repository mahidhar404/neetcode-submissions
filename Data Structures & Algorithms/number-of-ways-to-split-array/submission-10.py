class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n+1)

        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        res = 0
        for i in range(1,n):
            left = prefix[i]
            right = prefix[n] - prefix[i]
            res += 1 if left>= right else 0
        return res