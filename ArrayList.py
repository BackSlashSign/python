class ArrayList:
    def __init__(self):
        self.items = []
        print("Enter a command: i(nsert), e(mpty), g(etEntry), \
c(lear), a(dd), dup, remove, search, f(ind),r(placer), s(ort), \
m(erge), p(rint): ")
        self.InputUpdate()

    def add(self, elem):
        self.items.append(elem)
        self.InputUpdate()

    def remove(self, elem):
        for i in range(self.items.__len__()) :
            if self.items[i] == elem :
                return print("{0} removed".format(elem)), self.InputUpdate()
        return print("no such element"), self.InputUpdate()   

    def insert(self, pos, elem):
        return self.items.insert(int(pos), int(elem)), self.InputUpdate()

    def delete(self, pos):
        return self.items.pop(int(pos)), self.InputUpdate()

    def isEmpty(self):
        if self.items.__len__() > 0 :
            return print("True"), self.InputUpdate()
        else :
            return print("False"), self.InputUpdate()

    def getEntry(self, pos):
        if int(pos) > self.items.__len__():
            print("리스트의 범위를 벗어 났습니다 다시 입력하세요")
            return self.InputUpdate()
        else : 
            print(self.items[int(pos)])
            return self.InputUpdate()

    def size(self):
        return print(self.items.__len__()), self.InputUpdate()

    def clear(self):
        return self.items.clear(), self.InputUpdate()

    def search(self, elem):
        for i in range(self.items.__len__()):
            if self.items[i] == elem:
                return print("%s  found"%elem), self.InputUpdate()
        return print("No such element"), self.InputUpdate()

    def find(self, elem):
        for i in range(self.items.__len__()):
            if self.items[i] == elem :
                print("{0}는 {1}번 인덱스에 있습니다.".format(self.items[i], i))
                return self.InputUpdate()
        return print("해당하는 항목이 없습니다. : %s 없음"%elem), self.InputUpdate()

    def replace(self, pos, elem):
        self.items[pos] = elem
        return self.InputUpdate()
    
    def sort(self):
        for i in range(self.items.__len__()):
            self.items[i] = int(self.items[i])
        self.items.sort()
        for i in range(self.items.__len__()):
            self.items[i] = str(self.items[i])
        return self.InputUpdate()
    
    def merge(self,lst):
        self.items.extend(lst)
        return self.InputUpdate()
    
    def print(self, msg = "ArrayList"):
        print("{0} {1} {2}".format(msg, self.items.__len__(), self.items))
        return self.InputUpdate()

    def dup(self):                   #중복제거 새로 리스트를 만든뒤 반복문을 이용해서 중복을 제거
            new_list = []
            for i in self.items:
                if i not in new_list:
                    new_list.append(i)
            return new_list, self.InputUpdate()

    def InputUpdate(self):
        yourInput = input()
        return self.InputSplit(yourInput)

    def InputSplit(self,yourinput):          #초기화 : ArrayList클래스 사용
        inputdata = []
        inputdata = yourinput.split(" ")
        return self.StrFilter(inputdata)
    
    def StrFilter(self,inputdata):
        if inputdata[0] == "a":
            self.add(inputdata[1])
        elif inputdata[0] == "p":
            self.print()
        elif inputdata[0] == "i":
            self.insert(inputdata[1],inputdata[2])
        elif inputdata[0] == "e":
            self.isEmpty()
        elif inputdata[0] == "remove":
            self.remove(inputdata[1])
        elif inputdata[0] == "search":
            self.search(inputdata[1])
        elif inputdata[0] == "s":
            self.sort()
        elif inputdata[0] == "r":
            self.replace(inputdata[1],inputdata[2])
        elif inputdata[0] == "dup":
            self.itmes = self.dup()
        elif inputdata[0] == "m":
            new_lst = inputdata
            new_lst.remove(inputdata[0])
            self.merge(new_lst)
        elif inputdata[0] == "g":
            self.getEntry(inputdata[1])
        elif inputdata[0] == "d":
            self.delete(inputdata[1])
        elif inputdata[0] == "c":
            self.clear()
        elif inputdata[0] == "f":
            self.find(inputdata[1])
        else:
            print("형식에 맞지 않게 입력되었습니다.")
            print("프로그램 종료.")
        return 0

    def quit():
        return 0

def main():
    arraylst = ArrayList()
    
main()
