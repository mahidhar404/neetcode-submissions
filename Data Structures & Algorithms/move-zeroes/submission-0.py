class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            else:
                j = i-1 
                while(j >= 0 and nums[j] == 0):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    j -= 1
                
