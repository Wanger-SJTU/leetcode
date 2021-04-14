#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (29.16%)
# Likes:    2060
# Dislikes: 91
# Total Accepted:    210.1K
# Total Submissions: 719.1K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
# 
# Example 1:
# 
# 
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# 
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
#
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return None
        locMin = locMax = gloMax = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                tmp = locMax
                locMax = max(locMin*nums[i], nums[i])
                locMin = min(tmp*nums[i], nums[i])
            else:
                locMax = max(locMax*nums[i], nums[i])
                locMin = min(locMin*nums[i], nums[i])
            gloMax = max(gloMax, locMax)
        return gloMax



