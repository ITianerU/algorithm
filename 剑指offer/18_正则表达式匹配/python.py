"""
#### 题目描述

请实现一个函数用来匹配包括 '.' 和 '*' 的正则表达式。模式中的字符 '.' 表示任意一个字符，而 '*' 表示它前面的字符可以出现任意次（包含 0 次）。

在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串 "aaa" 与模式 "a.a" 和 "ab*ac*a" 匹配，但是与 "aa.a" 和 "ab\*a" 均不匹配。

#### 解题思路

应该注意到，'.' 是用来当做一个任意字符，而 '*' 是用来重复前面的字符。这两个的作用不同，不能把 '.' 的作用和 '*' 进行类比，从而把它当成重复前面字符一次。
"""

def match(s, pattern):
    # 当s为空，p为空，true
    if len(s) == 0 and len(pattern) == 0:
        return True
    # 当s不为空，p为空，false
    elif len(s) > 0 and len(pattern) == 0:
        return False
    # 当s为空，p不为空，如果p的第二位是*，则p的前两位可以可以相当于空，为true，之后再将p后几位字符串与s进行递归
    elif len(s) == 0 and len(pattern) > 0:
        if len(pattern) > 1 and pattern[1] == '*':
            return match(s, pattern[2:])
        else:
            return False
    else:
        # 当s不为空，p的长度大于1，p的第二位为*
        if len(pattern) > 1 and pattern[1] == '*':
            # 当s的第一位不等于p的第一位，并且上一部已判断p的第二位是*，所有p的前两位匹配为空，后移两位与s递归
            if s[0] != pattern[0] and pattern[0] != '.':
                return match(s, pattern[2:])
            # s的第一位等于p的第一位，此时有三种情况
            # 第一种，让p的前两位匹配为空，p后移两位与s递归
            # 第二种，让p的前两位与s的第一位匹配，s后移一位，p后移两位进行递归
            # 第三种，由于*可代表多次，所以p的前两位与s的前n位进行匹配，所有s后移1位，p不变进行递归
            else:
                return match(s, pattern[2:]) or match(s[1:], pattern[2:]) or match(s[1:], pattern)
        else:
            # 第一位相等，或p的第一位等于., 则进入下一次递归匹配
            if s[0] == pattern[0] or pattern[0] == '.':
                return match(s[1:], pattern[1:])
            else:
                return False



