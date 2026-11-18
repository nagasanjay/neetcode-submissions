class Solution:
    def trap(self, height: List[int]) -> int:
        totalLength = len(height)
        if totalLength == 0:
            return 0
        
        leftMax = [0] * totalLength
        rightMax = [0] * totalLength

        leftMax[0] = height[0]
        for i in range(1, totalLength):
            leftMax[i] = max(height[i], leftMax[i-1])
            
        rightMax[totalLength-1] = height[totalLength-1]
        for i in range(totalLength - 2, -1, -1):
            rightMax[i] = max(height[i], rightMax[i+1])

        waterStored = 0
        for i in range(totalLength):
            waterStored += min(leftMax[i], rightMax[i]) - height[i]

        return waterStored