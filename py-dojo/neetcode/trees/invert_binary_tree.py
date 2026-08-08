from tree_node import TreeNode, build
from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        print(root)


print(Solution().invertTree(build([1, 2, 3, 4, 5, 6, 7]))) # esperado: [1, 3, 2, 7, 6, 5, 4]
#print(Solution().invertTree(build([]))) # esperado: []

