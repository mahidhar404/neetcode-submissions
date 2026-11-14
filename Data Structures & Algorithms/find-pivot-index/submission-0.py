class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        nums_reversed = nums[::-1]
        post = []
        total = 0
        total_post = 0
        for n in nums:
            total += n
            prefix.append(total)
        for n in nums_reversed:
            total_post += n
            post.append(total_post)
        post = post[::-1]
        
        for i in range(len(post)):
            if post[i] == prefix[i]:
                return i
        
        return -1