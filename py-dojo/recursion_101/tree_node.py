"""Helper de arboles para recursion_101 (copia del que ya usas en neetcode/trees)."""

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        vals = []
        queue = deque([self])
        while queue:
            node = queue.popleft()
            if node:
                vals.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                vals.append(None)
        while vals and vals[-1] is None:
            vals.pop()
        return str(vals)

    __repr__ = __str__


def build(vals: List[Optional[int]]) -> Optional[TreeNode]:
    """Construye un arbol desde la representacion nivel-por-nivel de LeetCode."""
    if not vals:
        return None

    root = TreeNode(vals[0])
    queue = deque([root])

    i = 1
    while queue and i < len(vals):
        parent = queue.popleft()

        if i < len(vals) and vals[i] is not None:
            parent.left = TreeNode(vals[i])
            queue.append(parent.left)
        i += 1

        if i < len(vals) and vals[i] is not None:
            parent.right = TreeNode(vals[i])
            queue.append(parent.right)
        i += 1

    return root
