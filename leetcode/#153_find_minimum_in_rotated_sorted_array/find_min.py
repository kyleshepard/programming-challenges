class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        
        # if length is one or array is not rotated
        if nums[l] <= nums[r]:
            return nums[l]
        
        # if l and r are next to each other, r will be the index of the min
        while l < r-1:
            
            pivot = l + (r - l) // 2

            if nums[pivot] > nums[l]:
                l = pivot
            else:
                r = pivot
        
        return nums[r]