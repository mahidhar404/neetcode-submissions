class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for _ in range(len(nums)):
            if nums[0] == val:
                nums.pop(0)
            else:
                nums.append(nums.pop(0))

        return len(nums)   