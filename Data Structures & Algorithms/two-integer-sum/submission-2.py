class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in numsDict:
                return [numsDict[compliment], i]
            numsDict[num] = i
        
        return - 1