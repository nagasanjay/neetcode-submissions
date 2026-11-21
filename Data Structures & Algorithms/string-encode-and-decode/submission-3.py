class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStringArray = []
        for string in strs:
            encodedStringArray.append(str(len(string)))
            encodedStringArray.append("#")
            encodedStringArray.append(string)

        return "".join(encodedStringArray)

    def decode(self, s: str) -> List[str]:
        decodedStrings = []
        lookupIndex = 0

        while lookupIndex < len(s):
            lengthIndex = lookupIndex

            while s[lookupIndex] != "#":
                lookupIndex += 1

            stringLength = int(s[lengthIndex:lookupIndex])

            lookupIndex += 1
            decodedStrings.append(s[lookupIndex:(lookupIndex + stringLength)])
            lookupIndex += stringLength
        
        return decodedStrings
            

            