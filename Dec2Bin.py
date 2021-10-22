class Stack:
    def __init__(self):
        self.top = []
    def isEmpty(self):
        bool_ = True
        if len(self.top) == 0:
            bool_ = True
            return print(bool_),self.InputUpdate()
        else :
            bool_ = False
            return print(bool_),self.InputUpdate()
    def size(self):
        return print(len(self.top)),self.InputUpdate()
    def clear(self):
        self.top = []
        return self.InputUpdate()
    def push(self,item):
        self.top.append(item)
        return self.InputUpdate()    
    def pop(self):
        if self.isEmpty is not True:
            elem = self.top.pop()
            return print(elem), self.InputUpdate()
        else :
            print("err")
            return self.InputUpdate()    
    def peek(self) :
        return print(self.top[int(len(self.top)-1)]),self.InputUpdate()
    def __str__(self):
        return self.top,self.InputUpdate()
    def print(self):
        templst = []
        j=0
        for i in range(len(self.top)-1,-1,-1):
            templst.append(self.top[i])
        return print(templst), self.InputUpdate()
    def quit(self):
        return exit()
    
    def Dec2Bin(self):      #decimal to binary
        self.top = []
        print("Enter a decimal number:",end=" ")
        decNum = self.InputUpdate()
        originNum = decNum
        self.recursive(decNum,originNum)
        
    def recursive(self,item,originNum):
        if int(item) == -1:
            return self.quit()
        elif int(item) == 1 :
            self.top.insert(0,item)
            # print(self.top)
            print(originNum," ==>",end=" ")
            for i in self.top:
                print(int(i),end="")
            print()
            return self.Dec2Bin()
        else:
            decNum = int(item) / 2
            item = int(item) % 2
            self.top.insert(0,item)
            return  self.recursive(int(decNum),originNum),self.Dec2Bin()

    def InputUpdate(self):
        yourInput = input()
        return self.StrFilter(yourInput)
    def StrFilter(self,yourInput):   
        if yourInput == -1:
            return self.quit()
        return  yourInput

def main():
    stack = Stack()
    stack.Dec2Bin()
    return
main()
