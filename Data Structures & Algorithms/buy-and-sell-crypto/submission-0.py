class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, total_diff = 0, 0

        for r in range(l+1, len(prices)):
            curr_diff = 0
            if prices[l] > prices[r]:
                l = r
            else:
                curr_diff = prices[r] - prices[l]
                total_diff = max(total_diff, curr_diff)
        
        return total_diff
