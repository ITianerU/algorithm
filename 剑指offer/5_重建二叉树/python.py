"""
题目描述
根据二叉树的前序遍历和中序遍历的结果，重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

解题思路
前序遍历的第一个值为根节点的值，在中序遍历中根节点值左边为左子树，右边为右子树，使用这个值将中序遍历结果分成两部分，
左部分为树的左子树中序遍历结果，右部分为树的右子树中序遍历的结果。
根据拆分后的中序遍历结果的长度，可拆分前序遍历结果

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def reConstructBinaryTree(pre, tin):
    if len(pre) == 0:
        return None
    # 存入节点的值
    first = pre[0]
    treeNode = TreeNode(first)
    # 从中序遍历列表中，找到头节点的位置
    firstIndex = tin.index(first)
    # 根据上一步获取的位置，将中序遍历列表切割成左子树和右子树
    leftList = tin[:firstIndex]
    rightList = tin[firstIndex+1:]
    if len(leftList) == 0 and len(rightList) == 0:
        return treeNode
    # 根据切割后的子树的长度，切割前序遍历列表
    leftPre = pre[1:len(leftList)+1]
    rightPre = pre[len(leftList)+1:]
    # 递归
    treeNode.left = reConstructBinaryTree(leftPre, leftList)
    treeNode.right = reConstructBinaryTree(rightPre, rightList)
    return treeNode

if __name__ == '__main__':
    a = reConstructBinaryTree([1,2,4,3,5,6],[4,2,1,5,3,6])
    print(a)