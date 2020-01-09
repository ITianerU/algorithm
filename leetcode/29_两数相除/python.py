"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-two-integers
"""


class Solution(object):
    def divide(self, dividend, divisor):
        # 被除数为0, 返回0
        if divisor == 0:
            return 0
        # 被除数为1, 直接返回被除数
        if divisor == 1:
            return dividend
        # 被除数为-1, 因为-2^31除以-1, 会大于2^31-1, 所以需要比较
        if divisor == -1:
            # 被除数只要大于 -2**31, 除以-1的结果就不会超出范围
            if dividend > -2 ** 31:
                return -dividend
            return 2 ** 31 - 1
        # 表示最终结果是否为负数
        isFu = False
        # 判断最终结果是否为负数
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            isFu = True
        # 将被除数 和 除数, 都变为正数, 方便计算
        dividend = dividend if dividend > 0 else -dividend
        divisor = divisor if divisor > 0 else -divisor
        # 递归
        result = self.div(dividend, divisor)
        # 当结果为正数时, 判断边界范围
        if not isFu:
            return 2 ** 31 - 1 if result > 2 ** 31 - 1 else result
        return -result

    def div(self, dividend, divisor):
        # 递归结束条件, 如果被除数小于除数, 结束递归
        if dividend < divisor:
            return 0
        # 累计减掉的除数数量, 通过上面的if后, 被除数除以除数至少为1, 所有count默认为1
        count = 1
        # 临时变量, 不影像原来的除数
        tmp = divisor
        # 思路是, 将除数翻倍, 翻倍后, 如果还小于被除数, 就再翻倍, count的数量也跟着翻倍
        while tmp + tmp <= dividend:
            count = count + count  # 最小解翻倍
            tmp = tmp + tmp  # 当前测试的值也翻倍
        # 当除数翻倍后, 大于被除数, 就将被除数 - 减掉一个除数, 参与下次递归
        return count + self.div(dividend - tmp, divisor)