package ��ָoffer;

import java.util.ArrayList;
import java.util.List;

/*#### ��Ŀ����

��β��ͷ��������ӡ��ÿ������ֵ��
#### ����˼·

##### ʹ�õݹ�

Ҫ�����ӡ���� 1->2->3��3,2,1)�������������ӡ���� 2->3(3,2)������ٴ�ӡ��һ���ڵ� 1�������� 2->3 ���Կ���һ���µ�����Ҫ�����ӡ��������Լ���ʹ����⺯����Ҳ��������⺯���е����Լ�������ǵݹ麯����*/

public class ��β��ͷ��ӡ���� {
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