class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap of value to index
        hashmap = {};
        
        for i in range(len(nums)):
            
            pair = hashmap.get(target-nums[i], -1)
            
            if pair >= 0:
                return [pair, i]
            
            hashmap[nums[i]] = i
            
        return [-1,-1]