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


def build(vals: List[Optional[int]]) -> Optional[TreeNode]:
    if not vals:
        return None

    root = TreeNode(vals[0])
    queue = deque([root])

    i = 1
    while queue and i < len(vals):
        parent = queue.popleft()

        if i < len(vals) and vals[i] is not None:
            parent.left = TreeNode(vals[i])
            queue.append(parent.left)  # el hijo tambien recibira hijos despues
        i += 1

        if i < len(vals) and vals[i] is not None:
            parent.right = TreeNode(vals[i])
            queue.append(parent.right)
        i += 1

    return root


if __name__ == "__main__":
    root = build([3, 9, 20, None, None, 15, 7])
    print(root)          # -> [3, 9, 20, None, None, 15, 7]
    print(root.val)      # -> 3
    print(root.left.val)  # -> 9
    print(root.right.left.val)  # -> 15
