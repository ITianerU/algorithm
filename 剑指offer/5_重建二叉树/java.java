package 剑指offer;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*#### 题目描述

根据二叉树的前序遍历和中序遍历的结果，重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

#### 解题思路

前序遍历的第一个值为根节点的值，使用这个值将中序遍历结果分成两部分，左部分为树的左子树中序遍历结果，右部分为树的右子树中序遍历的结果。*/

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