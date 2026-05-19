# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        q = deque([root])
        level = 0
        while q:
            # try going level by level and getting last in level
            q_size = len(q)
            for i in range(q_size):
                curr = q.popleft()
                if curr.left: # fails here if answer is empty list
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                if i == (q_size - 1):
                    res.append(curr.val)
            level += 1
        
        return res

        