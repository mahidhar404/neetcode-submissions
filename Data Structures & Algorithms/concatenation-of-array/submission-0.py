class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length_of_nums = len(nums)
        ans = [0] * length_of_nums * 2

        for i in range(len(ans)):
            if i < len(ans)//2:           
                ans[i] = nums[i]
            else:
                ans[(i-len(nums))+length_of_nums] = nums[i-length_of_nums]
    
        return ans