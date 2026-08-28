class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1
        mid = (hi + lo) // 2

        while lo <= hi:
            if nums[mid] > target:
                hi = mid-1
                mid = (hi + lo) // 2
            elif nums[mid] < target:
                lo = mid + 1
                mid = (hi + lo) // 2
            else:
                return mid
        return -1
