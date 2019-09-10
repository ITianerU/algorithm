package 剑指offer;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*#### 题目描述

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

② 否则，向上找第一个左链接指向的树包含该节点的祖先节点。*/
public class 重建二叉树 {
	public TreeNode reConstructBinaryTree(int [] pre,int [] in) {
		TreeNode node = new TreeNode(-1);
		int length = in.length;
		if(pre.length == 0 || length == 0) {
			return null;
		}
        int first = pre[0];
        node.val = first;
        int firstIndex = 0;
        for(int i=0;i<length;i++) {
        	if(in[i] == first) {
        		firstIndex = i;
        		break;
        	}
        }
        int leftIn[] = Arrays.copyOf(in, firstIndex);
        int rightIn[] = Arrays.copyOfRange(in, firstIndex+1, length);
        int leftPre[] = Arrays.copyOfRange(pre, 1, leftIn.length+1);
        int rightPre[] = Arrays.copyOfRange(pre, leftIn.length+1, pre.length);
        node.left = reConstructBinaryTree(leftPre, leftIn);
        node.right = reConstructBinaryTree(rightPre, rightIn);
        return node;
    }
	
	public static void main(String args[]) {
		int pre[] = {3,9,20,15,7};
		int in[] = {9,3,15,20,7};
		重建二叉树 a = new 重建二叉树();
		TreeNode node = a.reConstructBinaryTree(pre,in);
		System.out.println("end...");
	}
}

class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;
	TreeNode(int x) {
		val = x; 
	}
}