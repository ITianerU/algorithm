package 剑指offer;

import java.util.ArrayList;
import java.util.List;

/*#### 题目描述

从尾到头反过来打印出每个结点的值。
#### 解题思路

##### 使用递归

要逆序打印链表 1->2->3（3,2,1)，可以先逆序打印链表 2->3(3,2)，最后再打印第一个节点 1。而链表 2->3 可以看成一个新的链表，要逆序打印该链表可以继续使用求解函数，也就是在求解函数中调用自己，这就是递归函数。*/

public class 从尾到头打印链表 {
	public ArrayList<Integer> printListFromTailToHead(ListNode listNode) {
        List<Integer> list = new ArrayList<Integer>();
        if(listNode != null) {
        	list.addAll(printListFromTailToHead(listNode.next));
            list.add(listNode.val);
        }
        return (ArrayList<Integer>) list;
    }
	
}

class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}