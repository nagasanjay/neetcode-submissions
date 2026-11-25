class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(s) < len(t):
            return ""
        
        if s == t:
            return s

        countS , countT = {}, {}
        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i], 0) + 1

        need, have = len(countT), 0
        start, end = 0, 0
        minLength = len(s) + 1
        minString = ""

        while end < len(s):
            countS[s[end]] = countS.get(s[end], 0) + 1
            if s[end] in countT and countS[s[end]] == countT[s[end]]:
                have += 1
            
            while need == have:
                if s[start] not in countT:
                    countS[s[start]] -= 1
                    start += 1
                elif countS[s[start]] > countT[s[start]]:
                    countS[s[start]] -= 1
                    start += 1
                else:
                    break
            
            if need == have and minLength > (end - start + 1):
                minString = s[start:end+1]
                minLength = end - start + 1
            
            end += 1
        
        return minString

                