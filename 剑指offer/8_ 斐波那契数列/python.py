"""
#### ��Ŀ����

��쳲��������еĵ� n �n <= 39��
0  n=0
1  n=1
f(n-1)+f(n-2)  n>1
#### ����˼·

���ʹ�õݹ���⣬���ظ�����һЩ�����⡣���磬���� f(4) ��Ҫ���� f(3) �� f(2)������ f(3) ��Ҫ���� f(2) �� f(1)�����Կ��� f(2) ���ظ������ˡ�
"""
def fibonacci(n):
    if n<=0:
        return n;
    nlist = [0 for i in range(n+1) ]
    nlist[0] = 0
    nlist[1] = 1
    for i in range(2, n+1):
        nlist[i] = nlist[i-1] + nlist[i-2]
    return nlist[n]

if __name__ == '__main__':
    print(fibonacci(40))

