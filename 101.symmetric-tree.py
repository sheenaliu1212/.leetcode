#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def preorder(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return preorder(p.left, q.right) and preorder(p.right, q.left)
        if not root:
            return True
        return preorder(root.left, root.right)
# @lc code=end

