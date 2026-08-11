from tree_node import TreeNode, build
from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


print(Solution().invertTree(build([1, 2, 3, 4, 5, 6, 7]))) # 1, 3, 2, 7, 6, 5, 4]
#print(Solution().invertTree(build([]))) # []