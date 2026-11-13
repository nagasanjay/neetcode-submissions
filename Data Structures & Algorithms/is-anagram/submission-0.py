class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1Map = Counter(s)
        string2Map = Counter(t)

        return (string1Map - string2Map) == (string2Map - string1Map)