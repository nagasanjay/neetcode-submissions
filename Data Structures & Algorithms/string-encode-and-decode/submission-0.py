class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for string in strs:
            encodedString += str(len(string)) + "#" + string

        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedStrings = []
        lookupIndex = 0
        while lookupIndex < len(s):
            lengthString = ""
            actualString = ""

            while s[lookupIndex] != '#':
                lengthString += s[lookupIndex]
                lookupIndex += 1
            lookupIndex += 1

            stringLength = int(lengthString)
            while stringLength > 0:
                actualString += s[lookupIndex]
                lookupIndex += 1
                stringLength -= 1

            decodedStrings.append(actualString)
        
        return decodedStrings
                