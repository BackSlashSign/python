class ArrayList:
    def __init__(self):
        self.items = []     #[]이걸로 두번 감싸져있다 [[ㅁㄴㅇㅁㄴㅇㅁ],[ㅈㅁㄴㅇ],[...]]
        self.LineLoad()

    def LineLoad(self):
        File = open("input4.txt","r",encoding="utf8")

        while True:
            line = File.readline()
            if line == "": break
            templst = [str(i) for i in line.splitlines()]
            for i in range(templst.__len__()):
                # self.items.append(templst[i])
                self.add(templst[i])
        self.print()

        # for line in File:
        #     self.add(line.split("\n"))
        # print("self.items : ",self.items)
        # self.print()

    def add(self, elem):
        self.items.append(elem)

    def remove(self, elem):
        for i in range(self.items.__len__()) :
            if self.items[i] == elem :
                return print("{0} removed".format(elem))
        return print("no such element")

    def _insert(self, pos, elemlst):       #elemlest : List
        # print("elemlst_",elemlst)
        # print("elemlst_ length : ",elemlst.__len__())
        for i in range(elemlst.__len__()):
            if elemlst[i] == '*': return
            self.items.insert(int(pos)+i, elemlst[i])
            # print("elemlst_[{0}] : ".format(i),elemlst[i])
        return

    def delete(self, pos1,pos2):
        del self.items[pos1:pos2+1]
        return 0

    def isEmpty(self):
        if self.items.__len__() == 0 :
            return print("True")
        else :
            return print("False")

    def getEntry(self, pos):
        if int(pos) > self.items.__len__():
            print("리스트의 범위를 벗어 났습니다 다시 입력하세요")
            return 
        else : 
            print(self.items[int(pos)])
            return 

    def size(self):
        return self.items.__len__()

    def clear(self):
        return self.items.clear()

    def search(self, elem):
        for i in range(self.items.__len__()):
            if self.items[i] == elem:
                return print("%s  found"%elem)
        return print("No such element")

    def find(self, elem):
        for i in range(self.items.__len__()):
            if self.items[i] == elem :
                print("{0}는 {1}번 인덱스에 있습니다.".format(self.items[i], i))
                return 
        return print("해당하는 항목이 없습니다. : %s 없음"%elem)

    def replace(self, pos, elem):
        self.items[int(pos)-1] = elem
        return 
    
    def sort(self):
        for i in range(self.items.__len__()):
            self.items[i] = int(self.items[i])
        self.items.sort()
        for i in range(self.items.__len__()):
            self.items[i] = str(self.items[i])
        return 
    
    def merge(self,lst):
        self.items.extend(lst)
        return 
    
    def print(self):
        i = 1
        for strLstSplit in self.items: 
            print("{0}> {1}".format(i,strLstSplit))
            i += 1
        return 

    def dup(self):                   #중복제거 새로 리스트를 만든뒤 반복문을 이용해서 중복을 제거
            new_list = []
            for i in self.items:
                if i not in new_list:
                    new_list.append(i)
            return new_list

def myLineEditor():
    lst = ArrayList()
    inputStrLst = []
    while True :
        # print("while load")
        inputCommand = list(map(str,input().split()))
        # print("inputCommand : ",inputCommand)
        if inputCommand[0] == 'i':
            while True:                
                inputStrLst.append(input())
                if inputStrLst[-1] == '*':
                    lst._insert((int(inputCommand[1])-1), inputStrLst)
                    break
                # print(inputStrLst)

        elif inputCommand[0] == 'd':
            lst.delete(int(inputCommand[1])-1,int(inputCommand[2])-1)

        elif inputCommand[0] == 'r':
            inputStrLst.append(input())
            lst.replace(inputCommand[1], inputStrLst[0])

        elif inputCommand[0] == 'p' :
            lst.print()

        elif inputCommand[0] == 'l' :       #load
            filename = "input4.txt"
            outfile = open(filename, "r")
            
            for i in range(lst.size()) :
                outfile.write(lst.getEntry(i) +'\n')
            outfile.close()

        elif inputCommand[0] == 'q' : return 

        inputStrLst.clear()
myLineEditor()
