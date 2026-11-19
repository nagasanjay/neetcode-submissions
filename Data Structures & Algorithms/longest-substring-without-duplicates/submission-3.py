class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        characterIndex = {}
        stringLength = 0
        maxLength = len(set(s))

        for right in range(len(s)):
            if s[right] in characterIndex:
                left = max(characterIndex[s[right]] + 1, left)
            characterIndex[s[right]] = right
            stringLength = max(stringLength, right - left + 1)

            if stringLength == maxLength:
                break

        return stringLength