MAX_SIZE = 3
class Queue:
    def __init__(self):
        self.items = [None] * MAX_SIZE
        self.front = 0
        self.rear = 0
        self.count = 0
        self.maxSize = int(MAX_SIZE)

    def isEmpty(self):
        return self.count == 0
    def isFull(self):
        if self.count == self.maxSize:
            return True
        else :
            return False
    def clear(self):
        self.items.clear()
    def enqueue(self,elem):      #맨뒤에다 집어넣음
        if self.isFull() is not True:    
            for i in range(self.items.__len__()):
                if self.items[i] == None:
                    self.items[i] = elem
                    self.count += 1
                    # print("count:",self.count)
                    return self.items
        elif self.isFull() is True:
            lst = [None] * self.count
            self.resize()
            self.items.extend(lst)
            return self.enqueue(elem)
    def dequeue(self):      #맨앞에서 빼고 출력
        temp = self.items.pop(0)
        # print(temp)
        return temp
    def resize(self):
        self.maxSize = self.maxSize * 2
        # print("maxSize:",self.maxSize)
        # print("count:",self.count)
        return 0
    def peek(self):         #맨앞 요소 확인
        # print(self.items[0])
        return self.items[0]
    def size(self):
        count = 0
        for i in range(self.items.__len__()):
            if self.items[i] is not None:
                count = count + 1
        # print("size:",str(count).rjust(2))
        return int(count)
    def print(self):
        lst = []
        for i in range(self.items.__len__()):
            if self.items[i] is not None:
                lst.append(self.items[i])
        return print(lst)
    def quit(self):
        exit()

class Deque(Queue):
    def __init__(self):
        super().__init__()
    def addRear(self, item):
        return self.enqueue(item)
    def deleteFront(self):
        return self.dequeue()
    def getFront(self):
        return self.peek()
    def addFront(self,item):
        return self.items.insert(0,item)
    def deleteRear(self):
        for i in reversed(range(self.items.__len__())):
            if self.items[i] is not None :
                temp = self.items.pop(i)
                # print(temp)
                return temp

    def getRear(self):
        for i in reversed(range(self.items.__len__())):
            if self.items[i] is not None:
                # print(self.items[i])
                return self.items[i]

def palidrome(file):
    deque = Deque()
    file = open(file,"r")
    lst1 = []
    lst2 = []
    lst1 = file.readlines()
    for i in range(lst1.__len__()):
        lst2.append(lst1[i].lower())
    for i in range(lst2.__len__()):
        lst2[i] = lst2[i].strip()
    # print(lst2)
    
    for i in lst2 :
        for c in i:
            deque.enqueue(c)
        for c in deque.items:
            if c is not None:
                print(c,end="")
        print()
        for j in range(int(deque.size()/2)):
            # print("deque.size()/2:",int(deque.size()/2))
            if deque.size() == 1 or deque.size() == 0:
                print("==> palidrome")
                break
            else:
                if str(deque.getFront()) != str(deque.getRear()):
                    print("==> not palidrome")     
                    break 
            
                elif str(deque.getFront()) == str(deque.getRear()):
                    if deque.size() == 3 or deque.size() == 2:
                        print("==> palidrome")
                        break 
                    deque.deleteFront()
                    deque.deleteRear()
        deque.__init__()        
def main():
    palidrome("input6.txt")
    return

main()