package 剑指offer;

import java.util.List;

/*#### 题目描述

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

从后向前遍是为了在改变 P2 所指向的内容时，不会影响到 P1 遍历原来字符串的内容。*/
public class 替换空格 {
	
	public String replaceSpace(StringBuffer str) {
		int first = str.length()-1;
		int length = str.length();
    	for(int i=0;i<length;i++) {
    		if(str.charAt(i) == ' ') {
    			// 两个空格
    			str.append("  ");
    		}
    	}
    	int seconde = str.length()-1;
    	while(first>=0 && seconde>first) {
    		char c = str.charAt(first--);
    		if(c == ' ') {
    			str.setCharAt(seconde--, '0');
    			str.setCharAt(seconde--, '2');
    			str.setCharAt(seconde--, '%');
    		}else {
    			str.setCharAt(seconde--, c);
    		}
    	}
		return str.toString();
    }
	public static void main(String[] args) {
		替换空格 a= new 替换空格();
		System.out.println(a.replaceSpace(new StringBuffer("hello world")));

	}

}
