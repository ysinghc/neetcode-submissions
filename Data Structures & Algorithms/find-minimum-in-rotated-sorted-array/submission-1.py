class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        ans = nums[l]

        while l <= r:
            if nums[l] < nums[r]:
                ans = min(ans, nums[l])
                break
            
            m = l + (r-l)//2
            ans = min(ans, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m-1
        
        return ans