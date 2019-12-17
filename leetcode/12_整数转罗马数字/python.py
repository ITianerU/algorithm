"""
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

示例 1:

输入: 3
输出: "III"
示例 2:

输入: 4
输出: "IV"
示例 3:

输入: 9
输出: "IX"
示例 4:

输入: 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.
示例 5:

输入: 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/integer-to-roman
"""

class Solution(object):
    def intToRoman(self, num):
        result = ""
        while num != 0:
            if num >= 1000:
                c = num // 1000
                for i in range(c):
                    result = result + "M"
                num = num % 1000
            elif num >= 900:
                result = result + "CM"
                num = num % 100
            elif num >= 500:
                c = (num - 500) // 100
                result = result + "D"
                for i in range(c):
                    result = result + "C"
                num = num % 100
            elif num >= 400:
                result = result + "CD"
                num = num % 100
            elif num >= 100:
                c = num // 100
                for i in range(c):
                    result = result + "C"
                num = num % 100
            elif num >= 90:
                result = result + "XC"
                num = num % 10
            elif num >= 50:
                c = (num - 50) // 10
                result = result + "L"
                for i in range(c):
                    result = result + "X"
                num = num % 10
            elif num >= 40:
                result = result + "XL"
                num = num % 10
            elif num >= 10:
                c = num // 10
                for i in range(c):
                    result = result + "X"
                num = num % 10
            elif num == 9:
                result = result + "IX"
                break
            elif num >= 5:
                result = result + "V"
                for i in range(num - 5):
                    result = result + "I"
                break
            elif num == 4:
                result = result + "IV"
                break
            else:
                for i in range(num):
                    result = result + "I"
                break
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(3))