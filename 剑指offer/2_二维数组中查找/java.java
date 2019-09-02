package ��ָoffer;

/*��Ŀ����
����һ����ά���飬��ÿһ�д����ҵ������򣬴��ϵ���Ҳ�ǵ������򡣸���һ�������ж�������Ƿ��ڸö�ά�����С�

Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.
Given target = 20, return false.
����˼·
Ҫ��ʱ�临�Ӷ� O(M + N)���ռ临�Ӷ� O(1)������ M Ϊ������N Ϊ ������

�ö�ά�����е�һ������С��������һ��������ߣ�����������һ�������±ߡ���ˣ������Ͻǿ�ʼ���ң��Ϳ��Ը��� target �͵�ǰԪ�صĴ�С��ϵ����С�������䣬��ǰԪ�صĲ�������Ϊ���½ǵ�����Ԫ�ء�*/

public class ��ά�����в��� {
	public boolean Find(int target, int[][] matrix) {
		if(matrix.length == 0 || matrix[0].length == 0) {
			return false;
		}
		int rows = matrix.length;
		int cols = matrix[0].length;
		int col = cols - 1;
		int row = 0;
		while (row<rows && col>=0) {
			if(matrix[row][col] == target) {
				return true;
			}else if(matrix[row][col] > target) {
				col--;
			}else {
				row++;
			}
		}
		return false;
	}
	
	public static void mian(String args[]) {
		��ά�����в��� a = new ��ά�����в���();
		int aarray[][] = {{1,2,8,9},{2,4,9,12},{4,7,10,13},{6,8,11,15}};
		boolean result = a.Find(1,aarray);
		System.out.println(result);
	}
}
