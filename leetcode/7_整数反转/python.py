"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21

注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。
请根据这个假设，如果反转后整数溢出那么就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def reverse(self, x):
        result = 0
        isF = False
        if x < 0:
            isF = True
        x = abs(x)
        while x > 0:
            result = x % 10 + result * 10
            x = x // 10
        if isF:
            result = -result
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-120))
