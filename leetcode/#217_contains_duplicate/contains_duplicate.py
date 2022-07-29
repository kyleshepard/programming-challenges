class Solution:
    # solution using sets and for loop
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        
        for x in nums:
            if x in num_set:
                return True
            else:
                num_set.add(x)
        
        return False

    # simpler solution that runs faster on average
    def anotherSolution(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))
