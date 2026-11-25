class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        elif s == t:
            return s

        tFreq = Counter(t)
        minimumLength = len(s) + 1
        minLengthString = ""
        start = 0
        end = 0
        sFreq = {}

        while end < len(s):
            if tFreq[s[end]] != 0:
                sFreq[s[end]] = sFreq.get(s[end], 0) + 1

            while start < end:
                if sFreq.get(s[start], 0) > tFreq[s[start]]:
                    sFreq[s[start]] = sFreq.get(s[start], 0) - 1
                elif tFreq[s[start]] != 0:
                    break
                start += 1

            if sFreq == tFreq:
                currentLength = end-start+1
                if currentLength < minimumLength:
                    minimumLength = currentLength
                    minLengthString = s[start:end+1]
            
            end += 1
            # print(sFreq)
            # print("-".join([str(start), str(end), str(minimumLength)]))

        return minLengthString