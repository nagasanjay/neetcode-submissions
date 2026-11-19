class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLength = 0
        charactersPresent = set()

        for right in range(len(s)):
            while s[right] in charactersPresent:
                charactersPresent.remove(s[left])
                left += 1
            charactersPresent.add(s[right])
            maxLength = max(maxLength, right - left + 1)

        return maxLength
