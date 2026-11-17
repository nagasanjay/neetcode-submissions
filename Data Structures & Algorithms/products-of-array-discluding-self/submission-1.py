class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroIndex = -1
        resultArray = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                if zeroIndex == -1:
                    zeroIndex = i
                else:
                    return resultArray
            else:
                product *= nums[i]

        if zeroIndex != -1:
            resultArray[zeroIndex] = product
            return resultArray

        for i, num in enumerate(nums):
            resultArray[i] = product // num

        return resultArray