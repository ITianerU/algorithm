

class Solution:
    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()
    def push(self, node):
        # write code here
        self.stack1.append(node);
    def pop(self):
        # return xx
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop();

if __name__ == '__main__':
    s = Solution()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())
    s.push(4)
    print(s.pop())
    s.push(5)
    print(s.pop())
    print(s.pop())



