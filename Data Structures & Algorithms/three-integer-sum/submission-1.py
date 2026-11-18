class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        current = 0
        result = []
        
        while current < len(nums) and nums[current] <= 0:
            left = current + 1
            right = len(nums) - 1

            target = -nums[current]

            while left < right:
                if nums[left] + nums[right] == target:
                    result.append([nums[current], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while right > left and nums[right] == nums[right+1]:
                        right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
            
            current += 1
            while current < len(nums) - 2 and nums[current] == nums[current-1]:
                current += 1
        
        return result
