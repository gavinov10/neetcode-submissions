class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        
        for num in nums_set:
            if num - 1 not in nums_set:
                currLength = 1
                while num + currLength in nums_set:
                    currLength += 1

                longest = max(longest, currLength)
        return longest
