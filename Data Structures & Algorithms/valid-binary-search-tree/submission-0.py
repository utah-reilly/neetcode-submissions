# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def nodeValid(root, left, right):
            if not root:
                return True
            if not (left < root.val < right):
                return False

            return nodeValid(root.left, left, root.val) and nodeValid(root.right, root.val, right)
        
        return nodeValid(root, float("-inf"), float("inf"))