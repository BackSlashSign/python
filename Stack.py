class Stack:
    def __init__(self):
        self.top = []
        self.InputUpdate()
    def isEmpty(self):
        bool_ = True
        if len(self.top) == 0:
            bool_ = True
            return print(bool_),self.InputUpdate()
        else :
            bool_ = False
            return print(bool_),self.InputUpdate()
    def size(self):
        return print(str(len(self.top))),self.InputUpdate()
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
        return str(self.top),self.InputUpdate()
    def print(self):
        templst = []
        j=0
        for i in range(len(self.top)-1,-1,-1):
            templst.append(self.top[i])
        return print(templst), self.InputUpdate()
    def quit(self):
        exit()
        return 0

    def push_match(self,item):
        return self.top.append(item)
    def isEmpty_match(self):
        if len(self.top) == 0:
            return 1    #T
        else :
            return 0    #F
    def clear_match(self):
        self.top = []
    def pop_match(self):
        elem = self.top.pop()   
        return elem
    def peek_match(self) :
        if self.isEmpty_match() == 1:
            return 1
        return self.top[int(len(self.top)-1)]
    def matchtest(self,str_):
        braketDict = {')':'(',']':'[','}':'{'}
        self.clear_match()              #초기화 필수
        for char in str_:
            if char in '([{' :          #열린 괄호일때 스택에 저장 
                self.push_match(char)
            elif char in ')]}' :        #닫힌 괄호이면서 스택꼭대기랑 같으면 스택에서 꺼냄
                if self.top:
                    peek = self.pop_match()
                    if braketDict[char] != peek:
                        return False
                else:
                    return False
        return len(self.top) == 0
    def match(self):         
        file = open("stackinput.txt","r")
        lines = file.read()
        lst=[str(i) for i in lines.splitlines()]
        for str_ in lst:
            if self.matchtest(str_) == True :
                print(str_,'\n',"matched")
            elif self.matchtest(str_) == False :
                print(str_,'\n',"not matched")
        return self.InputUpdate()

    def InputUpdate(self):
        yourInput = input()
        return self.InputSplit(yourInput)

    def InputSplit(self,yourinput):          #초기화 : ArrayList클래스 사용
        inputdata = []
        inputdata = yourinput.split(" ")
        return self.StrFilter(inputdata)
    
    def StrFilter(self,inputdata):    #pop, push, peek, size, empty, p(rint), m(atch), q(uit)
        if inputdata[0] == "pop":
            p = self.pop()
            print(p)
        elif inputdata[0] == "push":
            self.push(inputdata[1])
        elif inputdata[0] == "peek":
            print(self.peek())
        elif inputdata[0] == "size":
            print(self.size())
        elif inputdata[0] == "empty":
            self.isEmpty()
        elif inputdata[0] == "p":
            self.print()
        elif inputdata[0] == "m":
            self.match()
        elif inputdata[0] == "q":
            self.quit()
            return 0
        else:
            print("형식에 맞지 않게 입력되었습니다. 다시 입력하세요")
            return self.InputUpdate(self)
        return 0
def main():
    print("Enter a command: pop, push, peek, size, empty, p(rint), m(atch), q(uit)")
    stack = Stack()

main()