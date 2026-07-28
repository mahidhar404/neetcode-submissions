class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}

        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        maxi = 0
        answer = 0
        for key, value in counter.items():
            if value > maxi:
                maxi = value
                answer = key
        return answer
