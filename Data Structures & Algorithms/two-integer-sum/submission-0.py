class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # optimal solution
        prev = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in prev:
                return [prev[complement], i]
            prev[num] = i
    
        # brute force solution
        # loop through array
        # for i in range(len(nums)):
        #     # second pointer comparing the next element with prev
        #     for j in range(i + 1, len(nums)):
        #         # does num i + num j = the target number
        #         if nums[i] + nums[j] == target:
        #             # return the indices
        #             return [i, j]
        # return []