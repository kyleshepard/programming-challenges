class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # sort the array so we can easily skip duplicates
        nums.sort()
        solutions = []
        
        for i, n in enumerate(nums):
            # place i at next non-duplicate
            if i > 0 and n == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1
            while l<r:
                threeSum = n + nums[l] + nums[r]
                if threeSum > 0:
                    r = r-1
                elif threeSum < 0:
                    l = l+1
                else:
                    solutions.append([n, nums[l], nums[r]])
                    # be sure to continue to the next non-duplicate l value
                    l = l+1
                    while nums[l] == nums[l-1] and l<r:
                        l = l+1
                    # we don't need to decrement the r pointer to a non-duplicate value because it will happen automatically since it will only change when (n+l+r) > 0, and a duplicate r will just be decremented automatically implicitly
                
        return solutions