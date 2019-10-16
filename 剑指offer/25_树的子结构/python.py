"""
题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def HasSubtree(pRoot1, pRoot2):
    if pRoot1 == None or pRoot2 == None:
        return False
    return pd(pRoot1, pRoot2) or HasSubtree(pRoot1.left, pRoot2) or HasSubtree(pRoot1.right, pRoot2)

def pd(pRoot1, pRoot2):
    if pRoot2 == None:
        return True
    if pRoot1 == None:
        return False
    if pRoot1.val != pRoot2.val:
        return False
    return pd(pRoot1.left, pRoot2.left) and pd(pRoot1.right, pRoot2.right)

if __name__ == '__main__':
    node1 = TreeNode(8)
    node2 = TreeNode(8)
    node3 = TreeNode(7)
    node4 = TreeNode(9)
    node5 = TreeNode(2)
    node6 = TreeNode(4)
    node7 = TreeNode(7)
    node5.left = node6
    node5.right = node7
    node2.left = node4
    node2.right = node5
    node1.left = node2
    node1.right = node3

    cnode1 = TreeNode(8)
    cnode2 = TreeNode(9)
    cnode3 = TreeNode(2)
    cnode1.left = cnode2
    cnode1.right = cnode3
    print(HasSubtree(node1, cnode1))