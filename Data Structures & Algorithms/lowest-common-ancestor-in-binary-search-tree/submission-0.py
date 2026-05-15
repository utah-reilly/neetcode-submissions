# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None or p is None or q is None:
            return None
        
        # Need to find the node where p and q split
        if (p.val <= root.val and q.val >= root.val) or (p.val >= root.val and q.val <= root.val):
            return root
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l is None:
            return r
        if r is None:
            return l

        return min(l, r, key=lambda n: n.val)

