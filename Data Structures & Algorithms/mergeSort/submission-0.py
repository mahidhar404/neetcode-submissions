# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, pairs: List[Pair], start, middle, end):
        # Copy the sorted left & right halfs to temp arrays
        left = pairs[start : middle+1]
        right = pairs[middle+1: end+1]

        i = 0 
        j = 0 
        k = start 
        
        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                pairs[k] = left[i]
                i += 1
            else:
                pairs[k] = right[j]
                j += 1
            k += 1

        
        while i < len(left):
            pairs[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            pairs[k] = right[j]
            j += 1
            k += 1





        
    def mergeSort(self, pairs: List[Pair], start= 0, end= None) -> List[Pair]:
        if end is None:
            end = len(pairs) - 1
        if (end - start + 1) <= 1:
            return pairs
        
        middle = (start + end) // 2

        self.mergeSort(pairs, start, middle)
        self.mergeSort(pairs, middle+1, end)

        self.merge(pairs, start, middle, end)

        return pairs