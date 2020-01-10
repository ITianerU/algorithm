"""
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

 

示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words
"""
import copy
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        length = 0
        result = []
        # 每个子串的长度相同, 求出子串的长度
        wordsLen = len(words[0])
        # 计算出所有子串的总长度
        length = wordsLen * len(words)
        wordsDict = dict()
        # 将子串存到字典中， 子串为key， value为同名子串的数量
        for i in words:
            if i in wordsDict.keys():
                wordsDict[i] += 1
            else:
                wordsDict[i] = 1
        for i in range(len(s) - length + 1):
            # 每次遍历, 截取当前位置 + 子串总长度的字符串
            tmp = s[i:i + length]
            j = 0
            # 深拷贝字典
            tmpWords = copy.deepcopy(wordsDict)
            while True:
                # 截取与子串相同长度的字符串， 判断在字典里是否有该串， 没有就跳出循环
                if tmpWords and tmp[j:j+wordsLen] in tmpWords.keys():
                    # 将对应的值取出， 若大于1，-1， 不然删除该key
                    if tmpWords[tmp[j:j+wordsLen]] > 1:
                        tmpWords[tmp[j:j+wordsLen]] -= 1
                    else:
                        del tmpWords[tmp[j:j+wordsLen]]
                    j += wordsLen
                else:
                    break
            # 判断该字典是否为空， 为空说明子串全部被使用， 添加当前的位置
            if len(tmpWords) == 0:
                result.append(i)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))