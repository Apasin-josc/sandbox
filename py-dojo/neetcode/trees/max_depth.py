from tree_node import TreeNode, build
from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)


print(Solution().maxDepth(build([1,2,3,None,None,4])))