class Solution:
    def trap(self, height: List[int]) -> int:
        storedWater = 0
        waterInGap = 0
        index1 = 0
        index2 = 1

        while index2 < len(height):
            if height[index2] < height[index1]:
                waterInGap += (height[index1] - height[index2])
            else:
                storedWater += waterInGap
                waterInGap = 0
                index1 = index2
            index2 += 1
        
        return storedWater