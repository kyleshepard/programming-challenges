class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        def getDictionary(s: str) -> dict:
            dictionary = dict()
        
            for l in range(len(s)):
                char = s[l:l+1]
                dictionary[char] = dictionary.get(char, 0) + 1
                    
            return dictionary
    
        return (len(s) == len(t)) & (getDictionary(s) == getDictionary(t))