class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # add nums to a set
        numsSet = set()
        for num in nums:
            numsSet.add(num)

        count = 1
        maxSequence = 1

        # check for sequence
        for num in numsSet:
            if num - 1 not in numsSet:
                curr = num
                while curr + 1 in numsSet:
                    count += 1
                    curr += 1
            else:
                count = 1
            
            if maxSequence < count:
                maxSequence = count
        
        return maxSequence
