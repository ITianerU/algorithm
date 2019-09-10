"""
��Ŀ����
��һ�������ʼ�����ɸ�Ԫ�ذᵽ�����ĩβ�����ǳ�֮Ϊ�������ת������һ���ǵݼ�����������һ����ת�������ת�������СԪ�ء�
����˼·
����ת����԰�ֿ��Եõ�һ��������СԪ�ص�����ת���飬�Լ�һ���ǵݼ���������顣�µ���ת���������Ԫ����ԭ�����һ�룬�Ӷ��������ģ������һ�룬�����۰����ʵ��㷨��ʱ�临�Ӷ�Ϊ O(logN)��Ϊ�˷��㣬���ｫ log<sub>2</sub>N дΪ logN��
"""
def minNumberInRotateArray(rotateArray):
    if len(rotateArray) == 0:
        return 0
    while len(rotateArray) > 2:
        if rotateArray[0] < rotateArray[-1]:
            return rotateArray[0]
        count = len(rotateArray)//2
        left = rotateArray[:count]
        right = rotateArray[count:]
        if bj(left):
            rotateArray = left
        else:
            rotateArray = right
    return rotateArray[0] if rotateArray[0]<=rotateArray[-1] else rotateArray[-1]


def bj(rotateArray):
    index = 0
    while len(rotateArray) > 1:
        if rotateArray[index] > rotateArray[-(index+1)]:
            return True
        elif rotateArray[index] == rotateArray[-(index+1)]:
            if index>= len(rotateArray)//2:
                return False
            index = index + 1
        else:
            return False
    return False
if __name__ == '__main__':
    print(minNumberInRotateArray([3,3,3,4,5,6,1,1,2,2]))