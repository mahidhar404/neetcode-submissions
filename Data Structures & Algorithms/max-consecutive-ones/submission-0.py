from enum import Enum
from collections import Counter
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = dict(enumerate(nums))
        cur_seq = 0
        max_seq = 0
        for key, value in enumerate(counter):
            if counter.get(key) == 1:
                cur_seq += 1
                if max_seq < cur_seq:
                    max_seq = cur_seq
            else:
                cur_seq = 0
        
        return max_seq