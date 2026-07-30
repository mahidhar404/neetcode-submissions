class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for _ in range(len(nums)):
            if nums[0] == val:
                nums.pop(0)
            else:
                nums.append(nums.pop(0))

        k = 0
        for i in nums:
            if i == val:
                break
            k += 1

        return k       