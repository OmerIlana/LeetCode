# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        if root==None:
           return sum==0
        
        if root.left==None and root.right==None:
            return root.val==sum
        
        remainder = sum - root.val
        return self.hasPathSum(root.left, remainder) or self.hasPathSum(root.right, remainder)