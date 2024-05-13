#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, depth):
            if not root:
                return depth
            left = dfs(root.left, depth+1)
            right = dfs(root.right, depth+1)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right)
        return dfs(root, 0) != -1
    
          
# @lc code=end

