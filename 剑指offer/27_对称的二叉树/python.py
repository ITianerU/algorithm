"""
题目描述
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""
import copy
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        root = copy.deepcopy(pRoot)
        self.Mirror(pRoot)
        return self.equal(pRoot, root)

    def Mirror(self, root):
        if root == None:
            return root
        temp = root.left
        root.left = root.right
        root.right = temp
        root.left = self.Mirror(root.left)
        root.right = self.Mirror(root.right)
        return root

    def equal(self, root1, root2):
        if not root1 and not root2:
            return True
        if (not root1 and root2) or (not root2 and root1):
            return False
        if root1.val == root2.val:
            return self.equal(root1.left, root2.left) and self.equal(root1.right, root2.right)
        else:
            return False


if __name__ == '__main__':
    node1 = TreeNode(8)
    node2 = TreeNode(6)
    node3 = TreeNode(9)
    node4 = TreeNode(5)
    node5 = TreeNode(7)
    node6 = TreeNode(7)
    node7 = TreeNode(5)

    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node1.left = node2
    node1.right = node3

    test = Solution()
    print(test.isSymmetrical(node1))

