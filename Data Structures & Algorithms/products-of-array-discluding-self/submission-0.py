from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsLength = len(nums)
        prefix = [1] * numsLength
        suffix = [1] * numsLength

        for i in range(1, numsLength):
            prefix[i] = prefix[i-1] * nums[i-1]
            suffix[numsLength - i - 1] = suffix[numsLength - i] * nums[numsLength - i]

        result = []
        for index in range(numsLength):
            result.append(prefix[index] * suffix[index])

        return result
