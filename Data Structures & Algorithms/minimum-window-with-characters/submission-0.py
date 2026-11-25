class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        sFreq = Counter(s)
        tFreq = Counter(t)

        for character, count in tFreq.items():
            if sFreq[character] < count:
                return ""

        left = 0
        right = len(s) - 1

        while left < right:
            if sFreq[s[left]] > tFreq[s[left]]:
                sFreq[s[left]] -= 1
                left += 1
            elif sFreq[s[right]] > tFreq[s[right]]:
                sFreq[s[right]] -= 1
                right -= 1
            else:
                break

        return s[left : right+1]