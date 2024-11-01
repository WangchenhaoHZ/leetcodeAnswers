from typing import Optional
import copy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class TreeNode:
    def __init__(self, ls, index = 0):
        self.ls =ls
        self.index = index
    
    @property
    def left(self):
        if (2*self.index + 1<len(self.ls)) and (self.ls[2*self.index + 1]):
            return TreeNode(self.ls, 2*self.index + 1)
        else:
            return None
    
    @property
    def right(self):
        if (2*(self.index + 1)<len(self.ls)) and (self.ls[2*(self.index + 1)]):
            return TreeNode(self.ls, 2*(self.index + 1))
        else:
            return None
    @property
    def val(self):
        return self.ls[self.index]
        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.find(root, targetSum, 0, {0:1})
    
    def find(self, root: Optional[TreeNode], targetSum: int, preffix_sum:int, cnt:dict):
        ans = 0
        if root == None: return 0
        preffix_sum_now = preffix_sum
        preffix_sum_now += root.val
        cnt_now = copy.deepcopy(cnt)
        if preffix_sum_now - targetSum in cnt.keys():
            ans += cnt[preffix_sum_now - targetSum]
        # the summation of subarray must contain prescent element should be the total summation til prescent element minus 
        # the possible summation of <<former>> proper initial segments
        # so should use cnt, rather than cnt_now
        
        if preffix_sum_now in cnt_now.keys():
            cnt_now[preffix_sum_now] += 1
        else:
            cnt_now[preffix_sum_now] = 1
        
        if root.right:
            ans += self.find(root.right, targetSum, preffix_sum_now, cnt_now)
        if root.left:
            ans += self.find(root.left, targetSum, preffix_sum_now, cnt_now)
        return ans
    
print(
    Solution().pathSum(TreeNode([1]), 0)
)