"""

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

