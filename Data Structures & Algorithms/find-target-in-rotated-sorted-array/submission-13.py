class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            else :
                if nums[mid] <= target <= nums[hi]:
                    lo = mid
                else:
                    hi = mid - 1
        return lo if nums[lo] == target else -1
