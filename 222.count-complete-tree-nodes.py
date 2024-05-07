#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        res = []
        def preorder(root):
            if root is None:
                return res
            else:
                res.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return len(res)
# @lc code=end

