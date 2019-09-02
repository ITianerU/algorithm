package ��ָoffer;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*#### ��Ŀ����

���ݶ�������ǰ���������������Ľ�����ؽ����ö����������������ǰ���������������Ľ���ж������ظ������֡�

#### ����˼·

ǰ������ĵ�һ��ֵΪ���ڵ��ֵ��ʹ�����ֵ�������������ֳ������֣��󲿷�Ϊ�����������������������Ҳ���Ϊ������������������Ľ����*/

public class �ؽ������� {
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
		�ؽ������� a = new �ؽ�������();
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