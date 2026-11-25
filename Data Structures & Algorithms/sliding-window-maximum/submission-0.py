class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        currentMax = max(nums[:k])
        result = [currentMax]
        for i in range(k, len(nums)):
            currentMax = max(currentMax, nums[i-k], nums[i])
            result.append(currentMax)

        return result
