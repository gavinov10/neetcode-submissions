class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the array, loop through nums once, assign l, r pointers
        res = []
        sortedNums = sorted(nums)

        for i, num in enumerate(sortedNums):
            if i > 0 and num == sortedNums[i - 1]:
                continue
            l, r = i + 1, len(sortedNums) - 1
            while l < r:
                threeSum = num + sortedNums[l] + sortedNums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([num, sortedNums[l], sortedNums[r]])
                    l += 1
                    while sortedNums[l] == sortedNums[l - 1] and l < r:
                        l += 1
        return res