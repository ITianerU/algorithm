"""
#### 题目描述

给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

```java
public class TreeLinkNode {

    int val;
    TreeLinkNode left = null;
    TreeLinkNode right = null;
    TreeLinkNode next = null;

    TreeLinkNode(int val) {
        this.val = val;
    }
}
```

#### 解题思路

① 如果一个节点的右子树不为空，那么该节点的下一个节点是右子树的最左节点；

② 否则，向上找第一个左链接指向的树包含该节点的祖先节点。
"""

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

def GetNext(pNode):
    if pNode == None:
        return None
    if pNode.right:
        rightNode = pNode.right
        if rightNode.left:
            return rightNode.left
        return rightNode
    else:
        while pNode.next:
            parentNode = pNode.next
            if parentNode.left == pNode:
                return parentNode
            pNode = parentNode

if __name__ == '__main__':
    node1 = TreeLinkNode(1)
    node2 = TreeLinkNode(2)
    node3 = TreeLinkNode(3)
    node4 = TreeLinkNode(4)
    node5 = TreeLinkNode(5)
    node6 = TreeLinkNode(6)
    node7 = TreeLinkNode(7)
    node2.left = node4
    node2.right = node5
    node2.next = node1
    node3.left = node6
    node3.right = node7
    node3.next = node1
    node1.left = node2
    node1.right = node3
    node4.next = node2
    node5.next = node2
    node6.next = node3
    node7.next = node3


    node = GetNext(node5)
    print("end...")