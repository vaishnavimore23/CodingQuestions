# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False

        elif p.val != q.val:
            return False
        else:
            print("in else case")
            if p.left and q.left and p.left.val == q.left.val:
                self.isSameTree(p.left, q.left)
                return True
            if q.right and p.right and p.right.val == q.right.val:
                self.isSameTree(p.right, q.right)
                return True

    isSameTree([1, 2, 3], [1, 2, 3])
