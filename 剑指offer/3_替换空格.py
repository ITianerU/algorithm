"""
#### 题目描述

将一个字符串中的空格替换成 "%20"。

```text
Input:
"A B"

Output:
"A%20B"
```

#### 解题思路

在字符串尾部填充任意字符，使得字符串的长度等于替换之后的长度。因为一个空格要替换成三个字符（%20），因此当遍历到一个空格时，需要在尾部填充两个任意字符。

令 P1 指向字符串原来的末尾位置，P2 指向字符串现在的末尾位置。P1 和 P2 从后向前遍历，当 P1 遍历到一个空格时，就需要令 P2 指向的位置依次填充 02%（注意是逆序的），否则就填充上 P1 指向字符的值。

从后向前遍是为了在改变 P2 所指向的内容时，不会影响到 P1 遍历原来字符串的内容。
"""
def replaceSpace(str):
    strList = list(str)
    first = len(str) - 1
    for s in str:
        if s == " ":
            strList.append(" ")
            strList.append(" ")
    second = len(strList) - 1
    while first >= 0 and second > first:
        s = strList[first]
        first = reduce(first)
        if s == " ":
            strList[second] = "0"
            second = reduce(second)
            strList[second] = "2"
            second = reduce(second)
            strList[second] = "%"
            second = reduce(second)
        else:
            strList[second] = s
            second = reduce(second)
    return "".join(strList)

def reduce(num):
    num = num - 1
    return num

if __name__ == '__main__':
    print(replaceSpace("a 9 i f asdf kf "))
