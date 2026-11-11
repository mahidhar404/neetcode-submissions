class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # window size is k+1
        window_set = set()
        l = 0

        for r in range(len(nums)):

    
            if r-l+1 > k+1:
                window_set.remove(nums[l])
                l += 1
            if nums[r] in window_set and r-l+1 <= k+1:
                return True
            window_set.add(nums[r])

        return False
