class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = Counter(s1)
        s2Count = Counter()

        windowLength = len(s1)
        for index in range(windowLength):
            s2Count[s2[index]] += 1

        if s1Count == s2Count:
            return True
        
        for index in range(windowLength, len(s2)):
            s2Count[s2[index - windowLength]] -= 1
            s2Count[s2[index]] += 1
            if s1Count == s2Count:
                return True
        
        return False
