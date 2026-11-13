class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            countArray = [0] * 26
            for character in string:
                countArray[ord(character) - ord('a')] += 1
            result[tuple(countArray)].append(string)
        
        return list(result.values())