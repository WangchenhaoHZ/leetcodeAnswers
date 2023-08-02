from typing import List

# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
#         trees: List[List] = []
#         for edge in edges:
#             if trees == []: 
#                 trees.append(edge)
#                 continue
#             a, b = edge
#             if_in_trees = False
#             a_tree = []
#             b_tree = []
#             for tree in trees:
#                 if (a in tree) and (b in tree): return edge
#                 if a in tree:
#                     a_tree = tree
#                     if_in_trees = True
#                 if b in tree:
#                     b_tree = tree
#                     if_in_trees = True
#             if a_tree and b_tree:
#                 a_tree.extend(b_tree)
#                 a_tree.append(a)
#                 a_tree.append(b)
#                 trees.remove(b_tree)
#                 continue
#             if a_tree:
#                 a_tree.append(b)
#             if b_tree:
#                 b_tree.append(a)
#             if not if_in_trees:
#                 trees.append(edge)
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        MAX_VERTEX_NUM = 1001
        parent = [i for i in range(MAX_VERTEX_NUM)]
        for edge in edges:
            v1, v2 = edge
            v1_root = parent[v1]
            v2_root = parent[v2]
            while v1_root!= parent[v1_root]:
                v1_root = parent[v1_root]
            while v2_root!= parent[v2_root]:
                v2_root = parent[v2_root]
            if v1_root == v2_root: return edge
            parent[v2_root] = v1_root
            parent[v2] = v1_root
    
print(
    Solution().findRedundantConnection(edges = [[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]])
)