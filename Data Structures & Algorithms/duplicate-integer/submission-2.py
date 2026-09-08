class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # # brute force solution
        # # loop through list
        # for i in range(len(nums)):
        #     # compare current element with next element
        #     for j in range(i + 1, len(nums)):
        #     # if current == next element
        #         if nums[i] == nums[j]:
        #         # return True
        #             return True
        # # return False
        # return False

        # hash set
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False