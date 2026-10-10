class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minNum = float("inf")

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
                minNum = min(minNum, nums[mid])
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                minNum = nums[mid]
                break

        return minNum

