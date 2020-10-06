https://leetcode.com/problems/deepest-leaves-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def dfs(node, level):
            if not node.left and not node.right: #Leaf
                levels[level] += node.val
            if node.left:
                dfs(node.left, level+1)
            if node.right:
                dfs(node.right, level+1)
                
        if not root:
            return 0
        levels = collections.defaultdict(int)
        dfs(root, 0)
        deepest_level = sorted(levels.keys())[-1]
        return levels[deepest_level]

    
    def deepestLeavesSum(self, root):
        q = [root]
        while q:
            pre, q = q, [child for p in q for child in [p.left, p.right] if child]
        return sum(node.val for node in pre)