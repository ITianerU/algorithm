/*
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
*/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int temp = 0;
        ListNode first = new ListNode(0);
        ListNode seconde = first;
        while(l1 != null || l2 != null){
            int a = 0;
            int b = 0;
            if(l1 != null){
                a = l1.val;
                l1 = l1.next;
            }
            if(l2 != null){
                b = l2.val;
                l2 = l2.next;
            }
            int sum = temp + a + b;
            if(sum >= 10){
                temp = 1;
            }else{
                temp = 0;
            }
            first.next = new ListNode(sum % 10);
            first = first.next;
        }
        if(temp == 1){
            first.next = new ListNode(1);
        }
        return seconde.next;
    }
}