package ��ָoffer;

import java.util.List;

/*#### ��Ŀ����

��һ���ַ����еĿո��滻�� "%20"��

```text
Input:
"A B"

Output:
"A%20B"
```

#### ����˼·

���ַ���β����������ַ���ʹ���ַ����ĳ��ȵ����滻֮��ĳ��ȡ���Ϊһ���ո�Ҫ�滻�������ַ���%20������˵�������һ���ո�ʱ����Ҫ��β��������������ַ���

�� P1 ָ���ַ���ԭ����ĩβλ�ã�P2 ָ���ַ������ڵ�ĩβλ�á�P1 �� P2 �Ӻ���ǰ�������� P1 ������һ���ո�ʱ������Ҫ�� P2 ָ���λ��������� 02%��ע��������ģ������������� P1 ָ���ַ���ֵ��

�Ӻ���ǰ����Ϊ���ڸı� P2 ��ָ�������ʱ������Ӱ�쵽 P1 ����ԭ���ַ��������ݡ�*/
public class �滻�ո� {
	
	public String replaceSpace(StringBuffer str) {
		int first = str.length()-1;
		int length = str.length();
    	for(int i=0;i<length;i++) {
    		if(str.charAt(i) == ' ') {
    			// �����ո�
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
		�滻�ո� a= new �滻�ո�();
		System.out.println(a.replaceSpace(new StringBuffer("hello world")));

	}

}
