class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A

        lo = 0
        hi = len(A) - 1

        while True:
            i = (lo + hi) // 2
            j = (len(nums1) + len(nums2)) // 2 - i - 2
            
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if (i+1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if (j+1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                lo = lo - 1
            else:
                hi = hi + 1
            