class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0 , len(nums) - 1
        
        while left <= right:
            mid = left + (right-left)//2
            left_val = nums[left]
            mid_val = nums[mid]
            right_val = nums[right]
            
            if mid_val == target:
                return mid
            
            # left to mid is sorted
            if left_val <= mid_val:
                # if target is between left and mid, elminate everything right of mid
                if left_val <= target <= mid_val:
                    right = mid-1
                # if target is not between left and mid, elminate everything left of mid
                else:
                    left = mid+1
            # mid + 1 to right is sorted
            else:
                # if target is between mid and right, elminate everything left of mid
                if mid_val <= target <= right_val:
                    left = mid+1
                # if target is not between mid and right, elminate everything right of mid
                else:
                    right = mid-1
        
        return -1