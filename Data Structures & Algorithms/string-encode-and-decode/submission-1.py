class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStrings = []
        for string in strs:
            encodedStrings.append(str(len(string)))
            encodedStrings.append("#")
            encodedStrings.append(string)

        return ''.join(encodedStrings)

    def decode(self, s: str) -> List[str]:
        index1 = 0
        index2 = 0
        decodedStrings = []

        while index2 < len(s):
            while s[index2] != "#":
                index2 += 1

            stringLength = int(s[index1:index2])
            index2 += 1

            decodedStrings.append(s[index2:(index2 + stringLength)])
            index2 = index2 + stringLength
            index1 = index2
            
        return decodedStrings