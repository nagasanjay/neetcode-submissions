class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counterMap = {}

        for index, num in enumerate(nums):
            otherHalf = target - num
            if counterMap.get(otherHalf) is not None:
                return [counterMap.get(otherHalf), index]
            
            counterMap[num] = index

        return [-1, -1] # just a return to indicate error