class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]

        left = nums1[:m]
        i, j, c = 0, m, 0

        while i < m and j < m+n:
            if left[i] <= nums1[j]:
                nums1[c] = left[i]
                i += 1
            else:
                nums1[c] = nums1[j]
                j += 1
            c += 1

       
        while i < m:
            nums1[c] = left[i]
            i += 1
            c += 1
        while j < m+n:
            nums1[c] = nums1[j]
            j += 1
            c += 1