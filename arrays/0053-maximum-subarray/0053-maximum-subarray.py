class Solution:
    def maxSubArray(self, nums):
        total = 0
        maxi = nums[0]

        for i in range(len(nums)):
            total += nums[i]
            if total > maxi:
                maxi = total
            if total < 0:
                total = 0

        return maxi
