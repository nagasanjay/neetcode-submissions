class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequenceStart = []
        seen = set(nums)

        for num in seen:
            if num-1 not in seen:
                sequenceStart.append(num)

        maxLength = 0
        for start in sequenceStart:
            length = 1
            while (start + length) in seen:
                length += 1
            maxLength = max(maxLength, length)

        return maxLength