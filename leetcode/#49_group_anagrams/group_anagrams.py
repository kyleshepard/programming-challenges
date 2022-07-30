class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # hashmap that maps sorted strings to indices in the input string
        hashmap = {}
        
        # loop over all elements in input array
        for word_index in range(len(strs)):
            # create/update entry in hashmap with the pre-sorted string added
            sorted_word = ''.join(sorted(strs[word_index]))
            hashmap[sorted_word] = hashmap.get(sorted_word, []) + [strs[word_index]]
        
        return hashmap.values()
                