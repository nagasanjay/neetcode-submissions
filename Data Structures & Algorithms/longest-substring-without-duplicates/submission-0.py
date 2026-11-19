class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        characterIndex = {}
        maxLength = 0

        for right in range(len(s)):
            if s[right] in characterIndex:
                left = max(characterIndex[s[right]] + 1, left)
            characterIndex[s[right]] = right
            maxLength = max(maxLength, right - left + 1)

        return maxLength