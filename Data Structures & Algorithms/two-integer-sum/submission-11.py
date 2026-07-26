class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}

        for key, value in enumerate(nums):
            check = target - value
            if check in counter:
                return [counter[check], key]
            counter[value] = key
      
