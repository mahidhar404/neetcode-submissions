class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        
        for i in nums:
            counter[i]=counter.get(i,0)+1
            if counter.get(i) > 1:
                return True
        
        return False