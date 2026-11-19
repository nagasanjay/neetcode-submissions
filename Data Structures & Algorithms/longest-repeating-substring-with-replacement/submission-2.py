class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        maxFrequency = 0
        stringLength = 0

        for right in range(len(s)):
            count[s[right]] += 1
            maxFrequency = max(maxFrequency, count[s[right]])

            if (right - left + 1) - maxFrequency > k:
                count[left] -= 1
                left += 1
            
            stringLength = max(stringLength, right - left + 1)
        
        return stringLength