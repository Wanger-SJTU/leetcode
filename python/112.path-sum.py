#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (37.54%)
# Likes:    892
# Dislikes: 292
# Total Accepted:    308K
# Total Submissions: 818.6K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given the below binary tree and sum = 22,
# 
#                           
#                           ⁠     5
#                           ⁠    / \
#                           ⁠   4   8
#                           ⁠  /   / \
#                           ⁠ 11  13  4
#                           ⁠/  \      \
#                          7    2      1
# 
# 
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# 
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        return self.iter(root, sum)
    
    def recur(self, root, target):
        if not root: return False
        if not root.left and not root.right:
            return True if target == root.val else False
        return self.recur(root.left, target- root.val) or\
            self.recur(root.right, target- root.val)

    def iter(self, root, target):
        stack = [root]
        vals  = [root.val]
        while stack:
            cur = stack.pop(-1)
            val = vals.pop(-1)
            if not cur.left and not cur.right and val == target:
                return True
            if cur.left:
                stack.append(cur.left)
                vals.append(val+cur.left.val)
            if cur.right:
                stack.append(cur.right)
                vals.append(val+cur.right.val)
        return False

