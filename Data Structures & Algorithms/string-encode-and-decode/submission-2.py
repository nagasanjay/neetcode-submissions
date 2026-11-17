class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for string in strs:
            encodedString += str(len(string)) + "#" + string
        
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedStringsArray = []
        lookupIndex = 0

        while lookupIndex < len(s):
            lengthString = ""

            while s[lookupIndex] != "#":
                lengthString += s[lookupIndex]
                lookupIndex += 1
            lookupIndex += 1
            
            decodedStringsArray.append(s[lookupIndex : (lookupIndex + int(lengthString))])
            lookupIndex += int(lengthString)

        return decodedStringsArray

            
            