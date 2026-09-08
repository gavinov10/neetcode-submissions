class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}    # value -> index
        for i, num in enumerate(nums):
            complementNumber = target - num
            if complementNumber in prevMap:
                return [prevMap[complementNumber], i]
            prevMap[num] = i
        
                