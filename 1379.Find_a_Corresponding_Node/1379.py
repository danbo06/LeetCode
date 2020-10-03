https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def it(node):
            if node:
                yield node
                yield from it(node.left)
                yield from it(node.right)
            
        for n1, n2 in zip(it(original), it(cloned)):
            if n1 == target:
                return n2
    
# BFS
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.path = []
        self.found = False
        def dfs(node, path, target):
            if self.found:
                return
            if not node:
                return
            if node == target:
                self.path = path
                self.found = True
                return
            dfs(node.left, path + [0], target)
            dfs(node.right, path + [1], target)

        dfs(original, [], target)
        node = cloned
        for p in self.path:
            if p:
                node = node.right
            else:
                node = node.left
        return node