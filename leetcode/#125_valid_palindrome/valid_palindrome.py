class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # convert string into something we can easily read without whitespace/punctuation/captials
        formatted = ''.join(i for i in s.lower() if i.isalnum())
        
        for index in range(len(formatted)):
            if index >= len(formatted) - index - 1:
                break
            
            if formatted[index] != formatted[len(formatted) - index - 1]:
                return False
        
        # if we reach this, we have encountered no mismatched characters
        return True
        