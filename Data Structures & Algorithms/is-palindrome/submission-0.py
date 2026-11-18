import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanText = re.sub(r'[^a-zA-Z0-9]', '', s)
        start = 0
        end = len(cleanText) - 1


        while start < end:
            if cleanText[start].lower() != cleanText[end].lower():
                return False
            start += 1
            end -= 1
        
        return True