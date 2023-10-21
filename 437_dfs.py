# Definition for a binary tree node.
from typing import Optional
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

class Counter:
    def __init__(self) -> None:
        self.count = 0
    
    def add(self, n):
        self.count += n
     
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        ans = Counter()
        self.find(root, targetSum, {0:1}, ans, 0)
        return ans.count
        
    def find(self, root: Optional[TreeNode], targetSum: int,
                prefixsum_fromroot_counter_hashtable: dict, path_count: Counter, former_sum:int):
        sum = former_sum + root.val
        
        if sum - targetSum in prefixsum_fromroot_counter_hashtable:
            path_count.add(prefixsum_fromroot_counter_hashtable[sum - targetSum])
        
        if sum not in prefixsum_fromroot_counter_hashtable:
            prefixsum_fromroot_counter_hashtable[sum] = 1
        else:
            prefixsum_fromroot_counter_hashtable[sum] += 1
        
        if root.left: 
            self.find(root.left, targetSum, prefixsum_fromroot_counter_hashtable, path_count, sum)
        if root.right: 
            self.find(root.right, targetSum, prefixsum_fromroot_counter_hashtable, path_count, sum)

            
        if prefixsum_fromroot_counter_hashtable[sum] == 1:
            prefixsum_fromroot_counter_hashtable.pop(sum)
        else:
            prefixsum_fromroot_counter_hashtable[sum] -= 1
        
    
print(
    Solution().pathSum(root = TreeNode([1]), targetSum = 0)
)