"""
#### ��Ŀ����

һֻ����һ�ο������� 1 ��̨�ף�Ҳ�������� 2 ��... ��Ҳ�������� n ���������������һ�� n ����̨���ܹ��ж�����������
"""
def jumpFloor(number):
    if number<=2:
        return number
    num = [0 for i in range(number)]
    num[0] = 1
    num[1] = 2
    for i in range(2,number):
        num[i] = num[i-1] + num[i-2]
    return num[number-1]


"""
#### ��Ŀ����

һֻ����һ�ο������� 1 ��̨�ף�Ҳ�������� 2 ��... ��Ҳ�������� n ���������������һ�� n ����̨���ܹ��ж�����������
̨��    ����
 1       1
 2       2
 3       4
 4       8
"""
def jumpFloorII(number):
    if number<=2:
        return number
    num = [0 for i in range(number)]
    num[0] = 1
    num[1] = 2
    for i in range(2,number):
        num[i] = num[i-1] * 2
    return num[number-1]
