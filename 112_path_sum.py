# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root == None: return False
        if (root.left == None) and (root.right == None) and  (targetSum == root.val): return True
        if (root.left != None) and self.hasPathSum(root.left, targetSum - root.val): return True
        if (root.right != None) and self.hasPathSum(root.right, targetSum - root.val): return True
        return False

print(
    Solution().hasPathSum(n=38)
)