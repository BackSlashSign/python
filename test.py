class ArrayList:
    def __init__(self):
        self.items = []
        print("Enter a command: i(nsert), e(mpty), g(etEntry), \
c(lear), a(dd), dup, remove, search, f(ind),r(placer), s(ort), \
m(erge), p(rint): ")
        self.CommandInput()

    def add(self, elem):
        self.items.append(elem)

    def remove(self, elem):
        for i in range(self.items.__len__()) :
            if self.items[i] == elem :
                return print("{0} removed".format(elem))
        return print("no such element")

    def insert(self, pos, elem):
        return self.items.insert(int(pos), int(elem))

    def delete(self, pos):
        return self.items.pop(int(pos))

    def isEmpty(self):
        if self.items.__len__() > 0 :
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
        return print(self.items.__len__())

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
        self.items[pos] = elem
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
    
    def print(self, msg = "ArrayList"):
        print("{0} {1} {2}".format(msg, self.items.__len__(), self.items))
        return 

    def dup(self):                   #중복제거 새로 리스트를 만든뒤 반복문을 이용해서 중복을 제거
            new_list = []
            for i in self.items:
                if i not in new_list:
                    new_list.append(i)
            return new_list
    
    def CommandInput(self):
        while True :
            command = input()
            if command == 'i':
                pos = int(input())
                elem = input()
                self.insert(pos, elem)
            elif command == 'a':
                elem = input()
                self.add(elem)
            elif command == 'd':
                pos = int(input())
                self.delete(pos)
            elif command == 'r':
                pos = int(input())
                elem = input()
                self.replace(pos, elem)
            elif command == 'q' : return
            elif command == 'p' : self.print()

def main():
    arraylst = ArrayList()
    
main()
